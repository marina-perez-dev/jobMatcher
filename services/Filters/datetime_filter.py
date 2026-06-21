from datetime import datetime

def filter_by_date_time(jobs):
    jobs.sort(
        key=lambda job: datetime.fromisoformat(
            job.get("dateActualisation", "").replace("Z", "+00:00")
        ) if job.get("dateActualisation") else datetime.min,
        reverse=True
    )