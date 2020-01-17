import csv
import os
import psycopg2

# File path.
filePath = 'D:\\jerin\\Employment\\german-test\\task_data.csv'

# Database connection variable.
connect = None

# Check if the CSV file exists.
if os.path.isfile(filePath):

    try:

        # Connect to database.
        connect = psycopg2.connect(host='localhost', database='db1',
                                   user='postgres', password='root')

    except psycopg2.DatabaseError as e:

        # Confirm unsuccessful connection and stop program execution.
        print("Database connection unsuccessful.")
        quit()

    # Cursor to execute query.
    cursor = connect.cursor()

    # Assign CSV file to reader object.
    reader = csv.DictReader(open(filePath))

    # Record count.
    recordCount = 0

    # Insert person information into the database.
    for row in reader:

        # SQL to insert person information.
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

            # Confirm error adding person information and stop program execution.
            print("Error adding person information.")
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