from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-task/<date>')
def add_task(date):
    return render_template('add_date.html', date=date)



if __name__ == '__main__':
    app.run(debug=True)
