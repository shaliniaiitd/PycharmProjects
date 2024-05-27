#https://platform.openai.com/docs/api-reference
from openai import AzureOpenAI
import json
import os
from dotenv import load_dotenv
from src.constants import Config

from src.prompts import PROMPTS

# Load .env file

load_dotenv()


class OpenAIClient:
    def __init__(self, text, type):
        self.text = text
        self.type = type
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=Config.AZURE_OPENAI_API_VERSION,
            azure_endpoint=Config.AZURE_OPENAI_ENDPOINT,
        )

    def make_query(self, text, type):
        response = self.client.chat.completions.create(
            model=Config.AZURE_CHAT_DEPLOYMENT_NAME,
            temperature=Config.TEMPERATURE,
            top_p=Config.TOP_P,
            frequency_penalty=Config.FREQUENCY_PENALTY,
            presence_penalty=Config.PRESENCE_PENALTY,
            messages=[
                {"role": "system", "content": PROMPTS[type]},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    def process_text(self) -> object:
        if self.type == "short":
            response = self.make_query(self.text, "short")

        elif self.type == "original":
            response = self.make_query(self.text, "original")

        elif self.type == "originalAnd2":
            response = self.make_query(self.text, "original")
            response = self.make_query(response, "originalAnd2")

        json_object = json.loads(response)

        return json_object