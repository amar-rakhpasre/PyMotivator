'''
from apscheduler.schedulers.background import BackgroundScheduler
from PyMotivator import send_whatsapp_text, client, quote
import time

# Initialize the scheduler
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

# Schedule the job to run at 7:00 AM every day
job = scheduler.add_job(
    send_whatsapp_text,
    'cron',
    args=[client, quote],  # Passing the arguments correctly
    hour=7,  # Run at 7 AM
    minute=39  # Optional, ensures it runs at the start of the hour
)

# Print job details
print(job)

# Keep the program running
try:
    while True:
        time.sleep(1)  # Sleep to allow the scheduler to keep running
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
'''



from apscheduler.schedulers.background import BackgroundScheduler
from PyMotivator import send_whatsapp_text,client,quote
import time

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job = scheduler.add_job(send_whatsapp_text,'cron',[client,quote],hour="7",minute="45")
print(job)

while True:
	time.sleep(1)

