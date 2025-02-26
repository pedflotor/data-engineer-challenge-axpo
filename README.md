# Data Engineer - Challenge

## Intro

Axpo's infrastructure generates lots of data. Our goal is to make use of this
data to improve our decision base.

To do so we need you to collect, store and prepare data for BI specialists
and Data Scientists.

## Your mission, should you choose to accept it:

### Initial position

* List of Sensors (see iot_data_generator/sensors.json)
* Docker compose environment containing
    * IoT data generator (python, docker)
    * MQTT Broker

### Rule set

* **Please invest no more than 5 to 8 hours.** If you cannot complete the task
  in this time frame, document where you got stuck, so we can use this as a
  basis for discussion for your next interview.
* You're free to choose the tech stack you feel fitting
* You're allowed to change existing code to suit the purpose
* If you cant solve a problem you can also skip or simulate it and describe your
  thoughts.

### Part One: Coding Challenge

We want to see your coding skills. Implement the following 2-3 steps and
extend the docker compose environment, so we can run your solution using
```docker compose up -d```.

#### Step 1:

The first goal is to collect and store the IoT data as well as the corresponding
sensors in raw format to a low cost long term storage.

docker-compose up -d --build --> build images
docker ps --> check images running
docker logs data-engineer-challenge-axpo-iot_data_generator-1 --> check data generated
docker-compose down --> stop


#### Step 2:

The second goal is to make the data available so BI specialists can query
historical data until current point in time (near real time) for different
sensors.
docker-compose logs data_collector --> check exposing data to http://localhost:8000/sensors/

#### Step 3 (optional, if there is still time after Part Two):

Implement one of the following features:

* resample IoT data to 1 min mean values --> http://localhost:8000/sensors/aggregated10/
* data catalogue for customers
* data quality indicator

### Part Two: Solution Design

Imagine you're not bound to local development, so you could use whatever
services and products are out there.

* How would you solve the problem stated in Part One now?

#### Infraestructure
1. Data Ingestion:
Azure IoT Hub:
For ingesting IoT data. Supports a variety of protocols, including MQTT, which is ideal for low-latency, high-frequency sensor data.
2. Data Storage:
Azure Blob Storage:
Provides cost-effective, scalable storage. Store the raw IoT sensor data in its native format (e.g., JSON, CSV, or Avro).
Azure Data Lake Storage Gen2: supports hierarchical namespace and allows for easy organization of data into folders, which is perfect for organizing time-series data or sensor-specific files.
3. Data Processing:

    3.1 Azure Stream Analytics (more specific)
    
    3.2 Azure Databricks (global solution, advanced data processing, including batch processing and large-scale transformations). Can aggregate raw IoT data into structured forms (such as Parquet or Delta format) and store the results in Azure Blob Storage or a data warehouse.

    3.3 Azure Functions (serverless compute to trigger specific tasks based on events)

4. Data Storage for Querying:
    
    4.1 Azure SQL Database (For structured querying of processed sensor data)

    4.2 Azure Cosmos DB (in case the IoT data needs to be stored in a NoSQL format)

    4.3 Azure Time Series Insights (For time-series data specifically)

5. Data Access Layer (API):
- Azure API Management (create a front-end API for exposing processed data stored in Azure SQL Database or Cosmos DB) 

6. Data Monitoring & Alerts:
- Azure Monitor (monitor the health of data pipelines and IoT devices. Set up alerts)
- Azure Application Insights (Used to identify bottlenecks, track requests, and monitor the performance of services)

7. Data Quality Monitoring:
- Azure Purview (Discover and classify data)
- Great Expectations (on Databricks) (Fine-grained control over data quality)

8. Security & Compliance:
- Azure Active Directory (Azure AD) (User authentication and role-based access control (RBAC))
- Encryption & Network Security (Azure Key Vault)
- Use Virtual Networks to secure the communication between services.

#### Deployment Strategy on Azure
- Infrastructure as Code: Use Azure Resource Manager (ARM) Templates or Terraform to define the IaC. Allows to version control the infrastructure.
- CI/CD Pipelines: Set up Azure DevOps to automate the deployment of both the infrastructure (using ARM Templates or Terraform) and the application code (e.g., APIs, functions, or data processing scripts). Automate testing and monitoring of these deployments to ensure seamless delivery.



Design you favorite solution to solve the problem. There is no need for any
code in this part. Just write down your thoughts and arguments in a technical
draft. Don't lose time over-engineering or over-designing it.

May the following questions help you:

* How would your favorite architecture look like?
* What technologies and services would you use?
* How would you deploy the required infrastructure?
* How would you monitor your data pipelines?
* How would you monitor and improve data quality?
* How would you communicate with customers consuming the data?
* ...

### Evaluation criteria

What we're looking for:

* We want to see what you can do, not what you can't do
* The ability to determine the actual problem area and find a suitable solution
* Pragmatic solution, scratch features when necessary, time is short!
* Document your approach, your decisions, and your general notes directly in
  your code or in a readme file (for Part One)

## Preparations for the interview

* open your project in your IDE
* have your environment running
* be prepared to present your approach for 5-10 min (no Slides!)
* be prepared to answer a few questions after your presentation

# TODOs:

* improve instructions above
* let challenge be challenged by internals