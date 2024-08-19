other_words = []
def single_root_words(*other_words, root_word='ход'):
    same_words = []
    for word in other_words:
        if word in root_word or root_word in word:
            same_words.append(word)
    return same_words
    print(same_words)


result1 = single_root_words("выход", "маятник", "переход", "сахар", "находка", "лето", "ход")
print(result1)
result2 = single_root_words( "жаровня", "солнце", "пожар", "сходняк", "жаркое", root_word="жар")
print(result2)
