from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

# setting up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db '
# initializing the db for our app settings
db = SQLAlchemy(app)

# routing the app
@app.route('/')
# defining the route method
def index():
    # rendering the html file
    return render_template('index.html')


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
