from fastapi import requests


class ErrorUtil:
    @staticmethod
    def handle_request_errors(response):
        try:
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as errh:
            return {"error": f"HTTP error: {errh}"}
        except requests.exceptions.ConnectionError as errc:
            return {"error": f"Connection error: {errc}"}
        except requests.exceptions.Timeout as errt:
            return {"error": f"Timeout error: {errt}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"Unknown error: {err}"}
