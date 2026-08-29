---
source: Local
group: Data
---

# Event streaming

> Building systems that publish, transport and consume continuous streams of events in near real time.

## In practice

Design topics or streams, partitioning and retention policies that fit how data will be
produced and consumed. Build producers and consumers that handle ordering, delivery guarantees
and backpressure correctly. Monitor stream throughput and lag to catch consumers falling behind
before it affects downstream systems. Typical tools: Kafka, Kinesis, Pulsar.
