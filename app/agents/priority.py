def detect_priority(task: str):
    task = task.lower()

    if "urgent" in task or "asap" in task:
        return "high"
    elif "soon" in task:
        return "medium"
    return "low"