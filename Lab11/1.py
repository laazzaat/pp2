import psycopg2 as pgsql

def search_records(pattern):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='nurlan2006',
            host='localhost',
        )

        cur = connection.cursor()

        query = "SELECT * FROM phonebook WHERE name LIKE %s OR surname LIKE %s OR phonenumber LIKE %s"
        cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

        records = cur.fetchall()

        return records

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

pattern = input("Search: ...")
matching_records = search_records(pattern)
print("Matching Records:")
for record in matching_records:
    print(record)