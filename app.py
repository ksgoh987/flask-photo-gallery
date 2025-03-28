from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace this with your actual authentication logic
        if username == 'admin' and password == 'cby4931':
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

    photo_folder = os.path.join('static', 'uploads')
    photos = [
        file for file in os.listdir(photo_folder)
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]
    return render_template('gallery.html', photos=photos)


if __name__ == '__main__':
    app.run(debug=True)
