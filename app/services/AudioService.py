import base64
from typing import Dict, Union, Any, List, Tuple

import speech_recognition as sr
from google.cloud import texttospeech
import os

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
    def find_text_by_audio(file) -> Union[str, dict[str]]:
        try:
            with sr.AudioFile(file.file) as source:
                audio_data = AudioService.recognizer.record(source)
                return AudioService.recognizer.recognize_google(audio_data, language="fr-FR")

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_audio_bytes_by_prompt(prompt: str) -> Union[dict[str, str], str]:
        try:
            synthesis_input = texttospeech.SynthesisInput(text=prompt)
            response = AudioService.client.synthesize_speech(
                input=synthesis_input,
                voice=AudioService.voice,
                audio_config=AudioService.audio_config
            )
            audio_content = base64.b64encode(response.audio_content).decode('utf-8')
            return {"audio_content": audio_content}

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)

    @staticmethod
    def find_audio_file_by_prompt(prompt: str):
        try:
            synthesis_input = texttospeech.SynthesisInput(prompt)
            response = AudioService.client.synthesize_speech(
                input=synthesis_input,
                voice=AudioService.voice,
                audio_config=AudioService.audio_config
            )

            filename = "app/resources/audio/output.wav"

            with open(filename, "wb") as file:
                file.write(response.audio_content)

        except Exception as e:
            return ExceptionUtil.handle_exceptions(e)
