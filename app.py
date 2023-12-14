import sqlite3

from bottle import Bottle, run, template, request, redirect

app = Bottle()

# SQLite database configuration
DATABASE = 'gym.db'

# Helper function to connect to the database
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

# Initialize the database
def init_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gym_trainer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_workout (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            hours INTEGER NOT NULL,
            bottle_module TEXT,
            FOREIGN KEY (customer_id) REFERENCES gym_trainer (id)
        )
    ''')

    db.commit()

# CRUD operations for gym trainers
@app.route('/trainers')
def trainers():
    db = get_db()
    trainers = db.execute('SELECT * FROM gym_trainer').fetchall()
    return template('trainers', trainers=trainers)

@app.route('/create_trainer', method='GET')
def create_trainer_form():
    return template('create_trainer')

@app.route('/add_trainer', method='POST')
def add_trainer():
    db = get_db()
    name = request.forms.get('name')
    db.execute('INSERT INTO gym_trainer (name) VALUES (?)', (name,))
    db.commit()
    return redirect('/trainers')

@app.route('/edit_trainer/<trainer_id>', method='GET')
def edit_trainer_form(trainer_id):
    db = get_db()
    trainer = db.execute('SELECT * FROM gym_trainer WHERE id = ?', (trainer_id,)).fetchone()
    return template('edit_trainer', trainer=trainer)

@app.route('/update_trainer/<trainer_id>', method='POST')
def update_trainer(trainer_id):
    db = get_db()
    name = request.forms.get('name')
    db.execute('UPDATE gym_trainer SET name = ? WHERE id = ?', (name, trainer_id))
    db.commit()
    return redirect('/trainers')

@app.route('/delete_trainer/<trainer_id>', method='POST')
def delete_trainer(trainer_id):
    db = get_db()
    db.execute('DELETE FROM gym_trainer WHERE id = ?', (trainer_id,))
    db.commit()
    return redirect('/trainers')

# CRUD operations for customer workout hours
@app.route('/workouts')
def workouts():
    db = get_db()
    workouts = db.execute('SELECT * FROM customer_workout').fetchall()
    return template('workouts', workouts=workouts)

@app.route('/create_workout', method='GET')
def create_workout_form():
    db = get_db()
    trainers = db.execute('SELECT * FROM gym_trainer').fetchall()
    return template('create_workout', trainers=trainers)

@app.route('/add_workout', method='POST')
def add_workout():
    db = get_db()
    customer_id = request.forms.get('customer_id')
    hours = request.forms.get('hours')
    bottle_module = request.forms.get('bottle_module')
    db.execute('INSERT INTO customer_workout (customer_id, hours, bottle_module) VALUES (?, ?, ?)', (customer_id, hours, bottle_module))
    db.commit()
    return redirect('/workouts')

@app.route('/edit_workout/<workout_id>', method='GET')
def edit_workout_form(workout_id):
    db = get_db()
    workout = db.execute('SELECT * FROM customer_workout WHERE id = ?', (workout_id,)).fetchone()
    trainers = db.execute('SELECT * FROM gym_trainer').fetchall()
    return template('edit_workout', workout=workout, trainers=trainers)

@app.route('/update_workout/<workout_id>', method='POST')
def update_workout(workout_id):
    db = get_db()
    customer_id = request.forms.get('customer_id')
    hours = request.forms.get('hours')
    bottle_module = request.forms.get('bottle_module')
    db.execute('UPDATE customer_workout SET customer_id = ?, hours = ?, bottle_module = ? WHERE id = ?', (customer_id, hours, bottle_module, workout_id))
    db.commit()
    return redirect('/workouts')

@app.route('/delete_workout/<workout_id>', method='POST')
def delete_workout(workout_id):
    db = get_db()
    db.execute('DELETE FROM customer_workout WHERE id = ?', (workout_id,))
    db.commit()
    return redirect('/workouts')

if __name__ == '__main__':
    init_db()
    run(app, debug=True)
