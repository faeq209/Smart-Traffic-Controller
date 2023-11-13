import paho.mqtt.client as mqtt

MQTT_ADDRESS = "192.168.0.181"
MQTT_USER = "prasanna"
MQTT_PASSWORD = "mansi"
MQTT_TOPIC_gps_lat_topic = "GPS_LATITUDE"
MQTT_TOPIC_gps_long_topic = "GPS_LONGITUDE"
MQTT_TOPIC_emergency_phone_topic = "EMERGENCY_PHONE_NUMBER"
MQTT_TOPIC_vehicle_number_topic = "VEHICLE_NUMBER"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_gps_lat_topic)
    client.subscribe(MQTT_TOPIC_gps_long_topic)
    client.subscribe(MQTT_TOPIC_emergency_phone_topic)
    client.subscribe(MQTT_TOPIC_vehicle_number_topic)

def on_message(client, userdata, msg):
    print(msg.topic + ":" + str(msg.payload))

def sub():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()

if _name_ == "_main_":
    print("MQTT to InfluxDB bridge")
    sub()