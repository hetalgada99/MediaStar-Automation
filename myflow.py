from prefect import flow, task
import subprocess
import sys

@task
def run_em3():
    subprocess.run([sys.executable, "em3.py"], check=True)

@task
def run_em3_difference():
    subprocess.run([sys.executable, "em3_difference.py"], check=True)

@flow
def main():
    run_em3()
    run_em3_difference()

if __name__ == "__main__":
    main()
