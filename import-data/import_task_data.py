import csv
import os
import psycopg2
from decouple import config as env_conf

# File path.
file_path = env_conf('FILEPATH')
host = env_conf('POSTGRES_HOST')
db_name = env_conf('POSTGRES_DATABASE')
user = env_conf('POSTGRES_USER')
pwd = env_conf('POSTGRES_PWD')

# Database connection variable.
connect = None

# Check if the CSV file exists.
if os.path.isfile(file_path):

    try:

        # Connect to database.
        connect = psycopg2.connect(host=host, database=db_name,
                                   user=user, password=pwd)

    except psycopg2.DatabaseError:

        # Confirm unsuccessful connection and stop program execution.
        print("Database connection unsuccessful.")
        quit()

    # Cursor to execute query.
    cursor = connect.cursor()

    # Assign CSV file to reader object.
    reader = csv.DictReader(open(file_path))

    # Record count.
    recordCount = 0
    # Clear existing data
    cursor.execute("DELETE FROM task_data")
    # Insert data nto the database.
    for row in reader:

        # SQL to insert data information.
        sqlInsert = \
            "INSERT INTO task_data (id, timestamp, temperature, duration)  \
             VALUES (%s, %s, %s, %s)"

        try:

            # Execute query and commit changes.
            cursor.execute(sqlInsert, (row['id'],
                                       row['timestamp'],
                                       row['temperature'],
                                       row['duration']))
            connect.commit()

            # Increment the record count.
            recordCount += 1

        except psycopg2.DatabaseError as e:

            # Confirm error adding data and stop program execution.
            print("Error adding person information.", e)
            quit()

    # Close database connection.
    connect.close()

    # Provide feedback on the number of records added.
    if recordCount == 0:

        print("No new records added.")

    elif recordCount == 1:

        print(str(recordCount) + " task record added.")

    else:

        print(str(recordCount) + " task records added.")

else:

    # Message stating CSV file could not be located.
    print("Could not locate the CSV file.")
