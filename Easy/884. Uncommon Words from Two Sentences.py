from collections import Counter


def uncommonFromSentences(s1, s2):
    words_s1 = s1.split()
    words_s2 = s2.split()

    all_words = words_s1 + words_s2

    word_count = Counter(all_words)

    return [word for word in word_count if word_count[word] == 1]


s1 = "this apple is sweet"
s2 = "this apple is sour"