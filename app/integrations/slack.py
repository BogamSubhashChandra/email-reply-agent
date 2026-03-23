import os
import requests

WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_to_slack(tasks):
    if not WEBHOOK:
        return

    message = "\n".join(tasks)

    requests.post(WEBHOOK, json={"text": f"Tasks:\n{message}"})