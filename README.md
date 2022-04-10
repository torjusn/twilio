# SMS SQL Anomaly Alert
![This is an image](https://www.twilio.com/assets/icons/twilio-icon-512_maskable.png)

## Description
The code of this repository connects to a SQL database, checks if a chosen column is over a specified threshold value, then send an sms alerts if the threshold has been exceeded. 

## Why?
External monitoring devices coupled to SQL databases could hit values that require human intervention or be of special interest at times without direct supervision. Delivering condensed, easily readable alerts about such anomalies in a short amount of time could therefore be of great value. Fields of application could be personal use or industrial.

## REQUIREMENTS
- A SQL database with values to threshold on

- python 3.9.7
- pandas 1.4.0

## USAGE
First install the necessary python libraries from the `.yaml file`. This can be done either manually or by creating a local environment with miniconda by running:
`$ conda env create -f environment.yml`  

(Step not needed without conda.) The environment can then be run as:
`conda create --name sms_alert`  

Customize the connect part of the `main.py` file to fit your local SQL database environment. An example setup for the user `postgres`, no password, running on localhost, and default port connecting to the `dvdrental` database is shown below:
```
user="postgres",
password="",
host="127.0.0.1",
port="5432",
database="dvdrental"
```

Run the main script with customized threshold values to check the sql database for

