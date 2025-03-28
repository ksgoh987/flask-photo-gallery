from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def gallery():
    photo_folder = os.path.join('static', 'uploads')
    photos = [file for file in os.listdir(photo_folder) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return render_template('gallery.html', photos=photos)
if __name__ == '__main__':
    app.run(debug=True)
