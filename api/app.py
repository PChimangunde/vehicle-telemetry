from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/vehicle")
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)
COL = mongo.db.telemetry

# POST telemetry data
@app.route('/telemetry', methods=['POST'])
def receive_telemetry():
    payload = request.get_json(force=True)
    payload['received_at'] = datetime.utcnow()
    COL.insert_one(payload)
    return jsonify({"status": "ok"}), 201

# GET telemetry data
@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    limit = int(request.args.get('limit', 50))
    docs = COL.find({}, {'_id': False}).sort('received_at', -1).limit(limit)
    return jsonify({'data': list(docs)})

# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
