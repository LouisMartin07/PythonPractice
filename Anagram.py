def is_anagram(string1, string2):
    # Normalize the strings by making them lowercase and sorting the letters
    normalized_string1 = (sorted(string1.lower()))
    normalized_string2 = (sorted(string2.lower()))

    return normalized_string1 == normalized_string2

print(is_anagram('charm', 'march'))  
print(is_anagram('CharM', 'mARcH'))  
print(is_anagram('abcde2', 'c2abeld'))  
print(is_anagram('1racecar', 'racecar'))
