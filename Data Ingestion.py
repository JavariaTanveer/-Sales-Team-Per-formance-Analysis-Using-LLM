from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

# Global variable to store sales data
sales_data = pd.DataFrame()

@app.post("/api/upload_sales_data")
async def upload_sales_data(file: UploadFile):
    global sales_data
    if file.filename.endswith('.csv'):
        sales_data = pd.read_csv(file.file)
    elif file.filename.endswith('.json'):
        sales_data = pd.read_json(file.file)
    else:
        return {"error": "Unsupported file format. Please upload a CSV or JSON file."}

    return {"message": "Sales data uploaded successfully", "data_preview": sales_data.head().to_dict()}
