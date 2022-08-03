import sqlite3

#connect to a database 
conn = sqlite3.connect("SGA_1_3_learners.db")

#create a cursor
cursor = conn.cursor()

#querying the learners table
cursor.execute(
    """
    SELECT * FROM learners
    """
)

#check
print("Query executed!")

items = cursor.fetchall()
# print(items)

#format output to display in a tabular form
print("first_name" + "\tlast_name" "\temail" "\t\t\t\t\tcourse \n" f"{'.' * 90}")

#loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email:30}\t\t{course}")

#commit the database and table
conn.commit()

#close the connection to the database
conn.close()

