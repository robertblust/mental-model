---
source: Local
kind: Community
start: 2014-08
end: 2022-03
url: https://github.com/robertblust/cdo-server
skills:
  - Open-source stewardship
  - Model-driven engineering
  - Domain-specific language design
  - Organization design
  - API design
  - Identity and access management
  - Java
---

# Flatland CDO Server — A Model Repository Anyone Can Run

> Published an Eclipse CDO server that serves any model over REST without code written for that model, then described a company on it.

## Achievements

- Published the server in August 2014 and kept it public since, under the Eclipse Public License: seven people have starred it and three have forked it to build on, none of whom he knows.
- Made the REST interface generic by going through EMF's reflective API rather than generated accessors, so a model added to the repository is readable and writable the same day without an endpoint written for its types.
- Shipped it as something to run rather than assemble — an OSGi product with its own target platform, build and product tests, packaged as a container image — because a model repository that takes a week to stand up is one nobody tries.
- Wrote a plugin authenticating CDO sessions against LDAP, and later took bearer tokens at the REST boundary, so the repository could sit behind the same identity as everything around it.
- Designed a base vocabulary every model on top inherits — identity, naming, description, comments, hyperlinks, free-form properties, ratings and a global search marker — so the models above it describe their own domain and nothing else.
- Described 3AP's own organization in that vocabulary: circles nested inside circles, roles carrying responsibilities, and an assignment joining a person to a role in a circle with a capacity and a validity window, which is what makes the structure answerable by date rather than only as it stands today.
- Derived the questions a management team actually asks from that model instead of maintaining answers by hand — a circle's capacity including everything nested under it, who leads or deputizes where, which roles are assigned but unmatched, and which are defined and unfilled.
