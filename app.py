import json
import requests
from flask import Flask, request

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1440195595665936466/WI33qbwOy1NTsez526hB343cgjWFX0mlEv1HB2HquaKYajSJjjbN7tGKmnLUuQ0SgNmO"

@app.route("/tradingview-webhook", methods=["POST"])
def tradingview_webhook():
    data = json.loads(request.data.decode("utf-8"))
    
    message = f"""
🚨 **Ross-Style Momentum Alert**

**Symbol:** `{data.get("symbol")}`
**Price:** `{data.get("price")}`
**Time:** {data.get("time")}

**Stats:**
• Range: `{data.get("day_low")} → {data.get("day_high")}`
• Volume: `{data.get("volume")}`

_Open in Webull and confirm tape._
"""

    requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
