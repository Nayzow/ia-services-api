import re
from typing import Union

from app.models.Article import Article
from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class ArticleService:
    @staticmethod
    def get_sub_themes(title: str) -> Union[list[str], str]:
        try:
            prompt = "Tu es un rédacteur SEO depuis 20 ans, génère un sommaire de présentation pour un article sur le " \
                     "theme de : '" + title + "' sous forme de liste avec des '-'"
            return re.findall(r"-(.*)", OpenAiService.find_output_prompt_by_prompt(prompt))

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_article_by_title(title: str) -> Union[Article, str]:
        try:
            content = title + "\n"
            for sub_theme in ArticleService.get_sub_themes(title):
                content += sub_theme
                prompt = "Tu es un rédacteur SEO depuis 20 ans, génère un paragraphe de 125 mots pour un article sur " \
                         "le theme de '" + sub_theme + "' en français et optimisé pour le référencement web."
                content += OpenAiService.find_output_prompt_by_prompt(prompt) + "\n"
            return Article(title, content)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_article_html_by_title(title: str) -> Union[Article, str]:
        try:
            content = "<h1>" + title + "</h1> \n"
            for sub_theme in ArticleService.get_sub_themes(title):
                content += ("<h2>" + sub_theme + "</h2>") + "\n"
                prompt = "écris un paragraphe de 125 mots pour un article sur le theme " + sub_theme + " en français et optimisé pour le référencement web."
                content += ("<p>" + OpenAiService.find_output_prompt_by_prompt(prompt) + "</p>") + "\n"
            return Article(title, content)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_article_markdown_by_title(title: str) -> Union[Article, str]:
        try:
            content = "#" + title
            for under_theme in ArticleService.get_sub_themes(title):
                content += ("## " + under_theme)
                content += "\n"
                prompt = "écris un paragraphe de 125 mots pour un article sur le theme " + under_theme + " en français et optimisé pour le référencement web."
                content += OpenAiService.find_output_prompt_by_prompt(prompt) + "\n"
            return Article(title, content)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
