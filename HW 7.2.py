def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:] if text else ""
    if not text.endswith('.'):
        text += '.'
    return text
print(correct_sentence("Привет"))
print(correct_sentence("Привет"))
print(correct_sentence("Привет."))
print(correct_sentence("как дела"))