import psycopg2
# from config import host,user,password,database
select_all = "SELECT * FROM USERS"

try:
    connection = psycopg2.connect(
        host='localhost',
        user="postgres",
        password="postgres",
        database="parking"
    )
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM public.cars_user;"
        )

        print("Cars user - " , {cursor.fetchone()})
        print(cursor.fetchone())
except Exception as ex:
    print("Error - ", ex)