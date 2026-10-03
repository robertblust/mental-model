---
id: 01a03da5-1868-73f2-a230-1a895d40401e
source: Local
kind: Project
start: 2019-08
end: 2020-09
url: https://3ap.ch/case_studies/platform-for-digital-rental/
organization: Aroov
role: Backend & Integration Architect
skills:
  - Database design
  - Event-driven architecture
  - Microservices architecture
  - API design
  - Integration architecture
  - Solution selling
  - Solution architecture
---

# Aroov digital rental platform

> 3AP · Backend & Integration Architect — a digital rental platform on the reference architecture in its event-driven form, the first of them on PostgreSQL, integrated with Garaio REM.

## Achievements

### Context

- Digital rental platform — applicants apply for apartments in a few clicks; property managers get automated workflows and radically simpler applicant communication.
- Founded by Mobiliar and Garaio REM (2019), merged with market leader flatfox.ch (2021).

### Leadership

- Presented the solution architecture in the winning sales pitch.

### Architecture

- Created the backend architecture as 3AP's microservice reference architecture in its event-driven form, delivery pipeline included, on Google Cloud with Spring Boot, Kubernetes/GKE and Cloud Pub/Sub.
- Designed Aroov's PostgreSQL schema, the first of the platforms to hold its data in PostgreSQL rather than a document store.
- Designed Aroov's own microservice cut.
- Designed the integration architecture connecting Aroov to Garaio REM, a Swiss property-management system and an Aroov co-founder, after first diagnosing what Garaio REM offered for integration.
- Designed the event flow behind that integration: Garaio REM's data fetched over SFTP on a schedule, transformed into events and published to Google Cloud Pub/Sub through Spring Cloud Stream.
- Designed the REST API the Aroov front end was built against.

### Results

- One of four winners of the Digital Top 10 2021, voted by over 5,000 participants ahead of the Digital Real Estate Summit.

## References

| What | URL |
| --- | --- |
| Article | https://www.finews.ch/news/versicherungen/47571-flatfox-aroov-mobiliar-matthias-frieden-bernhard-maeder-fusion |
| Award announcement | https://www.gebaeudetechnik-news.ch/digital-top-10-gewinner-stehen-fest/ |
