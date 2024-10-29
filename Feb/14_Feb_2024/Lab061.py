# reverse a string program'
def rev_String(str):
    rev = ""
    for c in str:
        rev = c + rev
    print(rev)


orignal_Str = input("enter a word")
rev_word = rev_String(orignal_Str)
print(rev_word)

orignal = orignal_Str.lower()
# Pallindrome reverse string == orignal string like mom

if orignal == rev_word:
    print("palindrome")
else:
    print("not a palindrome")
