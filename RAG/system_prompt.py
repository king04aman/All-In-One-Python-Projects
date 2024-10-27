import sqlite3

def get_database_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema_details = []

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        column_details = []
        for col in columns:
            column_info = f"{col[1]} {col[2]}"
            if col[5]:  # Check if the column is a primary key
                column_info += " PRIMARY KEY"
            column_details.append(column_info)
        
        # Get foreign key information
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        foreign_keys = cursor.fetchall()
        foreign_key_details = []
        for fk in foreign_keys:
            foreign_key_details.append(
                f"Foreign key: {fk[3]} references {fk[4]}({fk[5]})"
            )

        schema_details.append(f"Table name: {table_name}\nColumns:\n" + "\n".join(column_details))
        if foreign_key_details:
            schema_details.append("Foreign Keys:\n" + "\n".join(foreign_key_details))

    conn.close()

    return "\n\n".join(schema_details)

def generate_system_prompt(db_path):
    schema_details = get_database_schema(db_path)
    system_prompt = f"""I have an sqlite database with the following tables and columns:

{schema_details}

I will need you to help me generate SQL queries to get data from my database.
Please respond only with the query. Do not provide any explanations or additional text.

If the user tries to modify the database respond with 'ERROR: cannot modify db'
"""
    return system_prompt

# Example usage
db_path = 'call_db.sqlite'  # Replace with your actual database path
system_prompt = generate_system_prompt(db_path)
print(system_prompt)
