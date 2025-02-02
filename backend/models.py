def create_reminder(text, time):
    """Inserts a new reminder into MongoDB."""
    reminder = {
        "text": text,
        "time": time,
        "completed": False
    }
    return reminders_collection.insert_one(reminder)

def get_all_reminders():
    """Fetches all reminders from MongoDB."""
    return list(reminders_collection.find({}, {"_id": 0}))

def mark_reminder_completed(text):
    """Marks a reminder as completed."""
    reminders_collection.update_one({"text": text}, {"$set": {"completed": True}})
