import sys
from googletrans import Translator

def translate_to_english(text, src_lang='auto'):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest='en')
    return translated_text.text

def main():
    if len(sys.argv) != 2:
        print("Usage: python translate.py 'text'")
        return

    text_to_translate = sys.argv[1]
    translated_text = translate_to_english(text_to_translate)
    print(translated_text)

if __name__ == "__main__":
    main()
