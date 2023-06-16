import string
from itertools import product, combinations


def deleteDuplicates(lst):  # lst - list of duplicate values
    return list(set(lst))


def popularWords(s):  # s - string (text)
    punctuation = string.punctuation + '–' + '—'
    s = s.translate(str.maketrans('', '', punctuation))
    lst_words = list(set(list(s.split())))
    cnt_mas = []  # list for counting the number of repetitions
    for word in lst_words:
        cnt_mas.append((s.count(word), word))
    cnt_mas.sort(reverse=True)
    for i in range(min(10, len(cnt_mas))):
        print(cnt_mas[i])


def backpack(d, w):  # d - dictionary of items, w - max weight of items
    lst_sets = []
    items = list(d.keys())
    for cnt_items in range(1,10**9):
        flag = 0
        for p in combinations(items, cnt_items):
            lst = list(p)
            itw = 0
            for item in lst:
                itw += d[item]
            if itw <= w:
                flag = 1
                lst_sets.append(lst)
        if not flag:
            break
    return lst_sets


print(backpack({'aaa': 10, 'bbb': 100}, 1000))
