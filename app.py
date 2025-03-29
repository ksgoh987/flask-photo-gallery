from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to something more secure in production
app.permanent_session_lifetime = 60  # Auto-logout after 60 seconds of inactivity

# Define allowed users
users = ['admin1', 'admin2']
default_password = 'cby4931'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and password == default_password:
            session.permanent = True
            session['user'] = username
            return redirect(url_for('gallery'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def gallery():
    if 'user' not in session:
        return redirect(url_for('login'))

    username = session['user']
    photo_folder = os.path.join('static', 'uploads', username)
    if not os.path.exists(photo_folder):
        os.makedirs(photo_folder)

    photos = [
        file for file in os.listdir(photo_folder)
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]
    return render_template('gallery.html', photos=photos, user=username)

if __name__ == '__main__':
    app.run(debug=True)
