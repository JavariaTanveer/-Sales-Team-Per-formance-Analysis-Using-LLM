from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import json
import os
from huggingface_hub import InferenceApi

app = FastAPI()

#HUGGINGFACE_API_KEY= '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' set up in Os

# Hugging Face API setup
api_key = os.getenv("HUGGINGFACE_API_KEY")
model_id = "gpt2"  # Choose the appropriate model, such as GPT-2.
hf_api = InferenceApi(repo_id=model_id, token=api_key)


@app.post("/api/upload_sales_data/")
async def upload_sales_data(file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        try:
            df = pd.read_csv(file.file)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")
    elif file.filename.endswith(".json"):
        try:
            data = json.load(file.file)
            df = pd.DataFrame(data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading JSON: {str(e)}")
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Only CSV and JSON are allowed.")

    # Data validation steps here
    return {"message": "Data successfully uploaded", "data": df.to_dict()}


@app.post("/api/sales_rep_feedback/")
async def sales_rep_feedback(sales_rep_id: str, data: list):
    # Filter data for the specific sales rep
    sales_rep_data = [entry for entry in data if entry['sales_rep_id'] == sales_rep_id]
    
    if not sales_rep_data:
        raise HTTPException(status_code=404, detail="No data found for this sales rep.")

    # Construct the input prompt for the Hugging Face GPT model
    prompt = f"Analyze the performance of sales representative {sales_rep_id} based on the following data: {sales_rep_data}. Provide feedback."

    # Send request to Hugging Face API
    response = await hf_api(prompt)

    return {"sales_rep_id": sales_rep_id, "feedback": response.get('generated_text', '')}


@app.post("/api/team_performance/")
async def team_performance(data: list):
    prompt = f"Analyze the team's performance based on the following sales data: {data}. Provide feedback and insights."

    # Send request to Hugging Face API
    response = await hf_api(prompt)

    return {"team_feedback": response.get('generated_text', '')}


@app.post("/api/sales_trends/")
async def sales_trends(data: list):
    prompt = f"Analyze the sales trends and provide a forecast based on the following sales data: {data}."

    # Send request to Hugging Face API
    response = await hf_api(prompt)

    return {"sales_trends_forecast": response.get('generated_text', '')}
