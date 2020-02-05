
for i in range(1, 101):
    include = str(i).find("7")
 
    if include == -1 and int(i) % 7 != 0:
        print(i,)
