# from flask import Flask, render_template, request, session, redirect, url_for
# import mysql.connector

# # Veritabanı bağlantısı
# connection = mysql.connector.connect(host='localhost', port='3306', database='flaskData', user='root', password='CSGO123abcDf.')
# cursor = connection.cursor()
# app = Flask(__name__)
# app.secret_key = "secret_key"

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/home')
# def home():
#     if 'username' in session:
#         return render_template('home.html', username=session['username'])
#     else:
#         return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     msg = ''
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
#         record = cursor.fetchone()
#         if record:
#             session['loggedin'] = True
#             session['username'] = record[1]
#             return redirect(url_for('home'))
#         else:
#             msg = 'Incorrect username/password. Try Again!'
#     return render_template('index.html', msg=msg)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
#         connection.commit()
#         msg = 'You have successfully registered!'
#     return render_template('register.html', msg=msg)

# @app.route('/admin')
# def admin():
#     if 'username' in session:
#         cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
#         role = cursor.fetchone()[0]
#         if role == 'admin':
#             return render_template('admin.html')
#         else:
#             return redirect(url_for('home'))
#     else:
#         return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('username', None)
#     return redirect(url_for('index'))


# @app.route('/user-management')
# def user_management():
#     if 'username' in session:
#         cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
#         role = cursor.fetchone()[0]
#         if role == 'admin':
#             cursor.execute('SELECT id, username, email FROM users')
#             users = cursor.fetchall()
#             return render_template('user_management.html', users=users)
#         else:
#             return redirect(url_for('home'))
#     else:
#         return redirect(url_for('login'))
    
# @app.route('/add_user', methods=['POST'])
# def add_user():
#     if 'username' in session:
#         cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
#         role = cursor.fetchone()[0]
#         if role == 'admin':
#             username = request.form['username']
#             password = request.form['password']
#             email = request.form['email']
#             cursor.execute('INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)',
#                            (username, password, email, 'user'))
#             connection.commit()
#             return redirect(url_for('user_management'))
#         else:
#             return redirect(url_for('home'))
#     else:
#         return redirect(url_for('login'))

# @app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
# def edit_user(user_id):
#     if 'username' in session:
#         cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
#         role = cursor.fetchone()[0]
#         if role == 'admin':
#             if request.method == 'POST':
#                 username = request.form['username']
#                 email = request.form['email']
#                 cursor.execute('UPDATE users SET username=%s, email=%s WHERE id=%s', (username, email, user_id))
#                 connection.commit()
#                 return redirect(url_for('user_management'))
#             else:
#                 cursor.execute('SELECT username, email FROM users WHERE id=%s', (user_id,))
#                 user = cursor.fetchone()
#                 return render_template('edit_user.html', user=user, user_id=user_id)
#         else:
#             return redirect(url_for('home'))
#     else:
#         return redirect(url_for('login'))

# @app.route('/delete_user/<int:user_id>')
# def delete_user(user_id):
#     if 'username' in session:
#         cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
#         role = cursor.fetchone()[0]
#         if role == 'admin':
#             cursor.execute('DELETE FROM users WHERE id=%s', (user_id,))
#             connection.commit()
#             return redirect(url_for('user_management'))
#         else:
#             return redirect(url_for('home'))
#     else:
#         return redirect(url_for('login'))

# @app.route('/btn1')
# def btn1():
#     return "Button 1 Clicked"

# @app.route('/btn2')
# def btn2():
#     return "Button 2 Clicked"

# @app.route('/btn3')
# def btn3():
#     return "Button 3 Clicked"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, session, jsonify
import mysql.connector
from flask_cors import CORS

# Veritabanı bağlantısı
connection = mysql.connector.connect(host='localhost', port='3306', database='flaskData', user='root', password='CSGO123abcDf.')
cursor = connection.cursor()
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "secret_key"

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the API"})

@app.route('/home')
def home():
    if 'username' in session:
        return jsonify({'username': session['username']})
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
    record = cursor.fetchone()
    if record:
        session['loggedin'] = True
        session['username'] = record[1]
        return jsonify({'message': 'Logged in successfully'})
    else:
        return jsonify({'error': 'Incorrect username/password'}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
    connection.commit()
    return jsonify({'message': 'You have successfully registered'})

@app.route('/admin')
def admin():
    if 'username' in session:
        cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
        role = cursor.fetchone()[0]
        if role == 'admin':
            return jsonify({'message': 'Welcome Admin'})
        else:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully'})

@app.route('/user-management')
def user_management():
    if 'username' in session:
        cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
        role = cursor.fetchone()[0]
        if role == 'admin':
            cursor.execute('SELECT id, username, email FROM users')
            users = cursor.fetchall()
            return jsonify(users)
        else:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/add_user', methods=['POST'])
def add_user():
    if 'username' in session:
        cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
        role = cursor.fetchone()[0]
        if role == 'admin':
            data = request.json
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            cursor.execute('INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)',
                           (username, password, email, 'user'))
            connection.commit()
            return jsonify({'message': 'User added successfully'})
        else:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'username' in session:
        cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
        role = cursor.fetchone()[0]
        if role == 'admin':
            if request.method == 'POST':
                data = request.json
                username = data.get('username')
                email = data.get('email')
                cursor.execute('UPDATE users SET username=%s, email=%s WHERE id=%s', (username, email, user_id))
                connection.commit()
                return jsonify({'message': 'User updated successfully'})
            else:
                cursor.execute('SELECT username, email FROM users WHERE id=%s', (user_id,))
                user = cursor.fetchone()
                return jsonify({'user': {'username': user[0], 'email': user[1]}})
        else:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if 'username' in session:
        cursor.execute('SELECT role FROM users WHERE username=%s', (session['username'],))
        role = cursor.fetchone()[0]
        if role == 'admin':
            cursor.execute('DELETE FROM users WHERE id=%s', (user_id,))
            connection.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True)
