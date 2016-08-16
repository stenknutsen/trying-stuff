
def tsm(str):
    strip_day = str.split(" ")[1]
    print(strip_day)
    s= strip_day.split(":")
    hours = s[0]
    minutes = s[1]
    s2 = s[2].split(".")
    seconds = s2[0]
    milliseconds = s2[1]

    print(hours)
    print(minutes)
    print(seconds)
    print(milliseconds)

    hours = int(hours)*60*60*1000
    minutes = int(minutes)*60*1000
    seconds = int(seconds)*1000
    milliseconds = int(milliseconds)
    thingy = int(float(s[2])*1000)
    total = hours+minutes+seconds+milliseconds

    print(hours)
    print(minutes)
    print(seconds)
    print(milliseconds)
    print(thingy)
    return total



def tsm_no_date(str):

    s= str.split(":")
    hours = s[0]
    minutes = s[1]
    s2 = s[2].split(".")
    seconds = s2[0]
    milliseconds = s2[1]

    print(hours)
    print(minutes)
    print(seconds)
    print(milliseconds)

    hours = int(hours)*60*60*1000
    minutes = int(minutes)*60*1000
    seconds = int(seconds)*1000
    milliseconds = int(milliseconds)
    thingy = int(float(s[2])*1000)
    total = hours+minutes+seconds+milliseconds

    print(hours)
    print(minutes)
    print(seconds)
    print(milliseconds)
    print(thingy)
    return total



print(tsm_no_date("13:41:17.910"))



