from flask import Blueprint, request, jsonify, abort
from config import Config
from controllers.log_controller import log_event, get_logs
from utils.validation import LogSchema

logging_service = Blueprint('logging_service', __name__)

@logging_service.before_request
def check_api_key():
    api_key = request.headers.get('X-API-KEY')
    if not api_key or api_key != Config.API_KEY:
        abort(403, description='Forbidden: Invalid API Key')


@logging_service.route('/log', methods=['POST'])
def log_event_route():
    schema = LogSchema()
    data = schema.load(request.json)
    response = log_event(**data)

    return jsonify(response), 201

@logging_service.route('/logs', methods=['GET'])
def get_logs_route():
    logs = get_logs()
    return jsonify(logs), 200