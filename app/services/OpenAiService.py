import openai


class OpenAiService:
    openai.api_key = "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"

    @staticmethod
    def text_from_prompt(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response["choices"][0]["text"]

    @staticmethod
    def image_from_prompt(prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=2,
            size="1024x1024"
        )
        return response
