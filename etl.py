import cassandra
import re
import os
import glob
import json
import csv
import decimal as d
from cql_queries import *
from create_tables import create_or_connect_to_keyspace


def connect_and_insert():
    # Connect to the give cluster / keyspace
    session, cluster = create_or_connect_to_keyspace()
    lines = get_lines()
    print(lines)
    for line in lines:
        handle_insertion(line)
    session.shutdown()
    cluster.shutdown()


def get_lines():
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

        # join the file path and roots with the subdirectories using glob
    file_path_list = glob.glob(os.path.join(root, '*'))
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = []

    # for every filepath in the file path list
    for f in file_path_list:
        # reading csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader)

    # extracting each data row one by one and append it
            for line in csvreader:
                # print(line)
                full_data_rows_list.append(line)

    # uncomment the code below if you would like to get total number of rows
    # print(len(full_data_rows_list))
    # uncomment the code below if you would like to check to see what the list of event data rows will look like
    # print(full_data_rows_list)

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect(
        'myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    file = 'event_datafile_new.csv'

    with open(file, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        return csvreader


def handle_insertion(line):
    # Insert into song_artist table
    song_artist_data = (
        line[0],
        line[-2],
        d.Decimal(line[5]),
        int(line[-3]),
        int(line[3]),
    )
    session.execute(song_artist_insert, song_artist_data)

    # Insert into user_song_artist_data table
    user_song_artist_data = (
        line[0],
        line[-2],
        d.Decimal(line[5]),
        int(line[-1]),
        line[1],
        line[4],
        int(line[-3]),
        int(line[3])
    )
    session.execute(user_song_artist_insert, user_song_artist_data)

    # Insert into user_song table
    user_song_data = (
        line[-2],
        line[1],
        line[4],
    )
    session.execute(user_song_insert, user_song_data)


if __name__ == '__main__':
    connect_and_insert()
