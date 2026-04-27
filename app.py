from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Храним последние 20 записей
history = []

@app.route('/')
def index():
    # Берем последнее значение для карточек
    current = history[-1] if history else {'temp': '--', 'hum': '--', 'time': '--'}
    return render_template('index.html', **current)

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    new_entry = {
        'temp': data.get('temperature'),
        'hum': data.get('humidity'),
        'time': datetime.now().strftime("%H:%M:%S")
    }
    history.append(new_entry)
    
    # Чтобы память не резиновая, оставляем только последние 20 точек
    if len(history) > 20:
        history.pop(0)
        
    return "OK", 200

# Добавляем маршрут, чтобы фронтенд мог забирать всю историю для графика
@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
