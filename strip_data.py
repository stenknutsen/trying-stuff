####################
#
#strips everything from raw data text files
#
###################
src_file_name = raw_input('Enter name of file to open: ')
src_file_name = "/Users/stenknutsen/Desktop/from_coca/"+ src_file_name


dest_file_name = raw_input('Enter name of file to write to (txt file extension will be added: ')
#dest_file_name = "/Users/stenknutsen/Desktop/lex_data/"+dest_file_name+".txt"

dict_name = raw_input('Enter dict name: ')

tag_name = raw_input('Enter tag name: ')

src_file = open(src_file_name)

dest_file = open("/Users/stenknutsen/Desktop/lex_data/"+dest_file_name+".txt",'a')

dest_file.write(dict_name+"={")


for line in src_file:
    line = line.strip(' \t\n\r')
    for word in line.split():
           if word[0].isalpha():
                dest_file.write('"'+word.lower()+'":"'+tag_name+'",\n')

dest_file.write("}\n")
dest_file.close()