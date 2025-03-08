# Career Coach Project - README

## 🚀 Project Overview

This project contains two scenarios, **Scenario 1** and **Scenario 2**, each implementing different data processing pipelines using cloud services.

- **Scenario 1 (AWS-based):** Extracts and processes restaurant event data, transforming JSON files into structured formats.
- **Scenario 2 (Azure-based):** Processes and updates car park availability information, integrating real-time and static datasets.

---

## ⚙️ Setup Instructions

### **Prerequisites**

1. Install **Python 3.10 or higher** (as required by the `requirements.txt` file).
2. Ensure you have `pip` installed.
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

### **Scenario 1 - Restaurant Data Processing**

#### **Running Locally**
1. Navigate to the Scenario 1 directory:
   ```sh
   cd scenario_1
   ```
2. Run the application:
   ```sh
   python main.py
   ```
3. Run tests:
   ```sh
   pytest tests/
   ```

#### **Running on Deployed Server (Render)**
- **Base URL:**  
  👉 [https://career-coach-project-scenario-1.onrender.com](https://career-coach-project-scenario-1.onrender.com)

- **Trigger the full data processing pipeline:**
  ```sh
  curl -X POST "https://career-coach-project-scenario-1.onrender.com/process-all"
  ```
  - This will extract restaurant details, process April 2019 event data, and analyze ratings.

---

### **Scenario 2 - Car Park Availability**

#### **Running Locally**
1. Navigate to the Scenario 2 directory:
   ```sh
   cd scenario_2
   ```
2. Run CLI commands for processing:
   ```sh
   python main.py --carpark A12  # Find details by carpark number
   python main.py --address "Tampines"    # Search by address keyword
   ```
3. Run tests:
   ```sh
   pytest tests/
   ```

#### **Running on Deployed Server (Render)**
- **Base URL:**  
  👉 [https://career-coach-project-scenario-2.onrender.com](https://career-coach-project-scenario-2.onrender.com)

- **Search for car park details by car park number:**
  ```sh
  curl "https://career-coach-project-scenario-2.onrender.com/get-availability?carpark_id=A12"
  ```

- **Search for car parks by address keyword:**
  ```sh
  curl "https://career-coach-project-scenario-2.onrender.com/get-availability/search?address=Tampines"
  ```

---

## 📌 Usage Examples

### **Scenario 1**
- Run the full restaurant data processing pipeline:
  ```sh
  python main.py
  ```
  This automatically:
  - Extracts restaurant details
  - Extracts April 2019 event data
  - Analyzes and categorizes restaurant ratings

### **Scenario 2**
- Search for car park details by **car park number**:
  ```sh
  python main.py --carpark A12
  ```
- Search for car parks by **address keyword**:
  ```sh
  python main.py --address "Tampines"
  ```

---

## 🔑 Key Design Decisions

### **Scenario 1 (AWS)**

- Used **AWS Lambda** for serverless execution of data extraction scripts.
- **Amazon S3** stores raw data before transformation.
- **AWS Glue** processes JSON and CSV files before storing them in **AWS RDS** for structured querying.
- **AWS CloudWatch** monitors Lambda function execution.
- **AWS CodePipeline & CodeBuild** automate CI/CD.

### **Scenario 2 (Azure)**

- **Azure App Service** runs the CLI-based application.
- **Azure Data Factory** handles static car park data ingestion.
- **Azure Logic Apps** fetches real-time data from external APIs.
- **Azure SQL Database** stores processed results for efficient querying.
- **Azure API Management** can be used to expose REST endpoints in the future.
- **GitHub Actions CI/CD** automates Docker builds and deployment.

---

## 🛠 Assumptions & Interpretations

- The input dataset formats remain **consistent** (i.e., JSON for Scenario 1, CSV for Scenario 2).
- API endpoints for real-time data in Scenario 2 remain **available and stable**.
- CI/CD pipelines ensure seamless deployment without manual intervention.
- Scenario 2 may **later transition into a full API-based system**, replacing the CLI.

---

## 🏢 System Architecture

- **Scenario 1:** AWS-based serverless data processing: 

The restaurant data extraction system processes raw JSON datasets and transforms them into structured data for analysis and reporting. The design leverages AWS services for event-driven processing, automation, and cost-efficiency.

The process begins with Amazon S3, where new restaurant datasets are uploaded. This triggers AWS Lambda, which orchestrates three key tasks: extracting restaurant details, filtering event data for April 2019, and categorizing restaurant ratings. Lambda’s serverless architecture minimizes compute costs, only running when necessary.
For ETL (Extract, Transform, Load) processing, AWS Glue extracts raw event and restaurant data, performs schema inference, and processes it into a structured format. The transformed data is stored in AWS RDS (PostgreSQL), chosen for scalability and efficient structured queries.

Monitoring and security are critical to the system’s reliability. AWS CloudWatch tracks execution logs and performance metrics, helping diagnose failures. AWS Secrets Manager ensures database credentials remain secure, reducing exposure risks.
For automated deployment, AWS CodePipeline and AWS CodeBuild handle continuous integration and deployment, streamlining updates for Lambda functions and Glue scripts.
Currently, the system operates as a batch-processing pipeline, but it can be expanded with AWS API Gateway to expose the processed data for external applications, allowing real-time querying.

This deployment balances cost, performance, and automation, ensuring reliable restaurant data extraction, minimal operational overhead, and easy future upgrades.

--------------------------------------------------------------------------
- **Scenario 2:** Azure-based batch & real-time data ingestion pipeline:

The car park availability system integrates static and real-time data from the Singapore Government Data API to ensure up-to-date parking availability. The architecture is designed for scalability, resilience, and efficiency, leveraging Azure cloud services to automate ingestion, processing, and deployment.

The system is hosted on Azure App Service, which provides automatic scaling and serverless management to handle fluctuating demands efficiently. While currently implemented as a Command Line Interface (CLI) tool, the architecture allows easy expansion into API-based or web-based services. Azure Functions could further enhance real-time data processing by triggering updates when API changes occur.

For data ingestion, Azure Data Factory automates the scheduled loading of static datasets, while Azure Logic Apps fetch real-time updates periodically. Azure Blob Storage serves as an intermediate storage layer for raw files before processing. Azure SQL Database was selected for its ability to efficiently store structured, merged datasets, ensuring fast querying and data consistency.

Security and observability are managed using Azure Monitor and Application Insights, allowing real-time tracking of system performance, error detection, and diagnostics. Azure Key Vault securely stores API keys and database credentials, preventing exposure of sensitive information in the codebase.

Deployment is containerized using Docker, with images stored in Azure Container Registry (ACR) for consistency across environments. GitHub Actions CI/CD automates builds and deployments, ensuring smooth updates.

This architecture supports real-time processing and future scalability, allowing enhancements like public REST APIs, predictive analytics, and user-facing applications.


---------------------------------------------------------------------------------------**
> Architecture diagrams are available in `docs_diagrams/architecture_scenario1.png` and `docs_diagrams/architecture_scenario2.png`.

---

