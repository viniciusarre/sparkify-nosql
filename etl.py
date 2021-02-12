import csv
import decimal as d
from cql_queries import *
from create_tables import create_or_connect_to_keyspace


def main():
    """

     Runs the entire etl flow by: * Getting the lines on the CSV file; * Connecting to the to the keyspace; * Insert each line into the different tables; * Closes the session

    """

    # Connect to the give cluster / keyspace
    print('Getting the lines...')
    lines = get_lines()
    print('Handling insertion...')
    cluster, session = create_or_connect_to_keyspace()
    for i, line in enumerate(lines, 1):
        print('{}/{} lines processed.'.format(i, len(lines)))
        handle_insertion(line, session)
    print('Done!')
    session.shutdown()
    cluster.shutdown()


def get_lines():
    """
     Get and return all the lines from the event_datafile_new file
     which will be inserted into apache cassandra

        Return: list of lines

    """

    file = 'event_datafile_new.csv'
    lines = []

    with open(file, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            lines.append(line)
    return lines


def handle_insertion(line, session):
    """
        Handles the insertion of the CSV line
        Parameters:
            line: The CSV line to be inserted
            session: the apache cassandra connected session
    """
    # Insert into song_artist table
    song_info_by_session_data = (
        line[0],
        line[-2],
        d.Decimal(line[5]),
        int(line[-3]),
        int(line[3]),
    )
    session.execute(song_info_by_session_insert, song_info_by_session_data)

    # Insert into user_song_artist_data table
    song_info_by_artist_data = (
        line[0],
        line[-2],
        d.Decimal(line[5]),
        int(line[-1]),
        line[1],
        line[4],
        int(line[-3]),
        int(line[3])
    )
    session.execute(song_info_by_artist_insert, song_info_by_artist_data)

    # Insert into user_song table
    song_info_by_user_data = (
        line[-2],
        line[1],
        line[4],
    )
    session.execute(song_info_by_user_insert, song_info_by_user_data)


if __name__ == '__main__':
    main()
