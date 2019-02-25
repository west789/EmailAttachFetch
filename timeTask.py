import schedule
import time
from emailAttDown import emailFetchMain
from datetime import datetime

def job():
    print("I'm working...")
    emailFetchMain()

if __name__ == '__main__':
    if datetime.today().weekday()+1 in (2, 3):
        job()
    # schedule.every(30).seconds.do(job)
    schedule.every().monday.at("21:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
