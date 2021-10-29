def find(word_raw, letter, search_index=0):
    word = word_raw[search_index:]
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index + search_index
        index = index + 1
    return -1

inp1 = input("Word: ")
inp2 = input("Letter: ")
inp3 = int(input("Search index: "))
print("\nResult: " + str(find(inp1, inp2[0], inp3)))
print(str(find(inp1, inp2[0], inp3) + 1) + "th letter is a match!")
