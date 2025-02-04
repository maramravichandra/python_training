# cumulative sum
# numbers = [1,2,5,3,6]
# result = [1,3,8,11,17] [ list[0], list[0]+list[1], ...]

#palindrom string = "lol" "12233221"   12

def is_palindrome1(word:str):
    return list(word) == list(reversed(word))

def is_palindrome2(word:str):
    reversed_str = ""
    for ch in word:
        reversed_str = ch + reversed_str # 1. l+'' = l   2. o+l = ol 3 l+ol = lol
    return word == reversed_str

def is_palindrome3(word:str):
    return word == word[::-1] # [start:end:step] if step is positive = left to right else right to left

def is_palindrome4(word:str):
    reversed_str = ""
    word_len = len(word)
    while word_len > 0:
        reversed_str =  reversed_str + word[word_len-1]
        word_len = word_len - 1
    return word == reversed_str

word = "12232210"
print("is_palindrome1 : ", is_palindrome1(word))
print("is_palindrome2 : ", is_palindrome2(word))
print("is_palindrome3 : ", is_palindrome3(word))
print("is_palindrome4 : ", is_palindrome4(word))

