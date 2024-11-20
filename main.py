list = [9, 9, 1000, 10085, 1872, 2221, 22122]
num = 0
new_list = []
while list != []:
    if num in list:
        count = list.count(num)
        for i in range(count):
            new_list.append(num)
        while num in list:
            list.remove(num)
    num += 1
print(new_list)
