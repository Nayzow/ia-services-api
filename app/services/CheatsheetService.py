from typing import Union

from app.models.Cheatsheet import Cheatsheet
from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class CheatsheetService:
    @staticmethod
    def find_cheatsheet_by_subject(subject: str) -> Union[Cheatsheet, str]:
        try:
            prompt = "Génère une fiche de révision sur le sujet de " + subject
            response = OpenAiService.find_output_prompt_by_prompt(prompt)
            return Cheatsheet(subject, response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_cheatsheet_markdown_by_subject(subject: str) -> Union[Cheatsheet, str]:
        try:
            prompt = "Génère une fiche de révision sur le sujet de " + subject + "au format markdown"
            response = OpenAiService.find_output_prompt_by_prompt(prompt)
            return Cheatsheet(subject, response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
