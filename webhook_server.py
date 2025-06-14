from flask import Flask, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    logging.info(f"Webhook received: {data}")
    symbol = data.get("symbol", "SOL/USDT")
    event = data.get("event", "")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"ALERT: {symbol} | {event} | {time}"
    logging.info(message)
    return jsonify({"status": "ok", "message": message}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# added webhook server
