def find(word_raw, search_letter, search_index=0):
    word = word_raw[search_index:]
    count = 0

    for letter in word:
        if letter == search_letter:
            count = count + 1
    return count

inp1 = input("Word: ")
inp2 = input("Letter: ")
inp3 = int(input("Search index: "))
print("\nCount: " + str(find(inp1, inp2[0], inp3)))
