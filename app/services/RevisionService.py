from app.services.OpenAiService import OpenAiService


class RevisionService:
    @staticmethod
    def find_revision_by_subject(subject):
        prompt = "Génère une fiche de révision sur le sujet de " + subject
        return OpenAiService.find_output_prompt_by_prompt(prompt)

    @staticmethod
    def find_revision_markdown_by_subject(subject):
        prompt = "Génère une fiche de révision sur le sujet de " + subject + "au format markdown"
        return OpenAiService.find_output_prompt_by_prompt(prompt)
