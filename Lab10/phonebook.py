import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="nurlan2006",
    port = 54322
)
cur = conn.cursor()
if conn.closed:
    print("Соединение с базой данных закрыто.")
else:
    print("Приложение подключено к базе данных.")



def inputData():
    name = input("Insert your name: ")
    number = input("Insert your number: ")
    cur.execute('INSERT INTO phonebook("PersonName", "PhoneNumber") VALUES (%s, %s);', (name, number))
    conn.commit()


def importFromCSV():
    with open("queredData.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('INSERT INTO phonebook("PersonName", "PhoneNumber") VALUES (%s, %s);', (personName, phoneNumber))
    conn.commit()


def update_contact(PersonName, PhoneNumber):
    cur.execute('UPDATE phonebook SET "PhoneNumber" = %s WHERE "PersonName" = %s;', (PhoneNumber, PersonName))
    conn.commit()


def queryData():
    cur.execute('SELECT * FROM phonebook;')
    data = cur.fetchall()
    with open("queredData.txt", "w") as f:
        for row in data:
            f.write(f"Name: {row[1]}\nNumber: {row[2]}\n")


def deleteData():
    personName = input("Which name what to delete?\n")
    cur.execute(f'DELETE FROM phonebook WHERE "PersonName" = %s;', (personName,))
    conn.commit()


def deleteAllData():
    cur.execute('DELETE FROM phonebook;')
    conn.commit()

def queryData(template):
    cur.execute('SELECT * FROM phonebook WHERE "PersonName" LIKE %s OR "PhoneNumber" LIKE %s;', ('%' + template + '%', '%' + template + '%'))
    data = cur.fetchall()
    with open("queredData.txt", "w") as f:
        for row in data:
            f.write(f"Name: {row[1]}\nNumber: {row[2]}\n")


while True:
    print("What do you want to do?\n\
            1. Enter the data manually\n\
            2. Download from the CSV file\n\
            3. Update an existing contact\n\
            4. Request data from the table\n\
            5. Delete the data by name \n\
            6. Delete all data from the table\n\
            7.A function that returns all records based on the template \n\
            8. Exit")

    choice = input("Insert number of act (1-7):\n")
    if choice == '1':
        inputData()
    elif choice == '2':
        importFromCSV()
    elif choice == '3':
        name = input("Insert Name or number by space: ").split()
        update_contact(*name)
    elif choice == '4':
        queryData()
    elif choice == '5':
        deleteData()
    elif choice == '6':
        deleteAllData()
    elif choice == '7':
        template = input
        queryData(template)
    elif choice == '8':
        break

cur.close()
conn.close()