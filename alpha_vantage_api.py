import requests
from config import O3Q10FAT8BRW0KEY

def get_crypto_data():
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={O3Q10FAT8BRW0KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API request: {str(e)}")
        return None

crypto_data = get_crypto_data()
if crypto_data:
    print(crypto_data)

from config import API_KEY
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE

def establish_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        return conn
    except mysql.connector.Error as error:
        print(f"Error connecting to the database: {error}")
        return None

conn = establish_db_connection()
if not conn:
    
    print("Failed to establish a database connection.")
crypto_data = get_crypto_data()
if crypto_data:
    print(crypto_data)


