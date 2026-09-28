def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.remove("an")) 
            return n


        
l = ["jit","anita","ankita","anyana"]

print(rem(l, "an"))