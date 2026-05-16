# Glossery & terms

## What is Databricks?
- **Databricks**: is a unified data platform for building enterprise-level cloud infrastrucutre, 
including components like data lakehouse, data pipeline, BI, data science/AI and data governance. 
It provides a collaborative workspace for data engineers, data analysts, data scientists, ML engineers, data owners and other data roles to develop and share in the same platform.  


- **Data Lakehouse**: A data lakehouse merges the best of data lakes and data warehouses. 
While it allows enterprises to store raw data in its native format (like a data lake), it also enables the creation of delta tables, 
bringing warehouse-like advantages such as ACID transactions, schema enforcement, and fine-grained access control.


- **Data pipeline**: Enterprises can run their data pipelines using databricks's computing resources. 
The ELT logic and orchestration can be defined using Spark and SQL with Lakeflow Spark Declarative Pipeline and Lakeflow Job.


- **Business Intelligence**: Dashboards can be created and shared to other users on databricks, 
allowing visualization to be hosted on the same platform as the data inputs to the visualization.


- **Data Science & AI**: Data scientists and machine learning engineer can train, deploy and serve their classical ML and AI models using the computer resources in databricks. 
They are also able to manage the entire ML lifecycle with MLflow.


- **Data Governance**: Enterprises can use Unity Catalog as a single tool to manage premissions for both data objects and models.

### Glossery exercise_0
| terminology                         | explanation |
| ----------------------------------- | ----------- |
| on-premises IT infrastructure       |Refers to computing resources physically located within a company’s premises, including servers, storage, and networking equipment.             |
| cloud IT infrastructure             |Cloud infrastructure is a collection of hardware and software elements, including resources such as servers, storage, networking, and databases, that cloud providers offer on a pay-as-you-go, as-needed basis.             |
| 3 Vs of big data                    |Volume, Velocity & Variety.|
| scalability                         |Cloud scalability is the ability of a cloud computing system to increase or decrease its resources, such as computing power, storage, and network bandwidth, to meet changing demands.             |
| availability                        |Cloud availability refers to the ability of a cloud computing system to be accessible and usable upon demand by an authorized user.             |
| lakeflow connect                    |A unified, intelligent solution for data ingestion, designed to streamline and accelerate the process of bringing data into the Databricks Data Intelligence Platform.             |
| lakeflow spark declarative pipeline |Lakeflow Spark Declarative Pipelines is a declarative framework for developing and running batch and streaming data pipelines in SQL and Python.             |
| unity catalog                       |Unity Catalog is a unified governance layer for the Databricks Data Intelligence Platform that provides centralized access control, auditing, and data lineage across your entire cloud infrastructure. It acts as a single "source of truth" to securely manage and discover all your data, AI models, and files in one place.             |
| data lakehouse                      |Provides scalable storage and processing capabilities for modern organizations that want to avoid isolated systems for processing different workloads, like machine learning (ML) and business intelligence (BI). A data lakehouse can help establish a single source of truth, eliminate redundant costs, and ensure data freshness.             |
| delta table                         |An optimized storage layer that brings reliability to data lakes by using a transaction log to manage data through ACID transactions and versioning. It allows you to treat large collections of cloud files like a traditional database, enabling powerful features like "time travel" (data versioning) and schema enforcement.             |
| lakeflow jobs                       |A Databricks feature for orchestrating and scheduling workflows. You can chain together notebooks, pipelines, and scripts to run automatically — either on a schedule or triggered by an event.             |
| spark                               |An open-source distributed computing framework designed to process large amounts of data fast. Instead of running on one computer, Spark splits the work across many computers (a cluster) at the same time.             |
| pyspark                             |The Python API/bridge for Apache Spark. It enables you to preform real-time, large-scale data processing in a distributed enviorment using Python.|
| data intelligence platform          |Databricks' name for their overall platform. It combines data storage, data processing, machine learning, and AI in one place — with an "intelligent" layer on top that helps users find, understand, and work with their data using AI.             |
| medallion                           |A data design pattern used to organize data in layers, where each layer improves the quality of the data. Named after medals because the layers are called Bronze, Silver, and Gold.             |
| ginie                               |An AI-powered assistant in Databricks that lets you ask questions about your data. You just type a question like "what is the average price per neighborhood?" and Genie writes and runs the query for you.             |
| spark declarative pipline           |A framework in Databricks for building data pipelines where you describe what you want the data to look like, not how to process it step by step. Databricks handles the execution, error handling, and scheduling automatically.             |
| data linage                         |A way to track where data comes from, how it has been transformed, and where it ends up. It shows the complete journey of data — from source to final table. In Databricks you can see this visually under the "Lineage" tab in Catalog.             |



