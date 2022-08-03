import sqlite3

#check that it has been imported successfully
print("Module imported successfully!")

#create a database
conn = sqlite3.connect("SGA_1_3_learners.db")

#check that creation and connection is successful
print("SGA_1_3_learners created successfully!"); print (type(conn))

#create a cursor that allows the SQL statements to be executed
cursor = conn.cursor()

#check that cursor is created successfully
print("Cursor created successfully! \n", type(cursor))

#create a table called learners with four columns that accepts text inputs
# cursor.execute("""
#                 CREATE TABLE learners (
#                 first_name text,
#                 last_name text,
#                 email text,
#                 course text
#                 )
# """)

#check that the table executed successfully
print("Table created successfully!")

#commit the database and table
conn.commit()

#close the connection to the database
conn.close()


