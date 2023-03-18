from typing import Union

from app.models.Prompt import Prompt
from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class PromptService:
    @staticmethod
    def find_output_prompt_by_prompt(prompt: str) -> Union[Prompt, str]:
        try:
            response = OpenAiService.find_output_prompt_by_prompt(prompt)
            return Prompt(prompt, response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
