import csv
import psycopg2

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


with open('phonebook.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone_number = input("Enter phone number: ")


cur.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))

# Update data in the table
old_first_name = input("Enter the old first name: ")
new_first_name = input("Enter the new first name: ")
new_phone_number = input("Enter the new phone number: ")
cur.execute("UPDATE phonebook SET first_name = %s, phone_number = %s WHERE first_name = %s", (new_first_name, new_phone_number, old_first_name))

cur.execute("SELECT * FROM phonebook")
cur.execute("SELECT * FROM phonebook WHERE first_name = %s", ('Anelya',))
rows = cur.fetchall()
for row in rows:
    print(row)

delete_by = input("Enter 'first_name' or 'phone_number' to delete by: ")
value = input(f"Enter {delete_by}: ")
cur.execute(f"DELETE FROM phonebook WHERE {delete_by} = %s", (value,))


conn.commit()
cur.close()
conn.close()
