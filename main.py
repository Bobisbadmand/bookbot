def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    numb_words = Word_Count(text)
    letters_in_story = letter_count(text)
    letters_sorted = char_list_sorted(letters_in_story)
    #return text
    #print(numb_words)
    #print(letters_in_story)
    #print(f"LETTERS SORTED: {letters_sorted}")

    print(f"--- Begin report of {book_path} ---")
    print(f"{numb_words} words found in the document")
    print()

    for letterSorted in letters_sorted:
        if not letterSorted["char"].isalpha():
            continue
        print(f"The '{letterSorted['char']}' charactere was found {letterSorted['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def Word_Count(text):
    fulltext = text
    words = len(fulltext.split())
    return words
    #wordsCounted = words.count
    #print(words)
    #print(words)

def letter_count(text):
    lowerLetter = text.lower()
    letterDict = {}
    for letter in lowerLetter:
        if letter in letterDict:
            letterDict[letter] += 1
        else:
            letterDict[letter] = +1
    lettercounts = letterDict
    #print(lowerLetter)
    return lettercounts


def sort_by(L):
    return L["num"]


def char_list_sorted(letters_in_story):
    char_list = []
    for ch in letters_in_story:
        char_list.append({"char": ch, "num": letters_in_story[ch]})
    char_list.sort(reverse=True, key=sort_by)

    return char_list



main()