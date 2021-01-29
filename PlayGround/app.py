from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')  # this created a second instance/route
def dojo_world():
    return 'Dojo'


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/say/<name>')
def hello(name):
    print(name)
    return " hello " + name

    # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'


@app.route('/repeat/<num>/<name>')
def rep(name, num):
    num = int(num)
    return f'hello {name} !!!!!!!!!!'*num


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
