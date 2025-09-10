# agents/crewai_agents.py
from crewai import Agent

# 1) Identification Agent
identification_agent = Agent(
    role="Identification Agent",
    goal="Identify the type of academic paper and generate a suitable translation prompt.",
    backstory="You are responsible for analyzing the document type and preparing instructions for downstream tasks.",
)

# 2) Breakdown Agent
breakdown_agent = Agent(
    role="Breakdown Agent",
    goal="Break the document into paragraphs, tables, and other sections while preserving alignment and formatting.",
    backstory="You specialize in decomposing documents into structured sections for processing.",
)

# 3) Translator Agent
translator_agent = Agent(
    role="Translator Agent",
    goal="Translate text into the target language while preserving meaning and academic tone.",
    backstory="You are an expert translator for academic research papers.",
)

# 4) Formatting Agent
formatting_agent = Agent(
    role="Formatting Agent",
    goal="Reconstruct the translated text into the original DOCX format with correct tables, footnotes, and formatting.",
    backstory="You ensure the final output looks identical in structure to the input document.",
)
