from marshmallow import Schema, fields, validate

class LogSchema(Schema):
    log_level = fields.Str(required=True, validate=validate.OneOf(['INFO', 'ERROR', 'WARNING']))
    message = fields.Str(required=True)
    service_name = fields.Str(required=True)
    user_id = fields.Str(required=True)
    request_id = fields.Str(required=True)
    ip_address = fields.Str(required=True)
