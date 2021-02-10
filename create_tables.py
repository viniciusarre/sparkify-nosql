from cassandra.cluster import Cluster
from cql_queries import create_table_queries, drop_table_queries


def create_or_connect_to_keyspace():
    """
    - Create keyspace if non-existant
    - Returns the session after being set to the given keyspace

    """
    try:
        # If you have a locally installed Apache Cassandra instance
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS sparkify 
            WITH REPLICATION = 
            { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
                        )
        session.set_keyspace('sparkify')

    except Exception as e:
        print(e)
        raise Exception(e)

    return cluster, session


def drop_tables(session):
    """

    Drops each table using the queries in `drop_table_queries` list.

    """
    for query in drop_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)
            raise Exception(e)


def create_tables(session):
    """

    Creates each table using the queries in `create_table_queries` list. 

    """
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)
            raise Exception(e)


def main():
    """

    - Creates and/or connect to the sparkify keyspace
    - Drops all tables
    - Creates all tables
    - Closes the session and cluster

    """
    try:
        cluster, session = create_or_connect_to_keyspace()
        drop_tables(session)
        create_tables(session)

        session.shutdown()
        cluster.shutdown()
        print("Tables created successfully!")

    except Exception as e:
        print('An error occurred ', e)


if __name__ == '__main__':
    main()
