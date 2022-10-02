# Datamarts on BQ

## Description:

**Problem**


There were inconsistent data source problem due to firebase integration. Firebase exports daily raw batch data to BigQuery. Data Analysts feeds datamarts using raw table via scheduled queries but incoming data arrival time may change. 

**Solution** :

I solved this problem using Airflow. Because airflow BigQuerySensorOperator and BigQueryCheckOperator can wait table to be filled and also Airflow is one of the best way to orchestrate consecutive jobs.

## Architecture

<br>

TODO:
<p align="center" width="100%">
    <img width="80%" src="img/.png">
</p>


## 🐵 Faced Issues