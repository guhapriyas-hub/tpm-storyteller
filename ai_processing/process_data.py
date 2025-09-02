def compute_summary(df):
    total_tasks = len(df)
    open_tasks = df[df['status'] != 'Done'].shape[0]
    summary = {
        "Total Tasks": total_tasks,
        "Open Tasks": open_tasks,
        "Top 5 Tasks": df.head(5).to_dict(orient="records")
    }
    return summary