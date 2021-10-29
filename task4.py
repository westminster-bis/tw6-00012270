def absolute_value(x,y):
    if x < y:
        return -1
    elif x > y:
        return 1
    elif x==y:
        return 0

inp1 = int(input("Value 1: "))
inp2 = int(input("Value 2: "))
print(absolute_value(inp1,inp2))