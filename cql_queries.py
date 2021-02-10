song_artist_table_drop = 'DROP TABLE IF EXISTS song_artist;' # CQL query for dropping the song_artist table
user_song_artist_table_drop = 'DROP TABLE IF EXISTS user_song_artist;' # CQL query for dropping the user_song_artist table
user_song_table_drop = 'DROP TABLE IF EXISTS user_song;' # CQL query for dropping the song_artist table

# CQL query for creating the song_artist table
song_artist_table_create = (
    'CREATE TABLE IF NOT EXISTS song_artist (\
       artist TEXT,  \
       song TEXT, \
       song_length NUMERIC, \
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
       song_length NUMERIC, \
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
create_table_queries = (song_artist_table_create, user_song_artist_table_create, user_song_table_create)

# create table queries tuple
drop_table_queries = (song_artist_table_drop, user_song_artist_table_drop, user_song_table_drop)