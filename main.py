def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)

    #print the books
    #print(file_contents)
    
    word_count = count_words(file_contents)
    #print(f"The book has {word_count} words.")

    character_count = count_characters(file_contents)
    #print(character_count)

    #convert dictionary to list and sort it 
    char_sorted_list = chars_dict_to_sorted_list(character_count)

    #Make the report 
    print(f"--- Being report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for char in char_sorted_list:
        if not char["char"].isalpha():
            continue
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters(file_contents):
    characters = {}
    lower_case_contents = file_contents.lower() 
    for char in lower_case_contents:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_contents):
    return len(file_contents.split())

if __name__ == '__main__':
    main()
