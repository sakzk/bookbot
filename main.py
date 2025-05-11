from stats import get_word_count, get_alphabet_count
import sys

def main():
    # validate command line argument.
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        exit(1)
    path_to_book_file = sys.argv[1] # TODO
    # file_content = get_book_text("./" + path_to_book_file)
    file_content = get_book_text(path_to_book_file)
    # print(file_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book_file}...")

    print("----------- Word Count ---------- ")
    word_count = get_word_count(file_content)
    print(f"Found {word_count} total words")

    print("--------- Character Count ------- ")
    character_to_count = get_alphabet_count(file_content) # TODO: 命名 単数形_to_単数形 でいいのか？
    character_to_count = convert_to_sortable(character_to_count)
    character_to_count.sort(reverse=True, key=sort_on)
    prity_print(character_to_count)

    print("============= END =============== ")

def get_book_text(path_to_book_file)-> str:
    try:
        with open(path_to_book_file) as f:
            file_content = f.read()
        return file_content
    except FileNotFoundError:
        print(f"File[{path_to_book_file}] cannot be found.")
        exit(2) # ref: https://en.wikipedia.org/wiki/Errno.h

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
