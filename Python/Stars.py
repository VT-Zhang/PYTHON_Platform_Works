def star(list):
    i = 0
    for x in list:
        print "*" * list[i]
        i = i + 1

star([4,6,1,3,5,7,25])

def star2(list):
    i = 0
    for x in list:
        if type(list[i]) is int:
            print "*" * list[i]
        elif type(list[i]) is str:
            print list[i][0].lower() * len(list[i]);
        i = i + 1
star2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
