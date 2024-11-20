def freq(list1):
    list2 = list(set(list1))
    for x in list2:
        frequency = list1.count(x)
        print(f"Frequency of {x} = {frequency}")

list1 = list((input()))
freq(list1)
