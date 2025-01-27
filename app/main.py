from ai_module import generate_lesson_with_gpt
from anki_module import create_anki_deck
from database import initialize_database, log_progress
import gradio as gr

def german_tutor(level, theme):
    # Initialize database
    initialize_database()
    # Fetch or create a lesson
    lesson_content_json = generate_lesson_with_gpt(level, theme)
    # Create Anki deck
    anki_file = create_anki_deck(lesson_content_json)
    # Log progress
    log_progress("lesson", f"{level} - {theme}")
    return lesson_content_json, anki_file

# Initialize Gradio interface
iface = gr.Interface(
    fn=german_tutor,
    inputs=["text", "text"],
    outputs=["text", "file"]
)

if __name__ == "__main__":
    iface.launch()
