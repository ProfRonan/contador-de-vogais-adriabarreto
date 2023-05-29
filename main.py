def count_vowels(a):
    vogais = "aeiouAEIOU"
    result = 0
    for char in a:
        if char in vogais:
            result = result+1
    return result
count_vowels("aeiouAEIOU")
