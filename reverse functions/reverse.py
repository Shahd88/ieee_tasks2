def convert (n):
    st = str(n)
    result = []
    for num in st:
        result.append(int(num))
    result.reverse()
    return result
print(convert(123456789))
print(convert(45610200))