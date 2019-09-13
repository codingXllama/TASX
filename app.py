from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# setting up the app
app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db '
# initializing the db for our app settings
db = SQLAlchemy(app)

# db model


class Todo(db.Model):
    # Creating columns with id
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # completed = db.Column(db.Integer, default=0)
    # setting the date time when a column is created
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Creating a function for returning an element that is newly created

    def __repr__(self):
        return'<Task %r> ' % self.id
# routing the app
@app.route('/', methods=['POST', 'GET'])
# defining the route method
def index():
    if request.method == 'POST':
        # Creating logic for adding tasks
        task_content = request.form['content']
        # Creating a new task(to do object) object using the Todo class
        # Setting the content of the Todo list, by assigning the content instance variable to the new_task content
        new_task = Todo(content=task_content)

        # pushing the task to the database ~ we must use try block
        try:
            db.session.add(new_task)
            # to execute the db
            db.session.commit()
            # redirecting back to the index page
            return redirect('/')

        except:
            return 'There was an issue adding the task, please try again!'

    else:
        # looking at all the tasks created and arranging them by the order created
        # use .first() to get first() created
        tasks = Todo.query.order_by(Todo.date_created).all()
        # rendering the html file
        return render_template('index.html', tasks=tasks)


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
