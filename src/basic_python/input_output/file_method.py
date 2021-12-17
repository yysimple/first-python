with open("a.txt", "r", encoding="UTF-8") as f:
    # read_data1 = f.readline()
    # print(read_data1)
    for line in f:
        print(line, end="")
    print(f.tell())


