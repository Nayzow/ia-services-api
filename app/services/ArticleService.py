import re

from app.services.OpenAiService import OpenAiService


class ArticleService:
    @staticmethod
    def get_sub_themes(title):
        prompt = "écris un sommaire de présentation pour un article sur le theme de : '" + title + "' sous forme de liste avec des '-'"
        return re.findall(r"-(.*)", OpenAiService.text_from_prompt(prompt))

    @staticmethod
    def article_from_title(title):
        content = title + "\n"
        for sub_theme in ArticleService.get_sub_themes(title):
            content += sub_theme
            prompt = "écris un paragraphe de 125 mots pour un article sur le theme de '" + sub_theme + "' en français et optimisé pour le référencement web."
            content += OpenAiService.text_from_prompt(prompt) + "\n"
        return content

    @staticmethod
    def article_html_from_title(title):
        content = "<h1>" + title + "</h1> \n"
        for sub_theme in ArticleService.get_sub_themes(title):
            content += ("<h2>" + sub_theme + "</h2>") + "\n"
            prompt = "écris un paragraphe de 125 mots pour un article sur le theme " + sub_theme + " en français et optimisé pour le référencement web."
            content += ("<p>" + OpenAiService.text_from_prompt(prompt) + "</p>") + "\n"
        return content

    @staticmethod
    def article_markdown_from_title(title):
        content = "#" + title
        for under_theme in ArticleService.get_sub_themes(title):
            content += ("## " + under_theme)
            content += "\n"
            prompt = "écris un paragraphe de 125 mots pour un article sur le theme " + under_theme + " en français et optimisé pour le référencement web."
            content += OpenAiService.text_from_prompt(prompt) + "\n"
        return content
