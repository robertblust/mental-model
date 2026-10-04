---
id: 01a03da5-1868-7f9e-a0af-04d886c78518
source: Local
kind: Project
start: 2015-12
end: 2016-09
organization: Swisscard
role: Backend Engineer
skills:
  - Java
  - Legacy modernization
---

# Swisscard data integration rewrite

> 3AP · Backend Engineer — replaced the proprietary SOAP layer in front of Swisscard's core platform with Spring Boot behind the same WSDL contract, so no consumer had to change.

## Achievements

### Context

- One of 3AP's first client mandates: a proprietary Informatica Data Services SOAP layer fronted the core platform.

### Engineering

- Replaced that SOAP layer with a Spring Boot / Spring WS implementation over MSSQL through Spring Data, preserving the existing WSDL contract so no consumer had to change.
- Covered the replacement with JUnit tests run on Jenkins.
