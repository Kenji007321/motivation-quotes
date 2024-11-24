import smtplib
import datetime as dt
import random

my_email = "myemail@gmail.com"
password = "mypassword"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday() + 1

def sendemail(quote):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="emailtosend@gmail.com", 
                            msg=f"Subject:Quote of the Day ({year}/{month}/{day})\n\n{quote}."
                        )


if day_of_week == 1:
    with open("./quotes.txt") as quote_file:
        random_quote = random.choice(quote_file.readlines())
        
    sendemail(random_quote)
