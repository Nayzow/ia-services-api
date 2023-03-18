from typing import Union

from app.models.Letter import Letter
from app.services.OpenAiService import OpenAiService
from app.utils.ExceptionUtil import ExceptionUtil


class LetterService:
    @staticmethod
    def find_letter_by_company(company: str) -> Union[Letter, str]:
        try:
            name: str = "Thibault Tanguy"
            age: str = "24"
            job: str = "développeur"
            duration: str = "alternance"
            skills: str = "# Informations :" \
                          "- age : " + age + " ans" \
                                             "## Scolarité : " \
                                             "- Licence de psychologie (bac +3) " \
                                             "- 2ème année Ecole d'informatique (actuellement) " \
                                             "## Hard-skills : " \
                                             "- Anglais courant (Niveau B2+) " \
                                             "- Backend : " \
                                             "  - Conception et administration base de données MySQL & MariaDB " \
                                             "  - Conception d'API Java (familiarisé)" \
                                             "  - Langages : PHP, Java, Python, SQL, UML " \
                                             "  - Framework : Springboot (familiarisé)" \
                                             "- Front-End : " \
                                             "  - Conception d'interfaces web " \
                                             "  - Utilisation d'API avec Javascript" \
                                             "  - Langages : HTML, CSS, JavaScript, Bootstrap" \
                                             "  - Framework : Angular (familiarisé)" \
                                             "  - Réseaux & DevOps (amateur): " \
                                             "  - Mise en place de serveurs et de containers.  " \
                                             "  - Base de connaissances Azure Cloud, Docker, Docker compose. " \
                                             "Soft-skills : " \
                                             "  - Bienveillant, empathique, à l'écoute, curieux, autonome"

            prompt: str = "Génère une lettre de motivation de 700 mots avec la formule de politesse 'Madame, Monsieur," \
                          "' en français pour un poste de " + job + \
                          "en " + duration + \
                          " pour l'entreprise de services numérique " + company + \
                          ". Mentionne le nom de l'entreprise dans la lettre et signe au nom de +" + name + \
                          ". Mentionne l'intégralité de mes compétences, les voici : ' " + skills

            response = OpenAiService.find_output_prompt_by_prompt(prompt)

            return Letter(name, duration, response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
