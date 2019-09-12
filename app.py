from flask import Flask

# setting up the app
app = Flask(__name__)

# routing the app
@app.route('/')
# defining the route method
def index():
    return "Hello there!"


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
