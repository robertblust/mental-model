---
source: Local
group: Architecture
---

# Legacy modernization

> Bringing a system built for another era forward without stopping the business that runs on it.

## In practice

Wrap the legacy system in a stable interface before touching its inside. Generate rather
than hand-write the bridging code where the interfaces are numerous and regular. Replace one
layer at a time, keeping the old path alive until the new one has carried production load.
