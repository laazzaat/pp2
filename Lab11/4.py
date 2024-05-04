import psycopg2 as pgsql

def paginate_query(table_name, limit, offset):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='nurlan2006',
            host='localhost',
        )
        cur = connection.cursor()

        query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s;"
        cur.execute(query, (limit, offset))
        
        rows = cur.fetchall()

        for row in rows:
            print(row)

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

paginate_query('phone_book', limit=5, offset=0)