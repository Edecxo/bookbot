from stats import get_num_words, get_char_frequencies
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_text(path)
    word_count = get_num_words(text)
    char_freqs = get_char_frequencies(text)
    char_freq_list = [{"letter":key, "occured":char_freqs[key]} for key in char_freqs]
    char_freq_sorted = char_freq_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_freq_list:
        print(f"{item['letter']}: {item['occured']}")
    print("============= END ===============")

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def sort_on(dictionary):
    return dictionary["occured"]

main()

