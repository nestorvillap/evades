from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

@app.route("/")
def index():
	return render_template("home.html")

@app.route("/online")
def online():

	return render_template("online.html")

@app.route("/ss")
def game():

	return render_template("ss.html")

@app.route("/how-to-play")
def how():

	return render_template("how.html")

if __name__ == "__main__":
	app.run(debug=True)