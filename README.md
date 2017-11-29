# End-to-End Twitter Stream Processing Application

Through the use of Apache Storm, Amazon EC2, Python, Twitter API, Streamparse, Postgres, PsycoPG, and Tweepy this application captures and stores all text contained in tweets while the listener is running. Two serving layer applications are available to analyze total traffic, data on specific words, or data on occurrence ranges.

## Setup 

Create an Amazon EC2 instance using the following public AMI:  
    o	AMI Name: UCB MIDS W205 EX2-FULL  
    o	AMI ID: ami-d4dd4ec3  
  
Create and mount an EBS volume as /data, as outlied by the page below:  
  o	https://github.com/UC-Berkeley-I-School/w205-fall-17-labs-exercises/blob/master/lab_2/Lab2.md  
  
Install PsycoPG:  
```
$ pip install psycopg2==2.6.2  
```
Install Tweepy:
```
$ pip install tweepy  
``` 
Switch to the w205 user:  
```
$ su - w205
```  
Clone this repository:  
```
$ git clone https://github.com/nvogler/w205f17_exercise2.git  
$ cd w205f17_exercise2
```
## Usage (screenshots available in /screencaps)  
Move into the extweetwordcount directory and run the listener:  
```
$ cd extweetwordcount  
$ sparse run
```
Wait a minute or two while tweets are captured before stopping the listener:  
  o Press  Ctrl + C   

Move back to the main directory and try out the analysis applications:  
```
$ cd ..  
$ python finalresults.py  
$ python finalresults.py trump  
$ python histrogram.py 5,10  
```
TODO
Screenshots demonstrating end-to-end execution of the application are available in the screenshots directory.

TODO - Plot.png: a bar chart, generated however you prefer, that shows the top 20 words in your Twitter stream.
