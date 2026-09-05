---
source: Local
kind: Project
start: 2018-07
end: 2019-02
url: https://3ap.ch/case_studies/networked-first-aid-kit/
organization: Flawa
skills:
  - Integration architecture
  - Solution architecture
  - Solution selling
  - Microservices architecture
  - Event-driven architecture
  - CI/CD
  - IoT architecture
  - Data engineering
  - Frontend development
  - Java
  - Database design
  - Cloud architecture
  - API design
---

# Flawa iQ

> 3AP · Solution Architect — a networked first-aid kit that detects missing or expired modules over LoRaWAN and reorders them, from the sensing research to 10 working prototypes.

## Achievements

- An IoT first-aid kit for FLAWA AG that keeps itself stocked and compliant — Swiss firms are legally required to maintain first-aid supplies, so the kit detects missing or expired modules in real time and automatically triggers reordering, removing manual checks.
- Ran the initial sensing research — how to detect the absence of an item within a defined volume — and selected RFID-tagged modules as the approach.
- Evaluated the connectivity options (LoRaWAN vs. GSM); built the MVP on Swisscom's LoRaWAN network, with GSM selected for the later production version.
- Together with comtac AG (a canton-St.-Gallen LoRaWAN electronics specialist), delivered an MVP of 10 working prototypes (RFID modules + LoRaWAN, backend on Google Cloud).
- Built a small React front end for the MVP so the sensor readings could be seen rather than inferred from the telemetry.
- Built the backend to 3AP's microservice reference architecture on Spring and Java 11, released through a Jenkins pipeline — consuming device uplink and configuration events over AMQP from Swisscom's LoRaWAN broker, holding them in a reactive MongoDB repository, pushing them on to the client as server-sent events and feeding the data into the ERP over an API, which closes the loop so consumed or expired modules trigger automatic reordering.
- Won the work in a competitive pitch, on a solution architecture for a problem the client had described rather than specified.
- Won the “smart IoT” Award 2021, University of St. Gallen: https://flawa-iq.ch/de/blog/flawa-gewinnt-smart-iot-award
