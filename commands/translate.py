from deep_translator import GoogleTranslator


def translate():
    language_to_translate = input("Into which language should it be translated?")
    text = input("What should i translate?: ")

    translated = GoogleTranslator(source='auto', target=language_to_translate).translate(text)
    print(f"The translation is: {translated}")
