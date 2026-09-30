s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)