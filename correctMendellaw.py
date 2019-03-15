d, h, m = int(input ('')), int(input("")), input("")
gametes = []
def add (d, h, m):
    for i in range(d):
        gametes.append('A')
        gametes.append('A')
    for i in range(h):
        gametes.append('A')
        gametes.append('a')
    for i in range(int(m)):
        gametes.append('a')
        gametes.append('a')
add(d,h,m)
print(gametes)
vsego = len(gametes)
genotype = []
for i in range(vsego):
    if len(gametes) == 1:
        break
    if i % 2 == 0:
        for i in range (2, len(gametes)):
            gen = gametes[0] + gametes[i]
            genotype.append(gen)
        gametes = gametes[1:]
    else:
        for i in range(1, len(gametes)):
            gen = gametes[0] + gametes[i]
            genotype.append(gen)
        gametes = gametes[1:]
    print(gametes)
       
print (genotype)
ch = 0
for i in genotype:

        if 'A' in i:
            ch+=1
print(ch/len(genotype))