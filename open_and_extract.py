import sys

def extract_xmin_xmax(file_name):
    f = open(file_name, 'r')
    print f
    found_vowel = False
    found_interval = False
    for x in range(0,100) :
        target = f.readline()

        if target.endswith("vowel\"\n"):
            #print(x1)
            #print(x2)
            #print(x)
            #print(target)
            found_vowel = True
            break
    if found_vowel != True:
        f.close()
        return
    for x in range(0,100):
        target = f.readline()
        if target.endswith("[2]:\n"):
            #print(target)
            found_interval = True
            break
    if found_interval != True:
        f.close()
        return
    x1 = f.readline()
    x2 = f.readline()
    x1 = float(x1[19:])
    x2 = float(x2[19:])


    print(x1)
    print(x2)

    print(x2-x1)

    f.close()

    return {'xmin':x1,'xmax':x2}
