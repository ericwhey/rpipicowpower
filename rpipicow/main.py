import time
import network
import urequests as requests
from machine import Pin
from umqtt.simple import MQTTClient

# Setup the onboard LED so we can turn it on/off
led = Pin("LED", Pin.OUT)

# Fill in your WiFi network name (ssid) and password here:
wifi_ssid = "WIFI_SSID"
wifi_password = "WIFI_PASSWORD"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
print("Connecting to WiFi")
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
mqtt_host = "127.0.0.1"
mqtt_username = ""  # Your Adafruit IO username
mqtt_password = ""  # Adafruit IO Key
mqtt_receive_topic = "rpipicowpower"  # The MQTT topic for your Adafruit IO Feed

# Enter a random ID for this MQTT Client
# It needs to be globally unique across all of Adafruit IO.
mqtt_client_id = "aksdjfkjkj2k3jk43k4jk3j4kj3j4k3j4"

# Initialize our MQTTClient and connect to the MQTT server
mqtt_client = MQTTClient(mqtt_client_id,mqtt_host)

ntfy_url = "https://ntfy.sh/rpipicowpower";

# So that we can respond to messages on an MQTT topic, we need a callback
# function that will handle the messages.
def mqtt_subscription_callback(topic, message):
    print (f'Topic {topic} received message {message}')  # Debug print out of what was received over MQTT
    if message == b'on':
        print("LED ON")
        led.value(1)
        post_data = "Server On Initiated"

        x = requests.post(ntfy_url, headers = {"Title": "RPi Pico W Power"}, data=post_data)
        if x.status_code == 200:
            print("Notified")
    elif message == b'off':
        print("LED OFF")
        led.value(0)
        post_data = "Server Off Initiated"

        x = requests.post(ntfy_url, headers = {"Title": "RPi Pico W Power"}, data=post_data)
        if x.status_code == 200:
            print("Notified")

# Before connecting, tell the MQTT client to use the callback
mqtt_client.set_callback(mqtt_subscription_callback)
print("Connecting to MQTT")
mqtt_client.connect()

# Once connected, subscribe to the MQTT topic
mqtt_client.subscribe(mqtt_receive_topic)
print("Connected and subscribed")

try:
    while True:
        # Infinitely wait for messages on the topic.
        # Note wait_msg() is a blocking call, if you're doing multiple things
        # on the Pico you may want to look at putting this on another thread.
        print(f'Waiting for messages on {mqtt_receive_topic}')
        mqtt_client.wait_msg()
except Exception as e:
    print(f'Failed to wait for MQTT messages: {e}')
finally:
    mqtt_client.disconnect()