s=input()
b=True
sarcasm=''
for c in s:
    x=c
    if c.isalpha():
        if b:
            x=c.lower()
        else:
            x=c.upper()
        b=not b
    sarcasm+=x
print(''.join(sarcasm))