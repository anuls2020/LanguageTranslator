# This is a sample Language Translator
from googletrans import Translator


def translate_text(text, dest_language='ml'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text


def main():
    # Input the test to translate
    test_to_translate = input("Enter the test to translate: ")

    # Specify the destination language
    destination_language = input("Enter the destination language:(e.g., 'fr' for French)")

    # Translate text
    translated_text = translate_text(test_to_translate, destination_language)

    print("\nTranslated text")
    print(translated_text)


if __name__ == '__main__':
    main()
