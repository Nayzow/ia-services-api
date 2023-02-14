from fastapi import FastAPI, UploadFile, File, HTTPException
from requests import RequestException

from app.services.ArticleService import ArticleService
from app.services.AssistantService import AssistantService
from app.services.AudioService import AudioService
from app.services.LetterService import LetterService
from app.services.OpenAiService import OpenAiService

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": f"HTTP Exception: {exc.detail}"}


@app.exception_handler(RequestException)
async def request_exception_handler(request, exc):
    return {"error": f"Request Exception: {str(exc)}"}


@app.get("/prompt/{prompt}")
async def text(prompt):
    return OpenAiService.text_from_prompt(prompt)


@app.get("/image/{prompt}")
async def image(prompt):
    return OpenAiService.image_from_prompt(prompt)


@app.get("/article/{title}")
async def article(title):
    return ArticleService.article_from_title(title)


@app.get("/article/html/{title}")
async def article_html(title):
    return ArticleService.article_html_from_title(title)


@app.get("/article/markdown/{title}")
async def article_markdown(title):
    return ArticleService.article_markdown_from_title(title)


@app.get("/letter/{company}")
async def letter(company):
    return LetterService.letter_for_company(company)


@app.post("/audio/")
async def audio(file: UploadFile = File(...)):
    return AudioService.text_from_audio(file)


@app.post("/assistant/")
async def assistant(file: UploadFile = File(...)):
    return AssistantService.response_from_audio(file)
