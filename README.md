# Project: Data Pipelines with Airflow


## Introduction

This project uses a fictional company called Sparkify that is growing and requires expansion of their data systems to use a data warehouse in Amazon Redshift.

This project examines using data stored in an S3 bucket and uses Airflow to create a schedule to automate the ETL into a 
Redshift database.


## Prepatory steps

The following steps need to be complete before this project can be implemented:

1. We need to have an IAM User created in AWS
2. Create a redshift cluster in AWS and configure it to allow public access, enable enhanced VPC routing, and configure the incoming traffic rules to include a port range of 0-5500 with a source of Anywhere-iPv4.
3. Connect Airflow to AWS
4. Add Airflow connection to Redshift


## Datasets

The dataset for this project are:

- Log data: s3://udacity-dend/log_data
- Song data: s3://udacity-dend/song_data


## Configuring the DAG

The DAG (Directed Acyclic Graph) for this project is required to be configured with the following defaults:

- does not have dependencies on past runs
- on failure, tasks are retried 3 times
- retries occur every 5 minutes
- catch up is turned off
- do not email on retry

## Starting Airflow from the workspace

The project is run out of the Udacity airflow workspace. Once all your files are copied into the workspace you need to run the command '/opt/airflow/start.sh' to start the Airflow web server. Once this runs and you see the message 'Airflow webserver is ready' you can click the blue button 'Access Airflow' to open the web ui. 


## Helpful tips

### Use the forums
Be sure to read through the forums while doing this project. Many other students have experienced problems in the past and you'll get some great assistance just from reading through the forum posts

### Build a create tables task
The initial example DAG is almost all you'll need. I found it useful to create one extra task that was run directly after Begin_execution and before the staging events. I created a create_tables task that created all the tables I needed. This needed a bit of adjusting as I ran into an a few issues along the way. 

I created the tables using the CREATE TABLE IF NOT EXISTS commands, but I still ran into problems with the users table. Reading through the forums indicated that it could be solved by ensuring I included a DROP TABLE before I created it. I added the following line:

DROP TABLE public.users;

This solved the problem. See the create_tables.sql script in this repo for more detail.

### Simple typos can slow you down
The 'run_quality_checks' task included a list of tables to run checks on. I had neglected to make sure that the table names in this list matched the table names I had created in my create_tables script. For example, I had initially created a songs table, but in my list of quality checks I had specified the table name 'song' instead. 

Using the log output from Airflow can really help to point you towards the source of your error. 

### Use a .gitignore in your own repos
When you first create a repo for submission you are given a choice to create a readme file. You should always do this so you have something in your repo to begin with. After you clone your repo to your local computer the very first thing you should do is create a .gitignore file and add the name of any file that includes your credentials. This will ensure you don't accidentially commit any credentials to your public Github repos.
