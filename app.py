from flask import Flask

app = Flask(__name__)



@app.route('/<place>')
def place():
    return "favorite place is ooty"


if __name__ == '__main__':
    app.run(debug=True)

