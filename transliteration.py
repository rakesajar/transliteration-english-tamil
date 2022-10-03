# Imports
from ai4bharat.transliteration import XlitEngine


# Classes
class Transliteration:
    def __init__(self, beam_width=10):
        self.english2tamil = XlitEngine(["ta"], beam_width=beam_width, src_script_type = "en")
        self.tamil2english = XlitEngine(beam_width=beam_width, rescore=True, src_script_type = "indic")
    
    def transliterate_word(self, word, t2e=True, topk=5):
        if t2e:
            out = self.tamil2english.translit_word(str(word), 'ta', topk=5)
            return out
        out = self.english2tamil.translit_word(str(word))["ta"]
        # out = [item.removesuffix(u'\u200c') for item in out]
        return out
    
    def transliterate_sentence(self, sentence, t2e=True):
        if t2e:
            out = self.tamil2english.translit_sentence(str(sentence), 'ta')
            return out
        out = self.english2tamil.translit_sentence(str(sentence))["ta"]
        # out = out.removesuffix(u'\u200c')
        return out


transliteration_model = Transliteration()
