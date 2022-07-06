from magniv.core import task
from datetime import datetime

@task(schedule="@hourly")
def hello_world():
	print(f"Hello world, the time is {datetime.now()}")

if __name__ == '__main__':
	hello_world()