import csv
import os
import shutil
import re
import psycopg2
from decouple import config as env_conf
from datetime import datetime


# File path.
file_path = env_conf('SOURCE_FILE_PATH')
archive_file_path = env_conf('ARCHIVE_FILE_PATH')
file_name = env_conf('SOURCE_FILE_NAME')
host = env_conf('POSTGRES_HOST')
db_name = env_conf('POSTGRES_DATABASE')
user = env_conf('POSTGRES_USER')
pwd = env_conf('POSTGRES_PWD')

# Database connection variable.
connect = None

# Check if the CSV file exists.
if os.path.isfile(file_path + file_name):

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

    # Batchid variable
    batchid = datetime.now()

    with open(file_path + file_name, 'rt') as Data:
        # Assign CSV file to reader object.
        reader = csv.DictReader(Data)

        # Record count.
        recordCount = 0
        # Insert data nto the database.
        for row in reader:

            # SQL to insert task information.
            sqlInsert = \
                "INSERT INTO task_data (id, timestamp, temperature, duration, batch_id)  \
                VALUES (%s, %s, %s, %s, %s)"

            try:

                # Execute query and commit changes.
                cursor.execute(sqlInsert, (row['id'],
                                           row['timestamp'],
                                           row['temperature'],
                                           row['duration'],
                                           batchid))
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

    # Move src to archive directory
    archive_batch_id = re.sub(r"[^a-zA-Z0-9]", "", str(batchid))
    shutil.move(file_path + file_name, archive_file_path + archive_batch_id + '_task_data.csv')

else:

    # Message stating CSV file could not be located.
    print("Could not locate the CSV file.")
