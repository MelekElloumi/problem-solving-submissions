l=c=''
for x in''.join(f'{ord(i):07b}'for i in input()):
 if x!=l:l=x;c+='  000  00'[l>'0'::2]
 else:c+='0'
print(c[1:])