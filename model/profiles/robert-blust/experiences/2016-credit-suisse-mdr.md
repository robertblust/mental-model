---
source: Local
kind: Project
start: 2016-02
end: 2016-09
organization: Credit Suisse
role: Lead Architect & Developer
skills:
  - Model-driven engineering
  - Data governance
  - Data engineering
  - Solution architecture
  - Solution selling
  - Software architecture
  - Frontend development
  - Data modeling
  - UX design
---

# Credit Suisse Master Data Repository

> 3AP · Lead Architect & Developer — the Master Data Repository for Client Data Management, built on the Flatland CDO Server so data stewards and golden sources could be assigned and mapped for a FINMA requirement.

## Achievements

### Context

- Built the Master Data Repository (MDR) for Credit Suisse Client Data Management — managing data items and classifying their source systems so data stewards could be assigned, and mapping the distribution of data across the core systems (golden source vs. slave), identified and visualized for governance.

### Leadership

- Delivered to satisfy a FINMA regulatory requirement.

### Architecture

- Designed the metamodel of data items, source systems and their golden-source mapping, and let the repository and its front end follow from it.

### Engineering

- Implemented on the Flatland CDO Server rather than on stock Eclipse CDO — the model repository published as open source two years earlier, brought to a bank as the foundation of paid work — with an Angular front end built along the same lines as the generic model browser published beside that server, and fed by static source-code analysis and several data sources to discover and connect the model.
- Built the ingestion that filled it from two sources: the output of the bank's existing source-code analysis and the database schemas of the core systems, both read and transformed on the way in.

### Results

- Won without a tender: the problem was known inside the bank and reached 3AP through its network, and the work followed a proposed solution architecture rather than a specification.

## References

| What | URL |
| --- | --- |
| Flatland CDO Server repository | https://github.com/robertblust/cdo-server |
| Model browser repository | https://github.com/robertblust/cdo-web |
