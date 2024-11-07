import streamlit as st
from rag_pipeline import generate_response, store_document_embeddings
from preprocessing import extract_text_from_pdf, chunk_text
import os
import tempfile
import re
from database_handler import generate_sql_query,fetch_data_from_db,format_results_as_table
def sanitize_collection_name(name):
    name = re.sub(r'[^\w-]', '', name)
    
    
    if not name[0].isalnum():
        name = '_' + name  
    if not name[-1].isalnum():
        name = name + '_' 
    
    name = name[:63]
    
    return name

# Page title and configuration
st.set_page_config(page_title="Chat Interface", page_icon="🤖")

# Initialize session state for chat history and uploaded file state
if 'history' not in st.session_state:
    st.session_state.history = []

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# # Function to display chat messages in a chat message container style
# def display_chat_messages(messages):
#     for idx, message in enumerate(messages):
#         if 'role' in message and 'content' in message:
#             if message['role'] == 'user':
#                 st.info(f"You: {message['content']}")
#             elif message['role'] == 'bot':
#                 st.success(f"Bot: {message['content']}")

# Sidebar for File Upload and Embeddings
with st.sidebar:
   
    st.title('Ericsson Chat Interface')

    # File uploader for PDFs, DOCX, and TXT files
    uploaded_file = st.file_uploader("Upload a File", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        # Create a temporary directory if it doesn't exist
        temp_dir = os.path.join('data', 'temp')
        os.makedirs(temp_dir, exist_ok=True)

        # Save uploaded file to temporary directory
        collection_name=sanitize_collection_name(uploaded_file.name) 
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

        # Update session state with uploaded file
        st.session_state.uploaded_file = temp_file_path
    db_query=st.checkbox("DB Query")

# Automatically process and store embeddings when a file is uploaded
if st.session_state.uploaded_file:
    
    store_document_embeddings(st.session_state.uploaded_file,collection_name=collection_name, chunk_size=5)
    
    os.remove(st.session_state.uploaded_file)
    st.session_state.uploaded_file = None

# Container for the conversation
conversation_area = st.empty()

# User input for query (moved to sidebar)
with st.sidebar:
    query = st.chat_input('Enter your query:', key='query_input')


    # Handle user query submission

if db_query and query:
    
    query_sql=generate_sql_query(query)
    if(query_sql=="ERROR: cannot modify db"):
        
        with st.chat_message("user"):
            st.markdown(query)
        
        # Add bot response to history
        st.session_state.messages.append({'role': 'user', 'content': query})
        with st.chat_message("assistant"):
            st.markdown(query_sql)
        st.session_state.messages.append({"role":"assistant","content":query_sql})
    else:
        columns,results=fetch_data_from_db(query_sql)
        table=format_results_as_table(columns,results)
        
    
        with st.chat_message("user"):
                st.markdown(query)
    
        # Add bot response to history
        st.session_state.messages.append({'role': 'user', 'content': query})
        with st.chat_message("assistant"):
                st.markdown('Table')
                st.table(table)
        # st.session_state.messages.append({"role":"assistant","content":results})
    


elif query:
        # Add user query to history
        # st.session_state.history.append({'role': 'user', 'content': query})
        # Generate bot response
        with st.chat_message("user"):
            st.markdown(query)
        
        # Add bot response to history
        st.session_state.messages.append({'role': 'user', 'content': query})
        response = generate_response(query)
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role":"assistant","content":response})
            

# # Display updated chat messages
# display_chat_messages(st.session_state.history)
