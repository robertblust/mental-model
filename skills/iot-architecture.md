---
source: Local
group: Architecture
---

# IoT architecture

> Designing the path from a physical device to a business system: sensing, connectivity, ingestion, use.

## In practice

Choose the sensing and the radio for the device's power, range and cost, not for the
demo. Design the ingestion so that unreliable, bursty telemetry becomes a clean stream the
business systems can consume. Prototype with real devices in the real environment before
committing to a platform. Typical tools: LoRaWAN, RFID, MQTT.
