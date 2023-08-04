# Don't You Forget About Me

## About The Project

**This project was made originally 16 Aug. 2020**

The purpose behind this one is pretty funny actually. When planning to do something with my in-laws, my mother-in-law "forgot I was a person", so I made this to run once a day and send a picture of me to her such that her memory would be jogged. That was 100% not intentional on her part, and my mother-in-law is about the sweetest and nicest person I have ever met.  We get a chuckle out of it. This was one of those silly programs you can just do whatever you want with, and I thought it was a good story behind it too.

---

### Some Notes

I did sanitize the email and password information, and there would not be a history behind the repo for that reason as well. 

Because this project was just for me I did not do any extensive amount of defensive coding to prevent the end user from providing bad data. Since the target user was me! Nor did I really add a whole lot of flow control. Ideally, if there were any major issues at runtime, such as when checking for the directory existence or failure to login, if that was not found, it would stop the execution then and there and report that back to the user and go again after appropriate action had been taken. 

This app will get, from a directory, a random image, attach it to an email, and send the email to a pre-configured recipient.

### Built With

Python! Because I wanted to learn some more about the language. I have enjoyed it so far. 

## Getting Started

### External Libraries
I honestly do not recall what I needed to install, however, I just wanted to note what is used. 

Here are the packages that are used by the application

* os
* smtplib
* random
* from email import encoders
* from email.mime.base import MIMEBase
* from email.mime.multipart import MIMEMultipart
* from email.mime.text import MIMEText

### Installation 
Because there are not any external resources one may simply clone the repo. 

`git clone https://github.com/sempercuriosus/dont_you_forget_about_me.git`

### Usage

#### Set Up
Because this was sanitized previously there are a few set up items needed: 
  1. `_image_location` - I used a directory with several images in them to randomly select one
  2. `_to_email` - we need a recipient
  3. `_bcc` - another one, perhaps? This was to send to myself during testing
  4. `_from_email` - where is this being sent from?
  5. `_password` = '' - I used an App Specific Password for this because I have 2FA on my account
  6. `_subject` - pick a title!
  7. `_message_body` - I added a note in my messages

#### Running
This is not the most user friendly approach here, but again it was just a fun and get it done quick project. That said, when the python3 file is configured this will run as any other command line item with python by calling it. The command below is assuming you opened the terminal window in parent directory, otherwise the full file path will be needed.

`python3 dont_you_forget.py`

### Final Note
If I were to revisit this, say she forgets about me again, I would like to add some of that defensive coding and better flow control to make this more of a "complete" application to get some practice in that. 

Take Care!
-EH
