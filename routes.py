from flask import Flask, request, jsonify, make_response, Blueprint
from dnn_model import predict_week

routing_system = Blueprint('routing_system', __name__)


@routing_system.route('/predict', methods=['POST'])
def my_prediction():
    request_data = request.get_json()
    groceries_data = request_data['groceries_data']
    prediction = predict_week(groceries_data)
    response_data = {
        '5th_week': prediction,
        'status': 'success'
    }

    response = make_response(jsonify(response_data))
    response.status_code = 200
    return response


@routing_system.route('/api', methods=['POST'])
def my_api():
    request_data = request.get_json()
    name = request_data['name']
    age = request_data['age']
    response_data = {
        'message': f'Hello, {name}! You are {age} years old.',
        'status': 'success'
    }

    response = make_response(jsonify(response_data))
    response.status_code = 200
    return response

    # return jsonify(response)
    # return jsonify({'message': 'Success'}), 200


# Error handler for 404 Not Found errors
@routing_system.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Endpoint not found'}), 404


# Error handler for 500 Internal server error
@routing_system.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': 'Internal server error'}), 500
