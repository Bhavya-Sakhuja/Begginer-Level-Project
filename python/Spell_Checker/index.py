from spellchecker import SpellChecker

class CheckSpell:
      def __init__(self):
            self.spell = SpellChecker()

      def checkWords(self,text):
            words = text.split()
            correct_words = []

            for i in words:
                correction_word = self.spell.correction(i)
                if correction_word is None:
                    correct_words.append(i) 
                else:
                   correct_words.append(correction_word)

            return " ".join(correct_words)

      def run(self):
         print("--Spell Checker--")
         while(True):
            text = input("Enter text or enter exit to quit: ")
            if text.lower() == 'exit':
                  print("Thankuuu!")
                  break
            correct_output = self.checkWords(text)

            print("Correct word is: ",correct_output)


if __name__ == "__main__":
     CheckSpell().run()