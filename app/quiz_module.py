def generate_quiz(lesson_content):
    quiz = []
    for word, meaning in lesson_content["vocabulary"].items():
        quiz.append((f"What does '{word}' mean?", meaning))
    return quiz
