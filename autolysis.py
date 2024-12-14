import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
from dotenv import load_dotenv
load_dotenv()
AIPROXY_TOKEN = os.environ["AIPROXY_TOKEN"]
if not AIPROXY_TOKEN:
    raise EnvironmentError("AIPROXY_TOKEN environment variable not set.")

PROXY_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {AIPROXY_TOKEN}",
    "Content-Type": "application/json"
}