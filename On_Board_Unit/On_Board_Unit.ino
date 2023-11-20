
#include <PubSubClient.h>
#include <WiFi.h>

// WiFi
const char* ssid = "bit.ly/3Y2vzes";                
const char* wifi_password = "!@#$%^&*()";

// MQTT
const char* mqtt_server = "192.168.0.111"; 
const char* gps_lat_topic = "GPS_LATITUDE";
const char* gps_long_topic = "GPS_LONGITUDE";
const char* emergency_phone_topic = "EMERGENCY_PHONE_NUMBER";
const char* vehicle_number_topic = "VEHICLE_NUMBER";
//const char* temperature_topic = "temperature";
const char* mqtt_username = "prasanna"; // MQTT username
const char* mqtt_password = "mansi"; // MQTT password
const char* clientID = "Weather_Reporter"; // MQTT client ID

// Initialise the WiFi and MQTT Client objects
WiFiClient wifiClient;

// 1883 is the listener port for the Broker
PubSubClient client(mqtt_server, 1883, wifiClient);

 

// Custom function to connect to the MQTT broker via WiFi
void connect_MQTT(){
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Connect to the WiFi
  WiFi.begin(ssid, wifi_password);

  // Wait until the connection is confirmed
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Debugging – Output the IP Address of the ESP8266
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Connect to MQTT Broker
  if (client.connect(clientID, mqtt_username, mqtt_password)) {
    Serial.println("Connected to MQTT Broker!");
  }
  else {
    Serial.println("Connection to MQTT Broker failed…");
  }
}

void setup() {
  Serial.begin(9600);
  
}

void loop() {
  connect_MQTT();
  Serial.setTimeout(2000);
  String lati="22.250971";
  String longi="84.902028";
  String em_phno="7894433665";
  String v_no="OD-14Y-0001";
  
  float h = 5;
  float t = 10;

  Serial.print("Latitude: ");
  Serial.println(lati);
  
  Serial.print("Longitude: ");
  Serial.println(longi);
  

  // MQTT can only transmit strings
  //String hs="Hum: "+String((float)h)+" % ";
  //String ts="Temp: "+String((float)t)+" C ";

  // PUBLISH to the MQTT Broker (topic = Latitude)
  if (client.publish(gps_lat_topic, lati.c_str())) {
    Serial.println("Latitude sent!");
  }
  else {
    Serial.println("Latitude failed to sen Reconnecting to MQTT Broker ad trying again");
    client.connect(clientID, mqtt_username, mqtt_password);
    delay(10); // This delay ensures that client.publish doesn’t clash with the client.connect call
    client.publish(gps_lat_topic, lati.c_str());
  }

  // PUBLISH to the MQTT Broker (topic = Longitude)
  if (client.publish(gps_long_topic, longi.c_str())) {
    Serial.println("Longitude sent!");
  }
  else {
    Serial.println("Longitude failed to sen Reconnecting to MQTT Broker ad trying again");
    client.connect(clientID, mqtt_username, mqtt_password);
    delay(10); // This delay ensures that client.publish doesn’t clash with the client.connect call
    client.publish(gps_long_topic, longi.c_str());
  }
  
  // PUBLISH to the MQTT Broker (topic = Emergency Phone Number)
  if (client.publish(emergency_phone_topic, em_phno.c_str())) {
    Serial.println("Emergency Phone Number sent!");
  }
  else {
    Serial.println("Emergency Phone Number failed to sen Reconnecting to MQTT Broker ad trying again");
    client.connect(clientID, mqtt_username, mqtt_password);
    delay(10); // This delay ensures that client.publish doesn’t clash with the client.connect call
    client.publish(emergency_phone_topic, em_phno.c_str());
  }
    // PUBLISH to the MQTT Broker (topic = Vehicle Number)
  if (client.publish(vehicle_number_topic, v_no.c_str())) {
    Serial.println("Emergency Phone Number sent!");
  }
  else {
    Serial.println("Emergency Phone Number failed to sen Reconnecting to MQTT Broker ad trying again");
    client.connect(clientID, mqtt_username, mqtt_password);
    delay(10); // This delay ensures that client.publish doesn’t clash with the client.connect call
    client.publish(vehicle_number_topic, v_no.c_str());
  }
  
  client.disconnect();  // disconnect from the MQTT broker
  delay(1000*60);       // print new values after 1 Minute
}
