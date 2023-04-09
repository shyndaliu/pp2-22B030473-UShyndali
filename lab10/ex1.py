import csv
import psycopg2 as pgsql


connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="12345", port=5432)
cur=connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    id INT,
    name VARCHAR(255),
    number INT
);
""")

def update(id, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE id = {}
    """.format(mode,newv,id))

def delete(id):
    cur.execute("""DELETE FROM Phonebook
    WHERE id={}
    """.format(id))

#INSERTING DATA--------------------------

mode="enter";
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    mytuple=[]
    print("enter id:")
    mytuple.append(input())
    print("enter name:")
    mytuple.append(input())
    print("enter number:")
    mytuple.append(input())
    mytuple=tuple(mytuple)
    cur.execute("""INSERT INTO PhoneBook (id, name ,number) VALUES
    {};
    """.format(mytuple))

while True:
    print("Want to insert data from csv file? yes/no:")
    mode=input()
    if mode=="no":
        break
    print("enter the name of the file")
    mode=input()
    with open(mode+'.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)",row)

#UPDATING DATA---------
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter id")
    idtochange=input()
    print("What you want to change? name/number")
    mode=input()
    print("Enter new name/number")
    newvalue=input()
    update(idtochange, mode, newvalue)

#DELETING DATA-----------
while True:
    print("want to delete some data? yes/no")
    mode=input()
    if mode=="no":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter id")
    idtodelete=input()
    delete(idtodelete)


connection.commit()
cur.close()
connection.close()
