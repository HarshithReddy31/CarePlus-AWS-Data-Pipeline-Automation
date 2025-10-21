# 🧩 CarePlus AWS Data Pipeline Automation  

---

## 📝 Overview  
This project showcases how I built an **end-to-end data pipeline for CarePlus** to automate data ingestion, transformation, and analytics using **AWS services**.  
The solution replaces manual workflows with an event-driven, scalable, and secure cloud-based architecture.  

---

## 🚀 Key Features  
- Ingested raw data into **Amazon S3** directly from **Jupyter Notebook**  
- Automated ETL processes with **AWS Lambda** and **AWS Glue**  
- Triggered workflows using **S3 Event Notifications**  
- Managed secure access with **IAM Roles and Policies**  
- Loaded curated data into **Amazon Redshift** for analytics  
- Performed ad-hoc queries using **Amazon Athena**  
- Built BI dashboards in **Power BI**  
- Configured **AWS Budgets** for cost tracking and optimization  

---

## 🏗️ Architecture  

**Services Used:**  
`Jupyter Notebook → S3 → Lambda → Glue → Redshift → Athena → Power BI`  
Supporting Services: **IAM (Access Control)** | **S3 Events (Automation)** | **AWS Budgets (Cost Management)**  

### **Workflow Summary:**  
1. Data uploaded to S3 (via Jupyter Notebook)  
2. **S3 Event** triggers **Lambda Function**  
3. Lambda invokes **AWS Glue Job** for transformations  
4. Transformed data stored back in S3 (Parquet format)  
5. **Redshift** consumes curated data for reporting and dashboards  

---

## 📂 Repository Structure  

careplus-aws-data-pipeline/
│
├── lambda_function.py
├── glue_etl_script.py
├── jupyter_ingestion.ipynb
├── architecture_diagram.png
├── README.md
├── requirements.txt
├── LICENSE
└── sample_data/
    ├── input_data.csv
    └── transformed_data.parquet

---

## 🧠 Problem Solved  
CarePlus had a manual, error-prone process for managing support ticket data.  
This project **automated the entire ETL workflow**, improving **data accuracy**, **reducing latency**, and **accelerating insights** by over **60%**.  

---

## 💡 Tech Stack  
**Languages:** Python, SQL  
**AWS Services:** S3, Lambda, Glue, Redshift, Athena, IAM, Budgets  
**Tools:** Jupyter Notebook, Power BI  

---

## 🧾 Results  
✅ Reduced data processing time from hours to minutes  
✅ Achieved fully automated ETL with event triggers  
✅ Improved data reliability and cost efficiency  
✅ Enabled real-time insights for business teams  

---

## 🔗 How to Run  

1. Upload your dataset to an **S3 bucket**  
2. Deploy **Lambda function** using the provided script  
3. Configure **S3 event trigger** to invoke the Lambda  
4. Create and run the **AWS Glue Job** with the ETL script  
5. Analyze or visualize results in **Athena** or **Power BI**  

---

### 🏷️ Tags  
`AWS` `Data Engineering` `ETL` `Automation` `Lambda` `Glue` `Redshift` `Cloud` `Data Pipeline`  

## 👨‍💻 Author

**Sai Harshith Reddy Gaddamidhi**  



