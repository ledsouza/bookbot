def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    n_words = get_number_of_words(text)
    print(f"Number of words in the book: {n_words}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    main()