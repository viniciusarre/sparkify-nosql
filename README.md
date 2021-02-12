# Sparkify Data Modelling on a nosql

# About the Project

This project is a Proof of Concept of a nosql data modelling process built using Apache Cassandra. This includes reading song data from a CSV file and model them into different tables, according to what needs to be queried.

# The Structure 

The data is structured on the `/event_data` folder. `etl.py` handles the ETL pipeline and populates the tables, as well as creating the tables and populating them. Furthermore, the test notebook can be used to run the needed queries.

Here's an exemplification of the CSV data structure:

![ Data structure of the CSV file](./images/image_event_datafile_new.jpg " Data structure of the CSV file")

# Using the code

In order to use the solution, make sure you have installed the latest version of Apache Cassandra and Python as well as the pythonic `cassandra` driver.

For testing purposes, it is a good idea to set up an instance of a Jupiter Notebook server so you can use the notebooks presented in the code. The scripts can be run without any of the Notebooks, however, using them is a good and simpler way for testing the data line-by-line. 

Before running the ETL process, you need to write the `event_datafile_new` file which will contain the csv data to be inserted to the Cassandra Tables, which need to be extracted from the `/event_data` folder. The logic for this was set on `process_files.py`

In the current structure, you can create and change the ETL process using a [notebook](etl.ipynb) , this is easier for testing and setting up the pipeline steps individually or modify them. Once that's done, you can update the [etl script](etl.py) so that it fetches and sets up all the data.

The other Python scripts are structured in a way that makes handling the database operations easier. `cql_queries.py`, for instances has the string for creating, dropping and inserting into the tables. It was built as a module to be used by both `etl.py` and `create_tables.py`.

The `create_table.py` script can be used for the tables to be dropped and recreated, which is a good manner to reset the data for testing and fixing bugs, while being used alongside `etl.py` or `etl.ipynb`. 

# Running the scripts

After installing the dependencies, you can create the tables by running the following: 

```python create_tables.py``` 


Once that is done, you can extract the data from `event_data` into the `event_datafile_new.csv` file, which can be done by running:

```python process_files.py```


Then you can run the ETL code by running:

```python etl.py```


# Testing the data

There's also a [test notebook](test.ipynb) in place for verifying that the data was properly validate the ETL pipeline.


This project is my solution to an assessment in Udacity's [Data Engineering Nano Degree](https://www.udacity.com/course/data-engineer-nanodegree--nd027)
