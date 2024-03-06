from flask import Flask

# __name__ is needed so that Flask knows where to look for resources such as template and static files
app = Flask(__name__)


# using route decorator to tell Flask what URL should trigger the function
@app.route("/")
def helloworld():
  return "<p>Hello Harry!</p>"


# to run the flask app in the local server
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
