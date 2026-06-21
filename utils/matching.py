# Logique de croisement

def match_jobs_events(jobs, events):
    
    results = []

    for job in jobs:

        for event in events:
            if job["company"].lower() in event["company"].lower():
                results.append({
                    "company": job["company"],
                    "job": job["title"],
                    "event": event["name"],
                    "date": event["date"]
                })

    return results

