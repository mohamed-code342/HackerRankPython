def merge_the_tools(string, k):
    res = []
    for i in range(0, len(string), k):
        res.append(string[i:i+k])

    for substring in res:
        s = set()
        result = ''
        for char in substring:
            if char not in s:
                s.add(char)
                result += char
        print(result)
