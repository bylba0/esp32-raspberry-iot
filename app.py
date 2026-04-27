import sqlite3
from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('climate.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS measurements 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  temp REAL, hum REAL, time TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    temp = data.get('temperature')
    hum = data.get('humidity')
    time_now = datetime.now().strftime("%H:%M:%S")

    # Сохраняем в базу
    conn = sqlite3.connect('climate.db')
    c = conn.cursor()
    c.execute("INSERT INTO measurements (temp, hum, time) VALUES (?, ?, ?)", (temp, hum, time_now))
    conn.commit()
    conn.close()
    
    print(f"Записано в БД: {temp}C, {hum}%")
    return "OK", 200

@app.route('/history')
def get_history():
    conn = sqlite3.connect('climate.db')
    c = conn.cursor()
    # Берем последние 30 записей
    c.execute("SELECT temp, hum, time FROM measurements ORDER BY id DESC LIMIT 30")
    rows = c.fetchall()
    conn.close()
    
    # Переворачиваем, чтобы график шел слева направо
    history = [{"temp": r[0], "hum": r[1], "time": r[2]} for r in rows][::-1]
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
