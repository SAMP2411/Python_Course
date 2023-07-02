import smtplib, random, pandas
import datetime as dt

my_email = "nishipatel1802@gmail.com"
my_password = "gekcciipmpsdyocm"

birthday_details = pandas.read_csv("birthday.csv")
now = dt.datetime.now()
today_date = dt.datetime(day=now.day, month=now.month, year=now.year)
person_list = []

for _ in range(len(birthday_details)):
    birthmonth = birthday_details.month[_]
    birthdate = birthday_details.day[_]
    birthday_date = dt.datetime(day=birthdate, month=birthmonth, year=now.year)
    if birthday_date == today_date:
        with open("letter.txt") as letter_file:
            letter_content_list = letter_file.readlines()
            first_line = letter_content_list[0].replace(
                "[NAME]", birthday_details.name[_]
            )
            letter_content_list[0] = first_line

        new_letter = "".join(letter_content_list)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_details.email[_],
                msg=f"Subject:Birthday Wish\n\n{new_letter}",
            )
