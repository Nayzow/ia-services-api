from fastapi import FastAPI, UploadFile, File, HTTPException
from requests import RequestException
from app.services.MailService import MailService
from app.services.CheatsheetService import CheatsheetService
from app.services.ArticleService import ArticleService
from app.services.AssistantService import AssistantService
from app.services.AudioService import AudioService
from app.services.LetterService import LetterService
from app.services.OpenAiService import OpenAiService
from app.services.PromptService import PromptService
from app.services.TranslationService import TranslationService

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": f"HTTP Exception: {exc.detail}"}


@app.exception_handler(RequestException)
async def request_exception_handler(request, exc):
    return {"error": f"Request Exception: {str(exc)}"}


@app.get("/prompt/{prompt}")
async def find_output_prompt_by_prompt(prompt: str):
    return PromptService.find_output_prompt_by_prompt(prompt)


@app.get("/image/{prompt}")
async def find_image_by_prompt(prompt: str):
    return OpenAiService.find_image_by_prompt(prompt)


@app.get("/article/{title}")
async def find_article_by_title(title: str):
    return ArticleService.find_article_by_title(title)


@app.get("/article/html/{title}")
async def find_article_html_by_title(title: str):
    return ArticleService.find_article_html_by_title(title)


@app.get("/article/markdown/{title}")
async def find_article_markdown_by_title(title: str):
    return ArticleService.find_article_markdown_by_title(title)


@app.get("/translation/{langage}/{prompt}")
async def find_translation_by_langage_and_prompt(langage: str, prompt: str):
    return TranslationService.find_translation_by_langage_and_prompt(langage, prompt)


@app.get("/mail/positive/{prompt}")
async def find_positive_mail_response_by_prompt(prompt: str):
    return MailService.find_positive_mail_response_by_prompt(prompt)


@app.get("/mail/negative/{prompt}")
async def find_positive_mail_response_by_prompt(prompt: str):
    return MailService.find_negative_mail_response_by_prompt(prompt)


@app.get("/cheatsheet/{subject}")
async def find_cheatsheet_by_subject(subject: str):
    return CheatsheetService.find_cheatsheet_by_subject(subject)


@app.get("/cheatsheet/markdown/{subject}")
async def find_cheatsheet_markdown_by_subject(subject: str):
    return CheatsheetService.find_cheatsheet_markdown_by_subject(subject)


@app.get("/letter/{company}")
async def find_letter_by_company(company: str):
    return LetterService.find_letter_by_company(company)


@app.get("/audio/output/{prompt}")
async def find_audio_bytes_by_prompt(prompt: str):
    return AudioService.find_audio_bytes_by_prompt(prompt)


@app.post("/audio/input")
async def find_text_from_audio(file: UploadFile = File(...)):
    return AudioService.find_text_by_audio(file)


@app.post("/assistant/text")
async def find_output_prompt_by_audio_input(file: UploadFile = File(...)):
    return AssistantService.find_output_prompt_by_audio_input(file)


@app.post("/assistant/vocal")
async def find_audio_output_bytes_by_audio_input(file: UploadFile = File(...)):
    return AssistantService.find_audio_output_bytes_by_audio_input(file)
