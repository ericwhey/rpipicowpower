# Overview

A quick little project to simulate pressing the power button on a PC using a GPIO pin on a Raspberry Pi Pico W.

To turn on the PC the GPIO needs to simulate pressing the button for 1 second.  If the PC is on already it may also trigger a soft power down.

To turn off the PC the GPIO needs to simulate pressing the button for 5 seconds.

The initial design of the circuit to simulate pressing the button includes a transistor that the GPIO pin controls the gate.  More details to follow including a circuit diagram and image.

# Requirements

Mosquitto (MQTT) Broker installed on local network listening on an open network port.  I use a docker image eclipse-mosquitto with port 1883 open.

Raspberry Pico W

# Instructions

Customize main.py in the rpipicow folder for your settings, particularly the SSID and password for WiFi, the IP of the MQTT broker, the topic to listen to on MQTT, and the URL of a ntfy.sh server to send notifications to.

Use Thonny or similar tool to install MicroPython to the Raspbery Pico W.

Drag the main.py to the Raspberry Pico W drive or use Thonny to save the main.py to the Raspberry Pico W.

Disconnect the Raspberry Pico W and connect the circuit to the GPIO.

Configure the .env file or create an .env.override file in the app folder according to your system, specifically the MQTT_HOST and MQTT_TOPIC.

Start up the nginx and node servers on docker with the following commands:

cd docker
docker-compose up

Access the HTML page with the switch at the following URL:

http://127.0.0.1:8088

Press the buttons on the page to turn on or off the PC.




