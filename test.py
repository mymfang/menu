display = {}
for i in range(12):
    display[i] = 0
print(display)

a = '+1'
print(a.strip('+'))
if int(a.strip('+')) in display:
    print('yes')