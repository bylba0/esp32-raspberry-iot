from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    temp = data.get('temperature')
    hum = data.get('humidity')
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"{time_str}, Temp: {temp}, Hum: {hum}\n"
    
    # Печатаем в консоль
    print(f"[{time_str}] Сохранено: T={temp}C, H={hum}%")
    
    # Записываем в файл
    with open("data_log.txt", "a") as f:
        f.write(log_entry)
    
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
