my_set = [ '' for i in range(300)]
m = 0
with open ('C:\\Users\\1\\Downloads\\rosalind_splc1.txt ') as text:
          for line in text:
                    if line.isupper():
                              line = line.strip()
                              my_set[m] += line
                    else:
                              m += 1
                    
DNA = my_set[1:m+1]
print(DNA)

dna = DNA[0]
l, otvet = [], []
print(dna)
while len(dna) != 0:
          for i in range (len(dna)):
                    for k in range(len(dna), i, -1):
                              for stroka in DNA:
                                        print(stroka)
                                        l.append(stroka.find(dna[i:k]))
                                        if -1 in l:
                                                  break
                                        else:
                                                  otvet.append(dna[i:k])
                                        l = []

                                                  
          dna = dna[1:]
print(otvet)

