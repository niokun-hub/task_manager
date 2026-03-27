def validate_stats(status: str) -> bool:
    return status in ["new", "in_progress", "done"]