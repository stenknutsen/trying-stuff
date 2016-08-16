def file_to_list(fname):
    list = []
    with open(file_name) as f:
        for line in f:
            if line == "\n":
                break
            line = line.rstrip()
            list.append(line)
    return list


def find_zeroes(lfile):
    list = []
    for line in lfile:
        if (line.split(",")[3]=='0'):
            list.append(line+"<")
        else:
            list.append(line)
    return list

f = raw_input('Enter name of file to open: ')


file_name = "/Users/stenknutsen/Desktop/IO_folder/"+f+""




l = file_to_list(file_name)
i=0
for line in l:
    print(str(i) + " " +line)
    i=i+1

#l = find_zeroes(l)