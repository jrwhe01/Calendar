from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
# app.secret_key = 'secret_key' 

client = MongoClient("mongodb://localhost:27017/")
db = client["calendar"]
tasks_collection = db["tasks"]

@app.route('/')
def index():
    return render_template('index.html')

tasks_by_date = {}

@app.route('/add-task/<date>', methods=['GET', 'POST'])
def add_task_date(date):
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
            tasks_collection.insert_one(task_data)

    # flash("Task added successfully!")

    return render_template('add_task.html', date=date)

if __name__ == '__main__':
    app.run(debug=True)
