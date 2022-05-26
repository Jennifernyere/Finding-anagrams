# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    # [assignment] Add your code here
   
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

str1 = input('First word: ')
str2 = input('Second word: ')

print(find_anagrams(str1, str2))

