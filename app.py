from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')  # <--- Tambahkan ini
def dashboard():
    return render_template('dashboard.html')  # <--- Pastikan sesuai dengan nama file di templates

if __name__ == '__main__':
    app.run()
