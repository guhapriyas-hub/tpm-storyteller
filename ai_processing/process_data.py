def compute_summary(df):
    # Normalize column names: remove spaces and lowercase
    df.columns = df.columns.str.strip().str.lower()
    # Ensure required columns exists
    if 'status' not in df.columns:
        raise ValueError("Excel must have a 'Status' column")
    # Normalize status values for consistency
    df['status'] = df['status'].str.strip().str.lower()
    # Count total tasks
    total_tasks = len(df)
    # Count open tasks (anything not completed/done)
    open_tasks = df[~df['status'].isin(['completed', 'done'])].shape[0]
    # Top 5 tasks for display
    top_tasks = df.head(5).to_dict(orient="records")
    summary = {
        "Total Tasks": total_tasks,
        "Open Tasks": open_tasks,
        "Top 5 Tasks": top_tasks
    }
    return summary