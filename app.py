from flask import Flask, render_template, url_for

# setting up the app
app = Flask(__name__)

# routing the app
@app.route('/')
# defining the route method
def index():
    # rendering the html file
    return render_template('index.html')


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
