# Initialize the Flask app package
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register controllers
    from .controllers.chatbot_controller import chatbot_bp
    app.register_blueprint(chatbot_bp, url_prefix='/api')

    return app
