from fastapi import requests


class ExceptionUtil:
    @staticmethod
    def handle_exceptions(e: Exception) -> str:
        return f"An error occurred: {str(e)}"
