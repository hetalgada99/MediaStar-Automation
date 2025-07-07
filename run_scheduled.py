import schedule
import time
import subprocess
import sys

def run_my_flow():
    subprocess.run([sys.executable, "myflow.py"], check=True)

# Run at 7:30 AM every day
schedule.every().day.at("07:30").do(run_my_flow)

print("Scheduler started. Waiting to trigger the flow...")

while True:
    schedule.run_pending()
    time.sleep(60)
