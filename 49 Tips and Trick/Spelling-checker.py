from autocorrect import Speller

class SpellingCorrector:
    def __init__(self):
        self.spell = Speller(lang='en')

    def correct_spelling(self, query):
        corrected_query = self.spell(query)
        return corrected_query

class CustomerSupport:
    def __init__(self):
        self.spelling_corrector = SpellingCorrector()

    def process_query(self, query):
        corrected_query = self.spelling_corrector.correct_spelling(query)
        
        response = self.generate_response(corrected_query)
        return response

    def generate_response(self, query):
        
        return "Thank you for your query: " + query


def take_user_input():
    return input("Please enter your query: ")


if __name__ == "__main__":
    support = CustomerSupport()
    query = take_user_input()
    response = support.process_query(query)
    print("Original Query:", query)
    print("Corrected Query:", response)
