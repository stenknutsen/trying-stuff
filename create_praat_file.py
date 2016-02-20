import sys

def write():
    print('Creating new praat file')

    name = raw_input('Enter name of text file: ')+'.praat'  # Name of text file coerced with +.txt

    try:
        file = open(name,'a')   # Trying to create a new file or open one
        file.write("hello world in the new file\n")

        file.write("and another line\n")

        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python



write()