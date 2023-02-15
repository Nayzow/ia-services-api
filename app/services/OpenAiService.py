from ctypes import Union
from typing import Union, Any

import openai

from app.utils.ExceptionUtil import ExceptionUtil


class OpenAiService:
    openai.api_key = "[VOTRE_CLE]"

    @staticmethod
    def find_output_prompt_by_prompt(prompt: str) -> Union[str, dict[str]]:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2000,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response["choices"][0]["text"]

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_image_by_prompt(prompt: str):
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=2,
                size="1024x1024"
            )
            return response

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

