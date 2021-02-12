

############################### CREATE  / DROP FLOW #############################

# CQL query for dropping the song_artist table
song_artist_table_drop = 'DROP TABLE IF EXISTS song_artist;'
# CQL query for dropping the user_song_artist table
user_song_artist_table_drop = 'DROP TABLE IF EXISTS user_song_artist;'
# CQL query for dropping the song_artist table
user_song_table_drop = 'DROP TABLE IF EXISTS user_song;'

# CQL query for creating the song_artist table
song_artist_table_create = (
    'CREATE TABLE IF NOT EXISTS song_artist (\
       artist TEXT,  \
       song TEXT, \
       song_length DECIMAL, \
       session_id INT, \
       item_in_session INT, \
       PRIMARY KEY (session_id, item_in_session)\
    )'
)

# CQL query for creating the user_song_artist table
user_song_artist_table_create = (
    'CREATE TABLE IF NOT EXISTS user_song_artist(\
       artist TEXT,  \
       song TEXT, \
       song_length DECIMAL, \
       user_id INT, \
       first_name TEXT, \
       last_name TEXT, \
       session_id INT, \
       item_in_session INT, \
       PRIMARY KEY (user_id, session_id, item_in_session)\
    )'
)

# CQL query for creating the user_song table
user_song_table_create = (
    'CREATE TABLE IF NOT EXISTS user_song (\
        song TEXT, \
        first_name TEXT,\
        last_name TEXT, \
        PRIMARY KEY (song)\
    )'
)

# create table queries tuple
create_table_queries = (song_artist_table_create,
                        user_song_artist_table_create, user_song_table_create)

# create table queries tuple
drop_table_queries = (song_artist_table_drop,
                      user_song_artist_table_drop, user_song_table_drop)


############################### END OF CREATE  / DROP FLOW #############################

############################### INSERTIONS ###############################

song_artist_insert = "INSERT INTO song_artist \
    (artist, song, song_length, session_id, item_in_session) \
    VALUES (%s, %s, %s, %s, %s)\
"

user_song_artist_insert = "INSERT INTO user_song_artist \
    (artist, song, song_length, user_id, first_name, last_name, session_id, item_in_session) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)\
"

user_song_insert = "INSERT INTO user_song \
    (song, first_name, last_name) \
    VALUES (%s, %s, %s)\
"
###############################################################################

############################### QUERIES ###############################

# These are the test queries mentioned on the introduction notebook.

song_artist_query = "\
  SELECT artist, song, song_length FROM song_artist WHERE session_id = %s AND item_in_session = %s \
"

user_song_artist_query = "\
  SELECT artist, song, first_name, last_name FROM user_song_artist WHERE user_id = %s AND session_id = %s \
"

user_song_query = """SELECT first_name, last_name FROM user_song WHERE song = %s """
###############################################################################
