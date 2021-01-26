from poetry_demo import wikipedia

import pytest


languages = ["en", "de"]


@pytest.mark.parametrize("langs", languages)
def test_random_page_uses_given_language(langs):
    json = wikipedia.get_random_page(language=langs).json()
    assert json["lang"] == langs
