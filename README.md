# -Sales-Team-Per-formance-Analysis-Using-LLM
Backend Development Exercise: Sales Team Performance Analysis Using LLM

#Ensure these Libraries
pip install fastapi uvicorn pandas huggingface-hub
-----HUGGINGFACE_API_KEY----

# Replace with your Hugging Face API key
HUGGING_FACE_API_KEY = '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'

# Global variable to hold the sales data
sales_data = pd.DataFrame()

# Function to query the Hugging Face model for insights
def get_llm_insights_hf(prompt):
    url = "https://api-inference.huggingface.co/models/gpt2"  # You can change to other models
    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_API_KEY}"
    }
    
    data = {
        "inputs": prompt
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result[0]['generated_text']
    else:
        return "Error in Hugging Face API request: " + response.text

# Endpoint to upload sales data (CSV or JSON)
@app.post("/upload-sales-data/")
async def upload_sales_data(file: UploadFile):
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file.file)
    elif file.filename.endswith('.json'):
        df = pd.read_json(file.file)
    else:
        return {"error": "Unsupported file format"}

    global sales_data
    sales_data = df

    return {"message": "Data uploaded successfully", "data_preview": df.head().to_dict()}

# Endpoint to get feedback on sales rep performance
@app.get("/sales-rep-feedback/{rep_id}")
async def sales_rep_feedback(rep_id: str):
    # Filter the sales data for the specific sales rep
    rep_data = sales_data[sales_data['sales_rep_id'] == rep_id]

    if rep_data.empty:
        return {"error": "Sales representative not found"}

    # Generate prompt for LLM
    prompt = f"Provide feedback on the sales performance for representative {rep_id} based on the following data: {rep_data.to_dict()}"

    # Get LLM insights from Hugging Face
    feedback = get_llm_insights_hf(prompt)

    return {"sales_rep_id": rep_id, "feedback": feedback}

**API Endpoints**
1. Upload Sales Data
Endpoint: /upload-sales-data/
Method: POST
Description: Upload CSV or JSON sales data.
2. Sales Representative Feedback
Endpoint: /sales-rep-feedback/{rep_id}
Method: GET
Description: Get performance feedback for a specific sales representative.
3. Team Performance
Endpoint: /team-performance
Method: GET
Description: Get feedback on overall team performance.
4. Performance Trends
Endpoint: /performance-trends
Method: GET
Description: Analyze trends and provide sales forecasts.

