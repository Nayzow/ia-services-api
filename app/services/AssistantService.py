from app.services.AudioService import AudioService
from app.services.OpenAiService import OpenAiService


class AssistantService:
    @staticmethod
    def response_from_audio(file):
        return OpenAiService.text_from_prompt(AudioService.text_from_audio(file))
