from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# setting up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db '
# initializing the db for our app settings
db = SQLAlchemy(app)

# db model


class Todo(db.Model):
    # Creating columns with id
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    # setting the date time when a column is created
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Creating a function for returning an element that is newly created

    def __repr__(self):
        return'<Task %r> ' % self.id
# routing the app
@app.route('/')
# defining the route method
def index():
    # rendering the html file
    return render_template('index.html')


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
