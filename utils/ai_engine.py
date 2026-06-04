
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_research_paper(topic, keywords):

    prompt = f"""
    Generate a short academic research paper.

    Topic: {topic}

    Keywords: {keywords}

    Include:
    1. Abstract
    2. Introduction
    3. Methodology
    4. Conclusion

    Keep response under 500 words.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Generation Error: {str(e)}"
