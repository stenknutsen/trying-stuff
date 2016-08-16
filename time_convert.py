import time
import sys
import datetime
import calendar

def make_timestamp(s):
    dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    epoch_time = calendar.timegm(dt.timetuple())
    return epoch_time

file_name = raw_input('Enter name of file to open: ')
new_file_name = "/Users/stenknutsen/Desktop/IO_folder/unix_"+file_name+""
file_name = "/Users/stenknutsen/Desktop/IO_folder/"+file_name+""

new_file = open(new_file_name, 'a')
#new_file.write("ms,ts,x,y\n")
with open(file_name) as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip()
        #print("DATA:")
        #print(line)
        date_data = line.split(',')
        #print(date_data[0])
        split_date = date_data[0].split('.')
        #print(split_date[0])
        #print(split_date[1])
        mil_time = make_timestamp(str(split_date[0]))
        #print(mil_time)
        #print(str((mil_time*1000)+int(split_date[1]))+ "," + line)
        new_file.write(str((mil_time*1000)+int(split_date[1]))+ "," + line + '\n')

new_file.close()