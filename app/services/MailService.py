from typing import Union
from app.models.Mail import Mail
from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class MailService:
    @staticmethod
    def find_positive_mail_response_by_prompt(prompt: str) -> Union[Mail, str]:
        try:
            request_prompt = "Génère une réponse affirmative à cet e-mail de manière professionnelle : " + prompt
            response = OpenAiService.find_output_prompt_by_prompt(request_prompt)
            object_prompt = "Génère un objet pour ce mail : " + response
            object_response = OpenAiService.find_output_prompt_by_prompt(object_prompt)
            return Mail(object_response, response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_negative_mail_response_by_prompt(prompt: str) -> Union[Mail, str]:
        try:
            request_prompt = "Génère une réponse négative à cet e-mail de manière professionnelle : " + prompt
            response = OpenAiService.find_output_prompt_by_prompt(request_prompt)
            object_prompt = "Génère un objet pour ce mail : " + response
            object_response = OpenAiService.find_output_prompt_by_prompt(object_prompt)
            return Mail(object_response, response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
