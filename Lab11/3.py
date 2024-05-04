import psycopg2 as pgsql

def create_insert_many_users_proc():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='nurlan2006',
            host='localhost',
        )
        cur = connection.cursor()

        cur.execute("""
            CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], surnames TEXT[], phones TEXT[]) RETURNS TEXT[] AS $$
            DECLARE
                incorrect_data TEXT[];
                i INT := 1;
            BEGIN
                WHILE i <= array_length(names, 1) LOOP
                    IF length(phones[i]) <> 10 OR NOT phones[i] ~ '^\d+$' THEN
                        incorrect_data := array_append(incorrect_data, names[i] || ' - ' || phones[i]);
                    ELSE
                        INSERT INTO phone_book (name, surname, phone_number) VALUES (names[i], surnames[i], phones[i]);
                    END IF;
                    i := i + 1;
                END LOOP;
                RETURN incorrect_data;
            END;
            $$ LANGUAGE plpgsql;
        """)

        connection.commit()
        print("Stored procedure created successfully!")

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

def insert_many_users(names, surnames, phones):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='nurlan2006',
            host='localhost',
        )
        cur = connection.cursor()

        cur.callproc('insert_many_users', (names, surnames, phones))
        incorrect_data = cur.fetchone()

        if incorrect_data:
            print("Incorrect Data:")
            for data in incorrect_data:
                print(data)
        else:
            print("All users inserted successfully!")

        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

create_insert_many_users_proc()
names = ['Anvar', 'Abylay']
surnames = ['Zhakupov', 'Akhmetov']
phones = ['7772394389','7890123456']
insert_many_users(names, surnames, phones)