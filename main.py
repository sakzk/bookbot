from stats import get_word_count, get_character_count

def main():
    path_to_book_file = "./books/frankenstein.txt"
    file_content = get_book_text(path_to_book_file)
    # print(file_content)
    word_count = get_word_count(file_content)
    print(f"{word_count} words found in the document")
    character_to_count = get_character_count(file_content) # TODO: 命名 単数形_to_単数形 でいいのか？
    print(f"unsorted mapping: {character_to_count}")

def get_book_text(path_to_book_file)-> str:
    with open(path_to_book_file) as f:
        file_content = f.read()
    return file_content
    return None # with ブロックの仕様を理解していない。エラーハンドリングで処理するべき。

main()
