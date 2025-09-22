from tabulate import tabulate
from googletrans import Translator
class TranslateClass:
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
        self.translator = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translated = self.translator.translate(self.word, dest=self.lang).text
        data = [
            ['Language', 'Sentence'],
            ['English', self.word],
            ['Target', translated]
        ]
        return tabulate(data, headers="firstrow", tablefmt="grid")
    

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    lang = input("Enter target language code (e.g., 'hi' for Hindi, 'es' for Spanish): ")
    print(TranslateClass(sentence, lang))

