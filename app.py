from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient("mongodb://localhost:27017/")
db = client["calendar"]

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip().lower()
        if username:
            session['username'] = username
            return redirect(url_for('calendar'))
    return render_template('login.html')

@app.route('/calendar')
def calendar():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('calendar.html', username=session['username'])

@app.route('/tasks_for_date/<date>')
def show_tasks(date):
    if 'username' not in session:
        return redirect(url_for('login'))

    task_collection = db[f"tasks_{session['username']}"]
    tasks = list(task_collection.find({'date': date}).sort("start_time", ASCENDING))
    return render_template('tasks_for_date.html', date=date, tasks=tasks)

@app.route('/add-task/<date>', methods=['GET', 'POST'])
def add_task_date(date):
    if 'username' not in session:
        return redirect(url_for('login'))

    task_collection = db[f"tasks_{session['username']}"]

    if request.method == 'POST':
        task_name = request.form.get('taskname') 
        description = request.form.get('description')
        st_hour = request.form.get('stHours')
        st_min = request.form.get('stMinutes')
        et_hour = request.form.get('etHours')
        et_min = request.form.get('etMinutes')

        if task_name:
            task_data = {
                "taskname": task_name,
                "description": description,
                "start_time": f"{st_hour}:{st_min}",
                "end_time": f"{et_hour}:{et_min}",
                "date": date,
            }
            task_collection.insert_one(task_data)
            return redirect(url_for('show_tasks', date=date))

    return render_template('add_task.html', date=date)

@app.route('/delete-task/<task_id>', methods=['POST'])
def delete_task(task_id):
    task_collection = db[f"tasks_{session['username']}"]
    task = task_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        task_collection.delete_one({"_id": ObjectId(task_id)})
        return redirect(url_for('show_tasks', date=task["date"]))
    return "Task not found", 404

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
