import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='admin')
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS royal_court")
    conn.commit()
    conn.close()
    print("Database 'royal_court' created successfully.")
except Exception as e:
    print(f"Failed to create database: {e}")
