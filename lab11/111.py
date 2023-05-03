import csv
import psycopg2
import os

os.chdir('C:/Users/ASUS/Desktop/pp2/lab10')

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="postgres", user="postgres", password="anel2004", host="localhost", port="5433")
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255),
        phone_number VARCHAR(20) NOT NULL
    );
""")
conn.commit()


def search(pattern):
    cur.execute("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone_number LIKE %s", (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def insert_or_update(first_name, last_name, phone_number):
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (first_name,))
    rows = cur.fetchall()
    if len(rows) == 0:
        cur.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))
    else:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (phone_number, first_name))


def insert_many(user_list):
    incorrect_data = []
    for user in user_list:
        if len(user) != 2 or not user[1].isdigit():
            incorrect_data.append(user)
            continue
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (user[0],))
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (user[0], user[1]))
        else:
            cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (user[1], user[0]))
    return incorrect_data


def paginate(limit, offset):
    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_by(delete_by, value):
    cur.execute(f"DELETE FROM phonebook WHERE {delete_by} = %s", (value,))


# Test the functions and procedures

with open('phb.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    for row in reader:
        insert_or_update(row[0], row[1], row[2])


search_pattern = input("Enter a search pattern: ")
search(search_pattern)


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone_number = input("Enter phone number: ")
insert_or_update(first_name, last_name, phone_number)


user_list = [
    ('John', '123456'),
    ('Mary', 'abc'),
    ('Alice', '789012'),
]
incorrect_data = insert_many(user_list)
print(f"Incorrect data: {incorrect_data}")


paginate_limit = input("Enter the number of records to fetch: ")
paginate_offset = input("Enter the offset: ")
paginate(paginate_limit, paginate_offset)


delete_by = input("Enter 'first_name' or 'phone_number' to delete by: ")
value = input(f"Enter {delete_by}: ")

delete_by(delete_by, value)
