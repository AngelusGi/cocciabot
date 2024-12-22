import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_success = load_dotenv()
        if not load_success:
            raise EnvironmentError("Failed to load .env file")
        
        self.bot_token = os.getenv("TG_BOT_TOKEN")
        self.bot_name = os.getenv("TG_BOT_NAME")
        
        if not self.bot_token:
            raise ValueError("Token is not provided")
        if not self.bot_name:
            raise ValueError("Bot name is not provided")
