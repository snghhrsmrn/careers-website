from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Noida, India',
    'salary': 'Rs. 16,00,000'
}, {
    'id': 3,
    'title': 'Frontend Dev',
    'location': 'San Francisco, USA',
    'salary': '$180,000'
}, {
    'id': 4,
    'title': 'Backend Dev',
    'location': 'Amsterdam, Netherlands',
    'salary': '€150,000'
}]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
