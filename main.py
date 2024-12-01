def main():
    book_path ="/home/frodo/Desktop/workspace/bootDev/NewBookBot/workspace/github.com/sakuthush/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # chars_list = chars_dict_to_sorted_list(chars_dict)
    # for item in chars_list:
    #     if not item["char"].isalpha():
    #         continue
    #     print(f"The '{item['char']}' character was found {item['num']} times")


    print(f"---------- Begin report of {book_path} ----------")
    print(f"{num_words} words found in the document")
    print()
    
    chars_list = chars_dict_to_sorted_list(chars_dict)
    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("---------- End of report ----------")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(text):
    with open(text) as f:
        return f.read()
    
def get_chars_dict(text):
    character_count = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1              
    return character_count

def sort_on(dict):
    return dict['num']

def chars_dict_to_sorted_list(num_chars_d):
    sorted_list = []
    for ch in num_chars_d:
        sorted_list.append({"char": ch, "num": num_chars_d[ch]})    
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list




if __name__ == "__main__":
    main()
