A=[
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 0, 4],
  ]
B = [] #A nin transpozesi
for i in range(4):
    #ic ice listeler olusturuluyor
    B.append([row[i] for row in A])
print("Transpozesi:",B)
