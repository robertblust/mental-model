---
id: 01a03da5-1868-776d-996c-8471613a113e
source: Local
kind: Project
start: 2018-07
end: 2019-02
url: https://3ap.ch/case_studies/networked-first-aid-kit/
organization: Flawa
role: Solution Architect
skills:
  - Integration architecture
  - Solution architecture
  - Solution selling
  - Microservices architecture
  - Event-driven architecture
  - IoT architecture
  - Data engineering
  - Java
  - Database design
  - Cloud architecture
---

# Flawa iQ

> 3AP · Solution Architect — a networked first-aid kit that detects missing or expired modules over LoRaWAN and reorders them, from the sensing research to 10 working prototypes.

## Achievements

### Context

- An IoT first-aid kit for FLAWA AG that keeps itself stocked and compliant — Swiss firms are legally required to maintain first-aid supplies, so the kit detects missing or expired modules in real time and automatically triggers reordering, removing manual checks.

### Architecture

- Ran the initial sensing research — how to detect the absence of an item within a defined volume — and selected RFID-tagged modules as the approach.
- Chose the sensors' connectivity after evaluating LoRaWAN against GSM: LoRaWAN on Swisscom's network for the MVP, GSM for the later production version.
- Designed the microservice cut of the backend, separating the telemetry ingestion from the communication with the ERP.
- Designed the MongoDB data model the device uplinks and configuration events were held in.
- Designed the backend's deployment on Swisscom Application Cloud, Swisscom's Cloud Foundry: each service pushed with a manifest, with the message broker and the database bound to it as managed services rather than run beside it.

### Engineering

- Together with comtac AG (a canton-Zürich LoRaWAN electronics specialist), delivered an MVP of 10 working prototypes (RFID modules + LoRaWAN, backend on Swisscom Application Cloud).
- Built the backend to 3AP's microservice reference architecture on Spring and Java 11, released through a Jenkins pipeline.
- Closed the reorder loop: device uplinks consumed over AMQP from Swisscom's LoRaWAN broker, held in a reactive MongoDB repository, pushed to the client as server-sent events and transformed into the data the ERP needed, so a consumed or expired module triggers its reorder.

### Results

- Won the work in a competitive pitch, presenting the solution architecture for a problem the client had described rather than specified.
- Won the “smart IoT” Award 2021, University of St. Gallen.

## References

| What | URL |
| --- | --- |
| Award announcement | https://flawa-iq.ch/de/blog/flawa-gewinnt-smart-iot-award |
| Trade article on the award | https://www.safety-security.ch/vernetzter-notfallkoffer-flawa-iq/ |
