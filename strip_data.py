####################
#
#strips everything from raw data text files
#
###################
src_file_name = raw_input('Enter name of file to open: ')
src_file_name = "/Users/stenknutsen/Desktop/mini_lexicon/"+ src_file_name


dest_file_name = raw_input('Enter name of file to create (txt file extension will be added: ')
dest_file_name = "/Users/stenknutsen/Desktop/lex_data/"+dest_file_name+".txt"

src_file = open(src_file_name)

dest_file = open(dest_file_name,'a')

for line in src_file:
    line = line.strip(' \t\n\r')
    for word in line.split():
           if word[0].isalpha():
                dest_file.write(word+'\n')

dest_file.close()