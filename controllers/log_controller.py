import uuid
from pymongo import MongoClient
from datetime import datetime
from flask import request
from config import Config
import pytz
import requests

client = MongoClient(Config.MONGO_URI)

# name ng database sa mongodb
db = client.logs_service 

# name ng collection inside the database
logs = db.logs  

def get_ip_address():
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.getlist('X-Forwarded-For')[0]
    else:
        ip = request.remote_addr

    return ip

def log_event(log_level, message, service_name, user_id=None, request_id=None, ip_address=None):
    try:
        if not request_id:
            request_id = str(uuid.uuid4())

        if not ip_address:
            ip_address = get_ip_address()

        # Handle the timezone
        user_timezone = request.headers.get('X-User-Timezone', 'UTC')
        user_tz = pytz.timezone(user_timezone)
        timestamp = datetime.now(user_tz).strftime('%Y-%m-%d %H:%M:%S')

        log_entry = {
            'log_level': log_level,
            'message': message,
            'service_name': service_name,
            'user_id': user_id,
            'request_id': request_id,
            'ip_address': ip_address,
            'timestamp': timestamp
        }

        logs.insert_one(log_entry)
        return {'status': 'success'}
    
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def get_logs():
    all_logs = list(logs.find())
    for log in all_logs:
        log['_id'] = str(log['_id'])
    return all_logs
