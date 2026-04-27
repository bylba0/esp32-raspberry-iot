# 🌡️ IoT Climate Control System

Система мониторинга климата в реальном времени. Данные собираются датчиком через ESP32 и визуализируются на веб-панели Raspberry Pi.

## 🚀 Технологический стек
* **Hardware:** ESP32 (Client), DHT22 Sensor, Raspberry Pi 4 (Server).
* **Backend:** Python 3 + Flask.
* **Frontend:** HTML5, CSS3, JS + **Chart.js** (визуализация графиков).
* **DevOps:** Управление процессами через `systemd`, контроль версий `Git`.

## 🛠️ Функционал
- **Real-time Monitoring:** Обновление данных каждые 5-7 секунд.
- **Data Visualization:** Интерактивный график температуры с историей последних 20 измерений.
- **Autostart:** Сервер автоматически поднимается при загрузке Raspberry Pi.

## 📂 Структура проекта
- `app.py` — Flask-сервер, обрабатывающий JSON-пакеты.
- `templates/index.html` — Веб-интерфейс с графиками.
- `smart_home.service` — Конфигурация для системного демона Linux.
