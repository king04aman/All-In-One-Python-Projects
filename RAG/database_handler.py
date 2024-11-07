# database_handler.py
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# System prompt for the Gemini model
system_prompt = """
I have an sqlite database with the following tables and columns:

Table name: RatePlan
Columns:
RatePlanId INTEGER PRIMARY KEY
Name VARCHAR(255)
MonthlyFee FLOAT
CallRate FLOAT
SmsRate FLOAT
DataRate FLOAT


Table name: Customer
Columns:
CustomerId INTEGER PRIMARY KEY
FirstName VARCHAR(255)
LastName VARCHAR(255)
Address VARCHAR(255)
City VARCHAR(255)
State VARCHAR(255)
Country VARCHAR(255)
PostalCode VARCHAR(255)
Phone VARCHAR(255)
Email VARCHAR(255)
RatePlanId INT
ContractStart DATE
ContractEnd DATE

Foreign Keys:
Foreign key: RatePlanId references RatePlanId(NO ACTION)

Table name: Phone
Columns:
PhoneId INTEGER PRIMARY KEY
Brand VARCHAR(255)
Model VARCHAR(255)
OS VARCHAR(255)
Price FLOAT

Table name: CustomerPhone
Columns:
CustomerPhoneId INTEGER PRIMARY KEY
CustomerId INT
PhoneId INT
PhoneAcquisitionDate DATE

Foreign Keys:
Foreign key: PhoneId references PhoneId(NO ACTION)
Foreign key: CustomerId references CustomerId(NO ACTION)

Table name: CDR
Columns:
CdrId INTEGER PRIMARY KEY
CustomerId INT
PhoneNumber VARCHAR(255)
CallDateTime DATETIME
CallType VARCHAR(255)
DurationInSeconds INT
DataUsageKb INT
SmsCount INT

Foreign Keys:
Foreign key: CustomerId references CustomerId(NO ACTION)

I will need you to help me generate SQL queries to get data from my database.
Please respond only with the query in simple text format. Do not provide any explanations or additional text.

If the user tries to modify the database respond with 'ERROR: cannot modify db'
"""

# Initialize chat with system prompt
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
chat.send_message(system_prompt)

def generate_sql_query(prompt):
    response = chat.send_message(prompt)
    sql_query = response.text.strip()
    if(sql_query=="ERROR: cannot modify db"):return "ERROR: cannot modify db"
    sql_query = sql_query.replace('```sql', '').replace('```', '').strip()
    print(sql_query)
    return sql_query

def fetch_data_from_db(sql_query, db_path='/media/tejas/b25dc664-2aec-424c-8f6c-f895bbec7e5d/Ericsson_RAG/call_db.sqlite'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    cursor.execute(sql_query)
    results = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()
    return columns, results

def format_results_as_table(columns, results):
    table = [columns]
    table.extend(results)
    return table


