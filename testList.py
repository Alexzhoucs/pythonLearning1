List0 = ["一", "二", "三"]
List1 = List0
List2 = List0[:]

i = int(0)

List = [List0, List1, List2]


size = len(List)
for i in range(0,size,1):
    print(i,List[i])

print("\nCHANGE\n")
List0.reverse()

size = len(List)
for i in range(0,size,1):
    print(i,List[i])