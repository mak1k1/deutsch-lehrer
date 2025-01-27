import re
import json
from app import client

def generate_lesson_with_gpt(level, theme):
    # Define the chat messages
    messages = [
        {"role": "system", "content": "You are a German language tutor."},
        {"role": "user", "content": f"""
            Create a lesson for a student at level {level} about the theme '{theme}'. 
            Provide:
            - A list of 5 vocabulary words with translations.
            - Two grammar rules.
            Output the result as plain JSON without any Markdown formatting or additional text.
            Use this format:
            {{
                "vocabulary": {{
                    "word1": "translation1",
                    "word2": "translation2",
                    "word3": "translation3",
                    "word4": "translation4",
                    "word5": "translation5"
                }},
                "grammar": [
                    "Grammar rule 1",
                    "Grammar rule 2"
                ]
            }}.
        """}
    ]

    try:
        # Call the OpenAI chat completion API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
            response_format={"type": "json_object"}
        )

        # Extract the response content
        raw_text = response.choices[0].message.content

        # Parse the response as JSON
        try:
            lesson_content = json.loads(raw_text)
            return lesson_content
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse GPT response as JSON: {e}\nRaw response:\n{raw_text}")

    except Exception as e:
        raise RuntimeError(f"DeepSeek API error: {e}")