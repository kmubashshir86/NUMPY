import numpy as np

ages=np.array([[12,34,21,2,34,22,12,23]
              ,[39,44,65,22,99,18,90,99]])
teenagers = ages[ages<18] #boolean indexing use to filter

print(teenagers)

adult = ages[(ages >= 18) & (ages <= 65) ]#& <= c wala and as numpy use c
evens = ages[ages %2 ==0]
seniors = ages[ages >= 65 ]
print(adult)

#where func
np.nan#not a number
print(np.where(ages>=18,ages,0))