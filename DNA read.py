DNA = input('')
a, c, g, t, lenght = 0, 0, 0, 0, len(DNA)
for k in range(lenght):
          if DNA[0] == 'A':
                    a += 1
                    DNA = DNA[1:]
          elif DNA[0] == 'C':
                    c += 1
                    DNA = DNA[1:]
          elif DNA[0] == 'G':
                    g += 1
                    DNA = DNA[1:]
          elif DNA[0] == 'T':
                    t += 1
                    DNA = DNA[1:]
print(a, c, g, t, sep = ' ')
