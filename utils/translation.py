from deep_translator import GoogleTranslator

def google_translate(text, target_lang="fr"):
    """
    Translate text using GoogleTranslator (deep-translator).
    Default target language = French ("fr").
    """
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception as e:
        print(f"⚠️ Translation failed: {e}")
        return text
