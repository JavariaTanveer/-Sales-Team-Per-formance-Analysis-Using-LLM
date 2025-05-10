

# 📊 Sales Team Performance Analysis Using LLM

A backend system that leverages a Large Language Model (LLM) via Hugging Face API to analyze and generate insights on sales performance data.

---

## 🚀 Features

* **Upload Sales Data**
  Accepts input in CSV or JSON format for performance evaluation.

* **Individual Performance Feedback**
  Generates AI-driven feedback for individual sales representatives.

* **Team Summary Report**
  Provides a summary of overall team performance using historical data.

* **Sales Trends & Forecasting**
  Detects monthly or quarterly trends and forecasts future sales potential.

---

## 🧠 Tech Stack

* **FastAPI** – Web framework for building APIs
* **Uvicorn** – ASGI server for running the FastAPI app
* **Pandas** – Data manipulation and analysis
* **Hugging Face Transformers** – LLM integration for text-based analysis

---

## 🔑 Setup Instructions

1. **Install Dependencies**

   ```bash
   pip install fastapi uvicorn pandas huggingface-hub
   ```

2. **Set Your Hugging Face API Key**

   Create a `.env` file or directly include your API key in the script where required.

3. **Run the API Server**

   ```bash
   uvicorn APIs:app --reload
   ```

4. **Test with Postman**

   Refer to `postman.txt` for ready-to-import Postman test cases.

---

## 📁 Project Structure

* `sales_performance_data.csv` – Sample sales dataset
* `Data Ingestion.py` – Data loading and preprocessing logic
* `LLM integeration.py` – Functions for interacting with the LLM
* `APIs.py` – FastAPI routes and endpoints
* `postman.txt` – Postman test case collection

---

## 🧪 Example Use Cases

* Analyze individual employee sales performance
* Generate automated team reports
* Forecast quarterly sales with AI interpretation

![Sales Team Performance Analysis Using LLM](https://github.com/user-attachments/assets/154492ec-7b85-41fd-a846-a154d58a5d0f)

---
# -Sales-Team-Per-formance-Analysis-Using-LLM
Backend Development Exercise: Sales Team Performance Analysis Using LLM

**Ensure these Libraries**
pip install fastapi uvicorn pandas huggingface-hub

**Sales Team Performance Analysis API**
This project is a backend system for analyzing sales performance using a Large Language Model (LLM) integrated via the Hugging Face API. The system processes sales data and provides feedback on both individual sales representatives and the sales team as a whole.

**Features**
Upload Sales Data: Supports uploading sales data in CSV or JSON format.
Individual Sales Rep Feedback: Get detailed performance analysis and feedback for a specific sales representative.
Overall Team Performance: Provides a summary of the entire sales team's performance.
Sales Trends and Forecasting: Analyzes sales trends over specified time periods (monthly or quarterly) and generates forecasts.

**Set Up Hugging Face API Key**
You need an API key from Hugging Face to generate insights using their LLMs. Get your API key from Hugging Face.

**API Endpoints**

**1. Upload Sales Data**
Endpoint: /upload-sales-data/
Method: POST
Description: Upload CSV or JSON sales data.

**2. Sales Representative Feedback**
Endpoint: /sales-rep-feedback/{rep_id}
Method: GET
Description: Get performance feedback for a specific sales representative.

**3. Team Performance**
Endpoint: /team-performance
Method: GET
Description: Get feedback on overall team performance.
4. Performance Trends
Endpoint: /performance-trends
Method: GET
Description: Analyze trends and provide sales forecasts.
