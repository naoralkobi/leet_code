temperatures = [89,62,70,58,47,47,46,76,100,70]

result = [0] * len(temperatures)
indexes = []

for i in range(len(temperatures) - 1):
    if temperatures[i + 1] > temperatures[i]:
        result[i] = 1
        helper = []
        for index in indexes:
            if temperatures[i + 1] > temperatures[index]:
                result[index] = i + 1 - index
                # indexes.remove(index)
            else:
                helper.append(index)
        indexes = helper

    else:
        indexes.append(i)


print(result)