def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_frequencies(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequencies = {c: 0 for c in alphabet}
    for char in text:
        if char.lower() in frequencies.keys():
            frequencies[char.lower()] += 1
    return frequencies

