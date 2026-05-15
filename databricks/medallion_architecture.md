### Way to ingest data to databeicks:
- manually uplode files to volume
- create incremental ingestion with Lakeflow connect

### Common table & view types
- managed table: Databricks fully manages both the data storage and metadata
- streaminng table: a table that is only updated with new data
- view: a virual table defined by a query that is computed each time it is accessed
- materialized view: a view where the query result is physically stored

### ELT pipeline in Databricks 
- can be built with Lakeflow Spark Declarative Pipeline or Apache Spark
- with Lakeflow SDP: 
    - define data assets in Python/SQL -> ELT pipeline determines interdependency of data assets -> schedule the ELT pipeline with Lakeflow Job

# Bronze layer


