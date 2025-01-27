import genanki
import uuid

def create_anki_deck(lesson_content):
    deck_id = int(uuid.uuid4()) % (10**10)
    deck = genanki.Deck(deck_id, "German Lesson")
    
    for word, meaning in lesson_content["vocabulary"].items():
        note = genanki.Note(
            model=genanki.BASIC_MODEL,
            fields=[word, meaning]
        )
        deck.add_note(note)
    
    deck_file = f"static/anki/german_lesson_{deck_id}.apkg"
    genanki.Package(deck).write_to_file(deck_file)
    return deck_file
