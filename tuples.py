print("List can be modify")
print("Tuples cant be modify")

L=[100,200,300,500]
T=(200,300,100,500)
L.append(400)
#T.append(400) this won't work
print(L"L.append(400) works")
print(T"T.append(400) won't work")