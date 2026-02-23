import google.generativeai as genai
from app.config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE, MAX_OUTPUT_TOKENS


class GeminiClient:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel(
            MODEL_NAME,
            generation_config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
            },
        )

        self.chat = self.model.start_chat(history=[])

    def send_message(self, message: str) -> str:
        response = self.chat.send_message(message)
        return response.text