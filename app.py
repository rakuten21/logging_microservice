from flask import Flask
from blueprints.logging_service.log_routes import logging_service

app = Flask(__name__)
app.register_blueprint(logging_service, url_prefix='/api/logs')

if __name__ == '__main__':
    app.run(debug=True, port=5001)