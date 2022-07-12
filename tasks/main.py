from magniv.core import task
from datetime import datetime

@task(schedule="@hourly")
def hello_world():
	print("Hello world, the time is {}".format(datetime.now()))

if __name__ == '__main__':
	hello_world()
