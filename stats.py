
def get_word_count(file_content: str) -> int:
    # split() のセパレータの理解は怪しい。
    return len(file_content.split())

def get_character_count(file_content: str) -> int:
    character_to_count = {}
    # file_content.lower() # NOTE: こいつは、file_content を上書きしない！
    for char in file_content.lower():
        if char not in character_to_count:
            character_to_count[char] = 0
        character_to_count[char] += 1
    return character_to_count
