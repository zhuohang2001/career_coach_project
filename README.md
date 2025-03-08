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

### **Scenario 1 (AWS) Setup**

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

### **Scenario 2 (Azure) Setup**

1. Navigate to the Scenario 2 directory:
   ```sh
   cd scenario_2
   ```
2. Run CLI commands for processing:
   ```sh
   python main.py --carpark CARPARK123  # Find details by carpark number
   python main.py --address "Blk 123"    # Search by address keyword
   ```
3. Run tests:
   ```sh
   pytest tests/
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
  ```

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

## 🏗 System Architecture

- **Scenario 1:** AWS-based serverless data processing.
- **Scenario 2:** Azure-based batch & real-time data ingestion pipeline.

> Architecture diagrams are available in `docs/architecture_scenario1.png` and `docs/architecture_scenario2.png`.

---

