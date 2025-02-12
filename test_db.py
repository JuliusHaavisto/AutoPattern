import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Timed out trying to connect to our Azure DB because inproper DB values in .env FIXED
try:
    print("Attempting to connect to the database...")

    # Establish connection
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER=tcp:{server},1433;'  #Could be inside .env but for now it stays in here
        f'DATABASE={database};'
        f'UID={username};PWD={password};'
        f'Encrypt=yes;TrustServerCertificate=no;'
        f'Connection Timeout=30;'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print("Connected to:", row[0])

    # Close the connection
    conn.close()

except pyodbc.Error as ex:
    print("X Connection failed!")
    print("Error:", ex)
