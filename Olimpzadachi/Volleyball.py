from queue import Queue

# входные данные
N = int(input())
strength = input()
q = int(input())
list_k = []
for i in range(q):
    ki = int(input())
    list_k.append(ki)

# преобразование данных (подготовка)
strength = map(int, strength.split())  # перевести в list

ochered = Queue(maxsize=N)

for i in strength:
    ochered.put(i)


c = 0
for i1 in range(max(list_k)):
    c += 1
    cc = 0
    if c == 1:
        first = ochered.get()
        second = ochered.get()
        if first < second:
            ochered.put(first)
            cc = second
        else:
            ochered.put(second)
    else:
        three = ochered.get()
        four = ochered.get()
        if cc < three:
            ochered.put(three)
        else:
            ochered.get(four)



# if i1 in list_k:
#     print(first, second)
