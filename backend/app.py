from flask import Flask, request, jsonify
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

app = Flask(__name__)

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
    # Implement logic to send reminder (e.g., email, push notification)
    print(f"Reminder: {reminder}")


@app.route('/api/medication-reminder', methods=['POST'])
def set_reminder():
    data = request.json
    reminder_time = datetime.datetime.strptime(
        data['time'], '%Y-%m-%d %H:%M:%S')
    scheduler.add_job(send_reminder, 'date',
                      run_date=reminder_time, args=[data])
    collection.insert_one(data)
    return jsonify({"message": "Reminder set successfully!"}), 201


if __name__ == '__main__':
    app.run(debug=True)
