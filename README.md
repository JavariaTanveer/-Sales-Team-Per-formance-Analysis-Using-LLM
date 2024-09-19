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

