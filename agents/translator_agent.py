from deep_translator import GoogleTranslator

def translate_paragraphs(sections, target_lang="fr"):
    """
    Translate a list of sections (dicts with 'type' + 'content') using GoogleTranslator.
    """
    translator = GoogleTranslator(source="auto", target=target_lang)
    translated_sections = []

    print(f"🔎 Translator received {len(sections)} items")

    for i, section in enumerate(sections, 1):
        text = section.get("content", "").strip()

        if not text:
            translated_sections.append(section)
            continue

        try:
            translated_text = translator.translate(text)
            print(f"[{i}] ✅ '{text[:50]}...' -> '{translated_text[:50]}...'")
            translated_sections.append({
                "type": section["type"],
                "content": translated_text
            })
        except Exception as e:
            print(f"[{i}] ❌ Translation failed: {e}")
            translated_sections.append(section)

    return translated_sections
