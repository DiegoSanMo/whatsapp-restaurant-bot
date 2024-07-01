from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    app.config['WHATSAPP_API_URL'] = os.getenv('WHATSAPP_API_URL')
    app.config['WHATSAPP_API_TOKEN'] = os.getenv('WHATSAPP_API_TOKEN')
    app.config['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

    from .routes import main
    app.register_blueprint(main)

    return app
