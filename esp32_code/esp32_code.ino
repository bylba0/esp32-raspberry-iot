#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "DHT.h"

// --- НАСТРОЙКИ СЕТИ ---
const char* ssid = "ASUS_FC";
const char* password = "customer_4593";

// --- НАСТРОЙКИ СЕРВЕРА ---
// Используем твой IP и порт 5000, где запущен Flask
const char* serverName = "http://192.168.50.131:5000/update";

// --- НАСТРОЙКИ ДАТЧИКА ---
#define DHTPIN 4      // Номер пина, куда подключен DATA-выход датчика
#define DHTTYPE DHT11 // Смени на DHT22, если у тебя белый датчик
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  
  // Подключение к Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi...");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi!");
}

void loop() {
  // Читаем реальные данные с датчика
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Проверка на корректность чтения
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return; 
  }

  // Если Wi-Fi на связи, отправляем данные
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    
    // Указываем адрес сервера
    http.begin(serverName);
    
    // Заголовок, что отправляем JSON
    http.addHeader("Content-Type", "application/json");

    // Формируем JSON пакет
    StaticJsonDocument<200> doc;
    doc["temperature"] = t;
    doc["humidity"] = h;

    String requestBody;
    serializeJson(doc, requestBody);

    // Отправляем данные методом POST
    Serial.print("Sending data: ");
    Serial.println(requestBody);
    
    int httpResponseCode = http.POST(requestBody);

    if(httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    
    http.end(); // Закрываем соединение
  } else {
    Serial.println("WiFi Disconnected. Reconnecting...");
    WiFi.begin(ssid, password);
  }

  // Отправка каждые 5 секунд (не части, чтобы не спамить сервер)
  delay(5000);
}
