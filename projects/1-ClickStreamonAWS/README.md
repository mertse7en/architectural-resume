# Click Streaming on AWS


## Architecture

<br>

<p align="center" width="100%">
    <img width="80%" src="img/clickstreamarch.png">
</p>


## Description:
Tha main aim of this project is to create event-streaming data architecture for an international VOD application. The size of data pushed to our streaming apps is approx 30-50 GB daily.
There are 3 main steps:

### 1- Landing
The first layer of architecture is the landing/ingesting layer. Each event collector pushes data through to Kinesis Data Streams, each data stream has data retention of 7 days.

BUCKETS 

We have 3 different s3 buckets;

<p align="left" width="100%">
    <img width="50%" src="img/buckets.png">
</p>


Each data stream has kinesis firehose sink that pushes data directly to row_json bucket



### Faced Issues

