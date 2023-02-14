from app.services.OpenAiService import OpenAiService


class LetterService:
    @staticmethod
    def letter_for_company(company):
        name = "Thibault Tanguy"
        age = "24"
        job = "développeur"
        duration = "alternance"
        skills = "# Informations :" \
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

        prompt = "Ecris une lettre de motivation de 700 mots avec la formule de politesse 'Madame, Monsieur," \
                 "' en français pour un poste de " + job + \
                 "en " + duration + \
                 " pour l'entreprise de services numérique " + company + \
                 ". Mentionne le nom de l'entreprise dans la lettre et signe au nom de +" + name + \
                 ". Mentionne l'intégralité de mes compétences, les voici : ' " + skills

        return OpenAiService.text_from_prompt(prompt)
