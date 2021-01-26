from confidential import SecretsManager

import requests

confidential = SecretsManager(
    secrets_file=".confidential/secrets.json", region_name="us-west-1",
)


def get_random_page(language="en"):
    """Returns a requests response from Wikipedia"""
    url = confidential["WIKIPEDIA_URL"].format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response
    except requests.RequestException as error:
        message = str(error)
        raise message
