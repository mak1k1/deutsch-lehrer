import re
import json
from app import client

def generate_lesson_with_gpt(level, theme):
    messages = [
        {"role": "system", "content": "You are a German language tutor."},
        {"role": "user", "content": f"""
        Create a complete lesson for a German learner at level {level} on the theme '{theme}'. 
        The lesson must follow this exact JSON structure:
        {{
            "lesson": {{
                "level": "{level}",
                "theme": "{theme}",
                "vocabulary": [
                    {{
                        "word": "word1",
                        "translation": "translation1",
                        "example_sentence": "example sentence1"
                    }},
                    {{
                        "word": "word2",
                        "translation": "translation2",
                        "example_sentence": "example sentence2"
                    }}
                ],
                "grammar": [
                    {{
                        "rule": "Grammar rule 1",
                        "explanation": "Explanation of rule 1",
                        "example": "Example usage of rule 1"
                    }},
                    {{
                        "rule": "Grammar rule 2",
                        "explanation": "Explanation of rule 2",
                        "example": "Example usage of rule 2"
                    }}
                ],
                "assignments": [
                    {{
                        "type": "multiple_choice",
                        "question": "Question text",
                        "options": ["Option 1", "Option 2", "Option 3"],
                        "answer": "Correct option"
                    }},
                    {{
                        "type": "fill_in_the_blank",
                        "question": "Sentence with a ____.",
                        "answer": "correct word"
                    }}
                ]
            }}
        }}
        """}
    ]

    try:
        # Call the OpenAI chat completion API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=1500,
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