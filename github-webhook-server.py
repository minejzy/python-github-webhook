from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello you doing,james!"

@webhook.hook()        # Defines a handler for the 'git push' event
def on_push(data):
    print("Got push with: {0} by james under v1".format(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8051)
