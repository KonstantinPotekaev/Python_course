import string


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
    for i in range(min(10,len(cnt_mas))):
        print(cnt_mas[i])


def backpack(d):    #d - dictionary of items


