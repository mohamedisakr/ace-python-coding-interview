from collections import defaultdict


def inverted_index(text: str) -> dict[str, list[int]]:
    index = defaultdict(list)
    for idx, word in enumerate(text.split()):
        index[word].append(idx)
    return dict(index)


# test case
# text = "we dont need no education we dont need no thought control no we dont"
# index = inverted_index(text)
# print(index)
# print(index["dont"])
# assert procedure(text, "dont") == [1, 6, 13]


# def inverted_index(text: str) -> dict:
#     index = {}
#     words = text.split(" ")
#     for idx, word in enumerate(words):
#         if word not in index:
#             index[word] = []
#         else:
#             index[word].append(idx)

#     return index
