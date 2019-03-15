d={} 
lenght = 0 
k = 0 
with open ('C:\\Users\\1\\Downloads\\rosalind_gc.txt', 'r+') as tex:
          for line in tex:
                    line = line.strip()
                    if line.isupper() != True: 
                              d[line] = []
                              shifr = line 
                              
                    else:
                              d[shifr]+=[line]
maxx = 0.0          
for key in d.keys(): #шифр
          for element in d.get(key): #отдельные последовательности
                    lenght += len(element)
                    for el in element: #отдельные нуклеотиды
                              if el == 'G' or el == 'C':
                                        k+=1
          percent = k/lenght
          d.update({key : percent})
          if percent > maxx:
                    maxx = percent*100
          k=0
          lenght = 0
nd = {value: key for key, value in d.items()}
for element in nd.keys():
          if element == maxx:
                    print(nd[element][1:])
print('%.6f'% maxx)
      

                    
