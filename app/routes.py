from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the data here
    response = {"status": "success", "message": "Webhook received"}
    return jsonify(response)
