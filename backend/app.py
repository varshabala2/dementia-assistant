from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
import datetime


app = Flask(__name__)
CORS(app)  # Allow requests from frontend


# MongoDB connection
uri = "your-connection-string"
client = MongoClient(uri)
db = client.get_database('your-database-name')
collection = db.get_collection('your-collection-name')

# Scheduler setup
scheduler = BackgroundScheduler()
scheduler.start()

# Function to send reminders


def send_reminder(reminder):
    print(f"Reminder: {reminder}")


@app.route('/api/medication-reminder', methods=['POST'])
def set_reminder():
    data = request.json
    try:
        reminder_time = datetime.datetime.strptime(
            data['time'], '%Y-%m-%d %H:%M:%S')
        scheduler.add_job(send_reminder, 'date',
                          run_date=reminder_time, args=[data])
        collection.insert_one(data)
        return jsonify({"message": "Reminder set successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Test route


@app.route('/api/test', methods=['GET'])
def test_connection():
    return jsonify({"message": "Connection successful!"})


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
