import requests, smtplib, time
import datetime as dt

my_email = "nishipatel1802@gmail.com"
my_password = "gekcciipmpsdyocm"

MY_LAT = 20.593683
MY_LONG = 78.962883


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="diyaparmar1602@gmail.com",
            msg=f"Subject:Look Up\n\nThe ISS is above you.",
        )


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    long = float(response.json()["iss_position"]["longitude"])
    lat = float(response.json()["iss_position"]["latitude"])

    if MY_LAT - 5 <= lat <= MY_LAT + 5 and MY_LONG - 5 <= long <= MY_LONG + 5:
        return True


def is_night():
    if current_hour >= sunset or current_hour <= sunrise:
        return True


parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now()
current_hour = time_now.hour

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        send_mail()
