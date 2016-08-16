from time_since_midnight import*

file_name = raw_input('Enter name of file to open: ')
new_file_name = "/Users/stenknutsen/Desktop/IO_folder/tsm_"+file_name+""
file_name = "/Users/stenknutsen/Desktop/IO_folder/"+file_name+""

new_file = open(new_file_name, 'a')

with open(file_name) as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip()

        date_data = line.split(',')

        mil_time = tsm(str(date_data[0]))

        new_file.write(str(mil_time) + "," + line + '\n')

new_file.close()