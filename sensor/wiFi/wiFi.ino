#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <String.h>


void setup() {
  Serial.begin(9600);
  WiFi.begin("Hai Nam T2","0915218277");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print("...");
    }
  Serial.print("OK");

}

void loop() { 
  if (Serial.available()>0){
    WiFiClient client;
    HTTPClient http;
    
    String url = Serial.readString();
    String url_get = url.substring(0, 52);
    Serial.println(url_get.c_str());

    
    http.begin(client, url_get);
    int httpResponseCode = http.GET();
    if (httpResponseCode>0){
      Serial.println(httpResponseCode);
      String data  = http.getString();
      Serial.println(data);
      }
    else{
      Serial.println("Error code: ");
      Serial.println(httpResponseCode);
      }
    http.end();
    }
 

}
