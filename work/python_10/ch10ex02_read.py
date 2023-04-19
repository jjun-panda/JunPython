with open("cars.data", "r") as fp:
    read_data = fp.readlines()

lis = []
for line in read_data:
    row = line.split("|")
    lis.append({"seq":int(row[0]), "name":row[1], "price":int(row[2])})

for r in range(len(lis)):
    print(r)
    # print(f'{r["seq"]}|{r["name"]}|{r["price"]}')