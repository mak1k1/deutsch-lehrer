import genanki
import uuid

def create_anki_deck(lesson_content):
    deck_id = int(uuid.uuid4()) % (10**10)
    deck = genanki.Deck(deck_id, "German Lesson")
    
    for vocab in lesson_content["lesson"]["vocabulary"]:
        note = genanki.Note(
            model=genanki.BASIC_MODEL,
            fields=[vocab["word"], vocab["translation"]]
        )
        deck.add_note(note)

    for grammar in lesson_content["lesson"]["grammar"]:
        note = genanki.Note(
            model=genanki.BASIC_MODEL,
            fields=[grammar["explanation"], grammar["example"]]
        )
        deck.add_note(note)

    for assignment in lesson_content["lesson"]["assignments"]:
        note = genanki.Note(
            model=genanki.BASIC_MODEL,
            fields=[assignment["question"], assignment["answer"]]
        )
        deck.add_note(note)
    
    deck_file = f"static/anki/german_lesson_{deck_id}.apkg"
    genanki.Package(deck).write_to_file(deck_file)
    return deck_file
