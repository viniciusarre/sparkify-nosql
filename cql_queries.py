

############################### CREATE  / DROP FLOW #############################

# CQL query for dropping the song_info_by_session table
song_info_by_session_table_drop = 'DROP TABLE IF EXISTS song_info_by_session;'
# CQL query for dropping the song_info_by_artist table
song_info_by_artist_table_drop = 'DROP TABLE IF EXISTS song_info_by_artist;'
# CQL query for dropping the song_info_by_session table
song_info_by_user_table_drop = 'DROP TABLE IF EXISTS song_info_by_user;'

# CQL query for creating the song_info_by_session table
song_info_by_session_table_create = (
    'CREATE TABLE IF NOT EXISTS song_info_by_session (\
       session_id INT, \
       item_in_session INT, \
       artist TEXT,  \
       song TEXT, \
       song_length DECIMAL, \
       PRIMARY KEY (session_id, item_in_session)\
    )'
)

# CQL query for creating the song_info_by_artist table
song_info_by_artist_table_create = (
    'CREATE TABLE IF NOT EXISTS song_info_by_artist(\
       user_id INT, \
       session_id INT, \
       item_in_session INT, \
       artist TEXT,  \
       song TEXT, \
       song_length DECIMAL, \
       first_name TEXT, \
       last_name TEXT, \
       PRIMARY KEY ((user_id, session_id), item_in_session)\
    )'
)

# CQL query for creating the song_info_by_user table
song_info_by_user_table_create = (
    'CREATE TABLE IF NOT EXISTS song_info_by_user (\
        song TEXT, \
        user_id INT ,\
        first_name TEXT,\
        last_name TEXT, \
        PRIMARY KEY ((song, user_id))\
    )'
)

# create table queries tuple
create_table_queries = (song_info_by_session_table_create,
                        song_info_by_artist_table_create, song_info_by_user_table_create)

# create table queries tuple
drop_table_queries = (song_info_by_session_table_drop,
                      song_info_by_artist_table_drop, song_info_by_user_table_drop)


############################### END OF CREATE  / DROP FLOW #############################

############################### INSERTIONS ###############################

song_info_by_session_insert = "INSERT INTO song_info_by_session \
    (session_id, item_in_session, artist, song, song_length) \
    VALUES (%s, %s, %s, %s, %s)\
"

song_info_by_artist_insert = "INSERT INTO song_info_by_artist \
    (user_id, session_id, item_in_session, artist, song, song_length,  first_name, last_name) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)\
"

song_info_by_user_insert = "INSERT INTO song_info_by_user \
    (song, user_id, first_name, last_name) \
    VALUES (%s, %s, %s, %s)\
"
###############################################################################

############################### QUERIES ###############################

# These are the test queries mentioned on the introduction notebook.

song_info_by_session_query = "\
  SELECT artist, song, song_length FROM song_info_by_session WHERE session_id = %s AND item_in_session = %s \
"

song_info_by_artist_query = "\
  SELECT artist, song, first_name, last_name FROM song_info_by_artist WHERE user_id = %s AND session_id = %s \
"

song_info_by_user_query = """SELECT first_name, last_name FROM song_info_by_user WHERE song = %s """
###############################################################################
