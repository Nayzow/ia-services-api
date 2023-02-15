from app.services.AudioService import AudioService
from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class AssistantService:
    @staticmethod
    def find_output_prompt_by_audio_input(file):
        try:
            return OpenAiService.find_output_prompt_by_prompt(AudioService.find_text_by_audio(file))

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_audio_output_by_audio_input(file):
        try:
            return AudioService.find_audio_bytes_by_prompt(
                OpenAiService.find_output_prompt_by_prompt(
                    AudioService.find_text_by_audio(file)
                )
            )

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
