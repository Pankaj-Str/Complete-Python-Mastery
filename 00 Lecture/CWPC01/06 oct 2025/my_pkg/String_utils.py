def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])