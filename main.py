def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = count_words(text)
    char_freqs = get_char_frequencies(text)
    char_freq_list = [{"letter":key, "occured":char_freqs[key]} for key in char_freqs]
    char_freq_sorted = char_freq_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for item in char_freq_list:
        print(f"The '{item['letter']}' character was found {item['occured']} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def get_char_frequencies(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequencies = {c: 0 for c in alphabet}
    for char in text:
        if char.lower() in frequencies.keys():
            frequencies[char.lower()] += 1
    return frequencies


def sort_on(dictionary):
    return dictionary["occured"]


main()
