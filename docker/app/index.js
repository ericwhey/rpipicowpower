// index.js
const mqtt = require("mqtt");
const express = require('express');
const app = express();

const mqtt_host = process.env.MQTT_HOST || "mqtt://127.0.0.1"
const mqtt_topic = process.env.MQTT_TOPIC || "rpipicowpower";

console.log("Connecting to mqtt " + mqtt_host);
const client = mqtt.connect(mqtt_host);

app.post('/api/on', (req, res) => {
    console.log("Publishing on to " + mqtt_topic);
    client.publish(mqtt_topic, "on");
    res.json({result: 0})
})
app.post('/api/off', (req, res) => {
    console.log("Publishing off to " + mqtt_topic);
    client.publish(mqtt_topic, "off");
    res.json({result: 0})
})

app.listen(3000, () => console.log('Server is up and running'));