from flask import Flask, render_template,request_finished
from flask.wrappers import Response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>/')
def num(num):
    return Response("<int:num>")


    

if __name__ == "__main__":
    app.run(debug=True)
