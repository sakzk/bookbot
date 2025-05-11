from stats import get_word_count, get_alphabet_count

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
    character_to_count = get_alphabet_count(file_content) # TODO: 命名 単数形_to_単数形 でいいのか？
    character_to_count = convert_to_sortable(character_to_count)
    character_to_count.sort(reverse=True, key=sort_on)
    prity_print(character_to_count)

    print("============= END =============== ")

def get_book_text(path_to_book_file)-> str:
    with open(path_to_book_file) as f:
        file_content = f.read()
    return file_content

def prity_print(character_to_count: list) -> None:
    # for character, count in character_to_count:
    #     print(f"{character}: {count}")
    for d in character_to_count:
        print(f"{d["character"]}: {d["count"]}")

# helper for dictionary sorting 
def sort_on(dict):
    return dict["count"]

def convert_to_sortable(d: dict) -> list:
    l = []
    for k, v in d.items():
        l.append({"character": k, "count": v})
    return l

main()
