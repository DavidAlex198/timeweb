from flask import Flask
import datetime

# print(time.strftime("%b %d, %Y, %H:%M"))


app = Flask(__name__)

@app.route('/')
def show_time():
	time = datetime.datetime.now()
	return time.strftime("%b %d, %Y, %H:%M")


if __name__ == "__main__":
	app.run(host="10.92.21.104", port=8008)
