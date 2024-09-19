#Individual Sales Representative Performance Analysis

@app.get("/api/rep_performance")
async def rep_performance(rep_id: str):
    # Filter data for the specific representative
    rep_data = sales_data[sales_data['rep_id'] == rep_id]
    
    if rep_data.empty:
        return {"error": "Sales representative not found"}

    # Generate prompt for LLM
    prompt = f"Analyze the performance of sales representative {rep_id} based on the following data: {rep_data.to_dict()}"

    # Get feedback from Hugging Face LLM
    feedback = get_llm_insights(prompt)

    return {"sales_rep_id": rep_id, "feedback": feedback}


# Overall Sales Team Performance Summary
@app.get("/api/team_performance")
async def team_performance():
    # Summarize sales data for all representatives
    team_summary = sales_data.groupby('rep_id').sum()

    # Generate prompt for LLM
    prompt = f"Provide a performance summary for the sales team based on the following data: {team_summary.to_dict()}"

    # Get feedback from Hugging Face LLM
    feedback = get_llm_insights(prompt)

    return {"team_performance_feedback": feedback}

#. Sales Performance Trends and Forecasting
@app.get("/api/performance_trends")
async def performance_trends(time_period: str):
    # Group by time period and calculate sales trends
    if time_period == 'monthly':
        trend_data = sales_data.groupby(sales_data['date'].dt.to_period('M')).sum()
    elif time_period == 'quarterly':
        trend_data = sales_data.groupby(sales_data['date'].dt.to_period('Q')).sum()
    else:
        return {"error": "Unsupported time period. Please use 'monthly' or 'quarterly'."}

    # Generate prompt for LLM
    prompt = f"Analyze the sales trends for the period {time_period} based on the following data: {trend_data.to_dict()}"

    # Get feedback and forecast from Hugging Face LLM
    feedback = get_llm_insights(prompt)

    return {"performance_trends_feedback": feedback}
