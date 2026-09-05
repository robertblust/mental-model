---
source: Local
kind: Community
start: 2021-06-03
end: 2021-06-03
url: https://engineering.3ap.ch/post/process-monitoring-with-bpmn/
organization: 3AP AG
skills:
  - Business process modeling (BPMN, DMN)
  - Process orchestration
  - Observability
  - Technical writing
  - Java
---

# Published Article — Process Monitoring with BPMN

> 3AP · Wrote the article and built the sample it runs on: finding a stalled guest journey by the message that never arrives.

## Achievements

- Published “Process Monitoring with BPMN” on 3AP's engineering blog on 3 June 2021, making the case that a process model is worth keeping at runtime and not only at design time.
- Set out a way to watch a guest journey without touching the services that run it: every system already posts webhooks, so a monitor correlates those events against a model of the journey and knows where each booking has got to.
- Turned each milestone into a receive task waiting for its message — booking confirmed, onboarding notification, online check-in, property access issued, check-out — with a boundary timer beside it, so the alert fires on the message that never came rather than on an error somebody has to notice.
- Published a runnable sample alongside it, still public: a Spring Boot service taking the webhooks behind an OpenAPI description, a Zeebe engine and Camunda Operate in one Docker Compose file, and the guest-journey model itself.
- Put BPMN and Zeebe to work in the open a year before the CamundaCon talk and two before the published case study, while the platform they describe was still being built.
