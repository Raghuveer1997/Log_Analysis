# Logs Analysis Udacity Project
### Raghuveer Pachipulusu

![Part of the Udacity Full-Stack Web Development Nanodegree]

## What it is Log Analysis ?

It is a Reporting page.
It prints out reports in text format based on the data in the database.`psycopg2` Module a python program is used to Connect With Database.

## Contents Of The Project 

Log Analysis Project consists of following files:

* Udacity_Log_Analysis.py - main python file to run this Logs Analysis Reporting tool
* sqlviews.sql - views file
* README.md - Steps To Follow For installing this reporting tool
* OutPut.PNG

## Tools Required For This Project 

1. Vagrant
2. VirtualBox
3. Python -Download latest version of python
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Python](https://www.python.org/)

## Steps to Install
1. Install Vagrant into your computer
2. install VirtualBox into your computer


## Steps For Runing The Project

Download the project zip file. Then unzip the file And  place It inside `vagrant/Udacity_Log_Analysis-Master`.

Firstly Open command prompt in Project folder and Initilize the Ubuntu version using vagrant to generate Vagrant file
 `vagrant init ubuntu/xenial64`


Later We Need To Launch the Vagrant VM using command:
  `vagrant up`
Then Log into this using command:
  `vagrant ssh`
  
 Change directory to `cd /vagrant` 
	or
   run these commands for exiting two directories
   i)cd ..
   ii)cd ..
   iii)cd/vagrant
 
Download database newsdata.sql from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Extract or Unzip the file newsdata.sql 

Copy the newsdata.sql file and place the file inside `vagrant/Udacity_Log_Analysis-Master
`.
In CommandPrompt Change directory to `vagrant/Udacity_Log_Analysis-Master` and look around with ls.

connect to postgres database using command
`sudo su - postgres`
`psql`

For creating user vagrant use command:
`create user vagrant with superuser createrole createdb replication bypassrls;`

For creating database news use command:
`create database news with owner vagrant;`

To change database to news:
`\c news`
	-use \c to connect to database="news"
	-use \dt to see the tables in database
	-use \dv to see the views in database

Run the two `CREATE VIEW` statements in the [Database Views](#database-views) section.
	
	-use \q to quit the database

To Logout from current user we use command:
`logout`
When we get back to the directory  
`vagrant/Udacity_Log_Analysis-Master`  
Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
 
Run Udacity_Log_Analysis.py main python file using:
  ```
    $ python Udacity_Log_Analysis.py
  ```
    
## Database Views

For running the log analysis code, you need to create views in the database. So go to the psql and run the following code.

* **popular_views**:
	```
	create or replace view popular_views as select
	articles.title, articles.id, articles.author,
	(select count(log.path)
	from log
	where log.path = concat('/article/',articles.slug)) as topviews
	from articles
	order by topviews desc;
	```
* **overall_req**:
	```
	create or replace view overall_req as
	select count(status) as count,
       date(time) as date
	   from log
	group by date
	order by count desc;
	
	```
* **fault_req**:
	```
	create or replace view fault_req as
	select count(*) as count,
       date(time) as date
	from log
	where log.status::text != '200 OK'
	group by date
	order by count desc;

	```

* **fault_perc**:

	```	
	create or replace view fault_perc as
	select overall_req.date,
       round((100.0*fault_req.count)/overall_req.count,1) as fault_prc
	from fault_req,
     overall_req
	where fault_req.date=overall_req.date;
	
	```
### Useful links
- PEP8 tool to check Python styles (http://pep8online.com/)
