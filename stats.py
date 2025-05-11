
def get_word_count(file_content: str) -> int:
    # split() のセパレータの理解は怪しい。
    return len(file_content.split())