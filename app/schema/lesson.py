from jsonschema import validate, ValidationError

lesson_schema = {
    "type": "object",
    "properties": {
        "lesson": {
            "type": "object",
            "properties": {
                "level": {"type": "string"},
                "theme": {"type": "string"},
                "vocabulary": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "word": {"type": "string"},
                            "translation": {"type": "string"},
                            "example_sentence": {"type": "string"}
                        },
                        "required": ["word", "translation", "example_sentence"]
                    }
                },
                "grammar": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "rule": {"type": "string"},
                            "explanation": {"type": "string"},
                            "example": {"type": "string"}
                        },
                        "required": ["rule", "explanation", "example"]
                    }
                },
                "assignments": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string"},
                            "question": {"type": "string"},
                            "options": {"type": "array", "items": {"type": "string"}},
                            "answer": {"type": "string"},
                            "instruction": {"type": "string"}
                        },
                        "required": ["type", "question", "answer"]
                    }
                }
            },
            "required": ["level", "theme", "vocabulary", "grammar", "assignments"]
        }
    },
    "required": ["lesson"]
}

# Validate JSON response
def validate_lesson(lesson_json):
    try:
        validate(instance=lesson_json, schema=lesson_schema)
        print("JSON is valid!")
    except ValidationError as e:
        raise ValueError(f"JSON validation error: {e.message}")
