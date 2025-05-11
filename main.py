from stats import get_word_count, get_character_count

def main():
    BOOK_TITLE = "frankenstein"

    print("============ BOOKBOT ============")
    path_to_book_file = f"./books/{BOOK_TITLE}.txt"
    file_content = get_book_text(path_to_book_file)
    # print(file_content)
    print(f"Analyzing book found at books/{BOOK_TITLE}.txt...")

    print("----------- Word Count ---------- ")
    word_count = get_word_count(file_content)
    print(f"{word_count} words found in the document") #TODO 2

    print("--------- Character Count ------- ")
    character_to_count = get_character_count(file_content) # TODO: 命名 単数形_to_単数形 でいいのか？
    # print(f"unsorted mapping: {character_to_count}")
    prity_print_dict(character_to_count)

    print("============= END =============== ")
    
def prity_print_dict(character_to_count: dict) -> None:
    # TODO:
    return 

def get_book_text(path_to_book_file)-> str:
    with open(path_to_book_file) as f:
        file_content = f.read()
    return file_content

main()
