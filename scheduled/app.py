from chalice import Chalice

app = Chalice(app_name='scheduled')


@app.schedule("cron(25 21 ? * * *)")
def scheduled(event):
    print("I'm running every day at 9:30pm")
    return True