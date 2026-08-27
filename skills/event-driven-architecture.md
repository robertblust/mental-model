---
source: Local
group: Architecture
---

# Event-driven architecture

> Designing systems where components communicate by producing and reacting to events rather than through direct calls.

## In practice

Identify the events that matter to a system and design the producers, consumers and channels
that carry events between them. Make decisions about ordering, delivery guarantees and how
components stay decoupled while still working together. Design for failure modes specific to
asynchronous systems, such as duplicate or out-of-order events. Typical tools: Kafka, RabbitMQ,
AWS EventBridge.
