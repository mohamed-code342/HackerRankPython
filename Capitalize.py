# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    res = []
    for word in words:
        if word and word[0].isalpha():
            res.append(word.capitalize())
        else:
            res.append(word)
    return ' '.join(res)
  

