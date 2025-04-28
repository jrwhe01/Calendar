from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-task/<date>', methods=['GET', 'POST'])
def add_task_date(date):
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        # Save the task along with the 'date'
        return redirect(url_for('home'))
    return render_template('add_task.html', date=date)



if __name__ == '__main__':
    app.run(debug=True)
