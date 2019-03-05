# Project 3: Logs Analysis Project
### by Raghuveer Pachipulusu

Logs Analysis Project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does

A Reporting page that prints out reports in a plain text format based on the data in the database.This Reporting tool is a python program using the `psycopg2` module to connect to the database.

## Project content

This Project consists for the following files are:

* Udacity_Log_Analysis.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* views.sql - views file
* OutPut.PNG

## Required Tools

1. Python
2. Vagrant
3. VirtualBox

## Installation

There are some dependancies and a few instructions on how to run the application.

## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd /vagrant` as instructed in terminal

## How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/MyLog_Analysis-Master`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/MyLog_Analysis-Master
`.

  6. In terminal Change directory to `vagrant/MyLog_Analysis-Master` and look around with ls.

  7. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
  8.Load the views(Virtual Table) in local database using command:
  
  ```
	$ psql -d news -f views.sql
  ```
  
   9. Run Udacity_Log_Analysis.py using:
  ```
    $ python Udacity_Log_Analysis.py
  ```
  Note: Queries will take sometime to execute 


## Miscellaneous

This README document is based on a template suggested by PhilipCoach in this
Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).
