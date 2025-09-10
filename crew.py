def run_pipeline(input_file, output_file, target_lang):
    import docx
    from agents.breakdown_agent import breakdown_doc
    from agents.identification_agent import identify_doc
    from agents.translator_agent import translate_paragraphs
    from agents.formatting_agent import rebuild_doc

    print(f"📂 Loading {input_file}...")
    doc = docx.Document(input_file)

    # Step 1: Identification
    doc_type = identify_doc(doc)
    print(f"🕵️ Identified document type: {doc_type}")

    # Step 2: Breakdown
    sections = breakdown_doc(doc)

    # Step 3: Translation
    translated_sections = translate_paragraphs(sections, target_lang)

    # Step 4: Formatting
    rebuild_doc(translated_sections, output_file)

    print(f"✅ Translation completed. Saved at: {output_file}")
