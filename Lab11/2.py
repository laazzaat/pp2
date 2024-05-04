import psycopg2 as pgsql

def create_insert_or_update():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='nurlan2006',
            host='localhost',
        )
        cur = connection.cursor()

        cur.execute("""
            CREATE OR REPLACE FUNCTION insert_or_update_user(name_param TEXT, surname_param TEXT, phone_param TEXT) 
            RETURNS VOID AS 
            $$
            BEGIN
                IF EXISTS (SELECT 1 FROM phone_book WHERE name = name_param OR surname = surname_param) THEN
                    UPDATE phone_book SET phone_number = phone_param WHERE name = name_param OR surname = surname_param;
                ELSE
                    INSERT INTO phone_book (name, surname, phone_number) VALUES (name_param, surname_param, phone_param);
                END IF;
            END;
            $$
            LANGUAGE plpgsql;
        """)

        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

def insert_or_update_user(name, surname, phone):
    try:
        connection = pgsql.connect(
            database="PhoneBook",
            user='postgres',
            password='sasha...',
            host='localhost',
        )
        cur = connection.cursor()
        cur.callproc('insert_or_update_user', (name, surname, phone))
        
        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

create_insert_or_update()
insert_or_update_user('Nuriman', 'Baltabayev', '1234567890')