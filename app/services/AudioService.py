import base64
import os
import speech_recognition as sr
from typing import Union
from google.cloud import texttospeech
from app.models.Audio import Audio
from app.utils.ExceptionUtil import ExceptionUtil


class AudioService:
    recognizer = sr.Recognizer()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app/resources/GoogleCloudAuthKey.json"
    client = texttospeech.TextToSpeechClient()
    voice = texttospeech.VoiceSelectionParams(
        language_code="fr-FR",
        name="fr-FR-Wavenet-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    @staticmethod
    def find_text_by_audio(file) -> Union[Audio, str]:
        try:
            with sr.AudioFile(file.file) as source:
                audio_data = AudioService.recognizer.record(source)
                response = AudioService.recognizer.recognize_google(audio_data, language="fr-FR")
                return response

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_audio_bytes_by_prompt(prompt: str) -> Union[Audio, str]:
        try:
            synthesis_input = texttospeech.SynthesisInput(text=prompt)
            response = AudioService.client.synthesize_speech(
                input=synthesis_input,
                voice=AudioService.voice,
                audio_config=AudioService.audio_config
            )
            response = base64.b64encode(response.audio_content).decode('utf-8')
            return Audio(response)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
