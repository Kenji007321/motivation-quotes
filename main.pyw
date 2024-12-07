import smtplib
import datetime as dt
import random

my_email = "myemail@gmail.com"
password = "mypassword"
file_quotes = "./quotes.txt"
file_used_quotes = "./used_quotes.txt"

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
    with open(file_quotes, "r") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

        unused_quotes = [i for i in all_quotes if i != random_quote]
    
    with open(file_quotes, "w") as quote_file:
        quote_file.writelines(unused_quotes)
        
    with open(file_used_quotes, "a") as used_quote_file:
        used_quote_file.writelines(random_quote)
        
    with open(file_used_quotes, "r") as quote_file:
        used_quotes = quote_file.readlines()
        
    sendemail(random_quote)
    print(f"Number of quotes unused: {len(unused_quotes)}")
    print(f"Number of quotes used: {len(used_quotes)}")
    
    if len(unused_quotes) == 0:
        with open(file_quotes, "w") as quote_file:
            quote_file.writelines(used_quotes)
        
        with open(file_quotes, "r") as quote_file:
            reset_quotes = quote_file.readlines()
        
        print(f"\nNumber of quotes unused(reset): {len(reset_quotes)}")
