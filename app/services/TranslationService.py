from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class TranslationService:
    @staticmethod
    def find_translation_by_langage_and_prompt(langage: str, prompt: str) -> str:
        try:
            request_prompt = "Traduit ce texte en " + langage + ": " + prompt
            return OpenAiService.find_output_prompt_by_prompt(request_prompt)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
