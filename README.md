# 🌡️ Smart Home Climate Monitoring System

Профессиональная система мониторинга микроклимата на базе ESP32 и Raspberry Pi.

## 🚀 Основные возможности
* **Persistence (БД):** Хранение истории измерений в SQLite (данные не пропадают после перезагрузки).
* **Dual-Line Analytics:** Интерактивный график (Chart.js) с двумя осями (температура и влажность).
* **Robustness:** Обработка ошибок связи и автоматическое восстановление сервера через `systemd`.
* **Real-time:** Частота опроса датчиков — каждые 5-7 секунд.

## 🛠️ Технологический стек
* **Контроллер:** ESP32 (C++, HTTP Client).
* **Сервер:** Raspberry Pi 4 (Python 3, Flask, SQLite3).
* **Интерфейс:** HTML5, CSS3 (Modern UI), JavaScript (Chart.js).
* **DevOps:** Git, Systemd Linux services.

## 📂 Структура
- `app.py` — серверная логика и API базы данных.
- `templates/index.html` — дашборд с аналитикой.
- `climate.db` — (локально) база данных измерений.
- `smart_home.service` — конфигурация автозапуска.
