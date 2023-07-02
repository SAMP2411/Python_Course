import smtplib, random
import datetime as dt

my_email = "nishipatel1802@gmail.com"
my_password = "gekcciipmpsdyocm"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if day_of_week == 2:
    # date_of_birth = dt.datetime(year=2001, month=11, day=15, hour=23)
    # print(date_of_birth)

    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()

    quote_to_send = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="diyaparmar1602@gmail.com",
            msg=f"Subject:HELLO\n\n{quote_to_send}",
        )
