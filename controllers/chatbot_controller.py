from flask import Blueprint, request, jsonify
from chatbot.services.chatbot_service import ChatbotService

# Create a Blueprint for chatbot routes
chatbot_bp = Blueprint('chatbot', __name__)
chatbot_service = ChatbotService()

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """
    Accepts a POST request with JSON containing 'query'.
    Returns the chatbot response.
    """
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    # Get response from the service
    response = chatbot_service.get_response(user_query)
    return jsonify({"response": response})
