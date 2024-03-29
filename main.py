def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    n_words = get_number_of_words(text)
    letter_count = count_letters(text)
    report(n_words, letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    lower_case_text = text.lower()
    for letter in lower_case_text:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def report(n_words, letter_count):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{n_words} words found in the document\n')
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letter_count:
        print(f'The "{letter}" character was found {count} times')
    print('--- End report ---')

if __name__ == '__main__':
    main()