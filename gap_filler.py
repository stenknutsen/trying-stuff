import sys




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

def count_zeroes(lfile):
    count=0
    for line in lfile:
        if line[38]=="0":
            count = count + 1
    return count

def tag_start(lfile):
    list = []
    prevLine = "                                                                    "
    for line in lfile:
        if (line.endswith("<"))& (prevLine[38]!="0"):
            list.pop()
            list.append(prevLine+"<s>")
            list.append(line)
        else:
            list.append(line)
        prevLine = line

    return list

def count_starts(lfile):
    count=0
    for line in lfile:
        if line.endswith("<s>"):
            count = count+1
    return count

def start_index(lfile):
    i = 0
    j = 0
    k=[]
    for line in lfile:
        if line.endswith("<s>"):
            i = lfile.index(line)
            #print(i)
            break
    for line in range(i+1, len(lfile)):
        if lfile[line].endswith("<"):
            j = j+1
        else:
            break
    #print(j)
    k.append(i)
    k.append(j)
    return k

def replace_zeroes(start_index_and_num, lfile):
    start = start_index_and_num[0]
    num_zeroes = start_index_and_num[1]

    rep = lfile[int(start)]
    rep = rep[38:].split("<s>")[0]


    print(rep)
    print(lfile[start].split(",")[2])
    print(lfile[start +num_zeroes+1].split(",")[2])
    start_x = int(lfile[start].split(",")[2])
    end_x = int(lfile[start +num_zeroes+1].split(",")[2])
    print("NUM ZERO: " +str(num_zeroes))
    if (start_x>960)&(end_x>960)&(num_zeroes<7):
        print("replace")
        lfile[start] = lfile[start].split("<s>")[0]
        for i in range(start+1, start+num_zeroes+1):
            lfile[i] = lfile[i][:38].split("<")[0]
            lfile[i] = lfile[i]+rep
    elif (start_x<=960)&(end_x<=960)&(num_zeroes<7):
        print("replace")
        lfile[start] = lfile[start].split("<s>")[0]
        for i in range(start+1, start+num_zeroes+1):
            lfile[i] = lfile[i][:38].split("<")[0]
            lfile[i] = lfile[i]+rep

    else:
        print("no replace")
        lfile[start] = lfile[start].split("<s>")[0]
        for i in range(start+1, start+num_zeroes+1):
            lfile[i] = lfile[i].split("<")[0]
    return lfile

#f = "testing.txt"
f = raw_input('Enter name of file to open: ')


file_name = "/Users/stenknutsen/Desktop/IO_folder/"+f+""




l = file_to_list(file_name)
l = find_zeroes(l)
l = tag_start(l)
num = count_starts(l)
zeroes_before = count_zeroes(l)

print(num)

for i in range(0,num):
    k = start_index(l)
    l = replace_zeroes(k,l)



new_file_name = ("/Users/stenknutsen/Desktop/IO_folder/filled_"+f)
file = open(new_file_name, 'a')
for line in l:
    file.write(line +"\n")

file.close()

print("File was "+ str(len(l))+" lines long")

zeroes_after = count_zeroes(l)


print("Number of zeroes before: " + str(zeroes_before))
print("Number of zeroes after: " + str(zeroes_after))