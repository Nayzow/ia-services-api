import speech_recognition as sr


class AudioService:
    recognizer = sr.Recognizer()

    @staticmethod
    def text_from_audio(file):
        with sr.AudioFile(file.file) as source:
            audio_data = AudioService.recognizer.record(source)
            return AudioService.recognizer.recognize_google(audio_data, language="fr-FR")
