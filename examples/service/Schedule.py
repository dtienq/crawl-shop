import schedule

def job():
    print('I am working')

schedule.every().hour.at(':00').do(job)

while 1:
    schedule.run_pending()