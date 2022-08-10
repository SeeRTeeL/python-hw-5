from collections import Counter


def popularity(text):

    words_list = []

    for words in text.split():
        list_word = ""
        for word in words:
            list_word += word.lower()

        words_list.append(list_word)

        c = dict(Counter(words_list))

    print(sorted(c.items(), key=lambda x: x[1]))


popularity('apple kiwi pineapple kiwi apple kiwi')
