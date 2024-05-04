import psycopg2 as pgsql

def delete_data_by_pattern(pattern):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='nurlan2006',
            host='localhost',
        )
        cur = connection.cursor()

        query = """
            DELETE FROM phone_book 
            WHERE name = %s 
            OR surname = %s 
            OR phone_number = %s;
        """
        cur.execute(query, (pattern, pattern, pattern))
        
        deleted_rows = cur.rowcount
        print(f"Deleted {deleted_rows} rows.")

        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

pat = input('Who do you want to delete?')
delete_data_by_pattern(pat)