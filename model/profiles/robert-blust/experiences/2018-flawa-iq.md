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
  - Microservices architecture
  - IoT architecture
  - Data engineering
  - Cloud architecture
  - API design
---

# Flawa iQ — Networked First-Aid Kit

> 3AP · Solution Architect — IoT sensing & connectivity.

## Achievements

- An IoT first-aid kit for FLAWA AG that keeps itself stocked and compliant — Swiss firms are legally required to maintain first-aid supplies, so the kit detects missing or expired modules in real time and automatically triggers reordering, removing manual checks.
- Ran the initial sensing research — how to detect the absence of an item within a defined volume — and selected RFID-tagged modules as the approach.
- Evaluated the connectivity options (LoRaWAN vs. GSM); built the MVP on Swisscom's LoRaWAN network, with GSM selected for the later production version.
- Together with comtac AG (a canton-St.-Gallen LoRaWAN electronics specialist), delivered an MVP of 10 working prototypes (RFID modules + LoRaWAN, backend on Google Cloud).
- Built the backend that ingests device telemetry from Swisscom's LoRaWAN broker, plus an API feeding the data into the ERP — closing the loop so consumed or expired modules trigger automatic reordering, to 3AP's microservice reference architecture.
- Won the “smart IoT” Award 2021, University of St. Gallen: https://flawa-iq.ch/de/blog/flawa-gewinnt-smart-iot-award
