cheracters = 'translit'

output = ''
lenght = len(cheracters)
i = 0
while i < lenght:
    output = output + cheracters[i]
    i = i + 1

lenght  = lenght * -1
i = -2

while i >= lenght:
    output = output + cheracters[i]
    i = i - 1

print(output)
