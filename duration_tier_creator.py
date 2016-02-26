import sys
from open_and_extract import*
#get_PRAAT_file_name_to_read = raw_input("Enter name of PRAAT file to read from: ")
#my_dict = extract_xmin_xmax(get_PRAAT_file_name_to_read)

#print("This is xmin: "+ str(my_dict['xmin']))
#print("This is xmax: "+ str(my_dict['xmax']))

file_name = raw_input('Enter name of file to create: ')
file_name = "/Users/stenknutsen/Documents/praat_scripts_folder/"+file_name + ".praat"
tier_name = raw_input('Enter tier name: ')
begin_vowel = float(raw_input('Enter xmin: ' ))
end_vowel = float(raw_input('Enter xmax: ' ))
percent_legnthen = float(raw_input('Enter percent lengthen: '))/100.0
total_area = end_vowel - begin_vowel
midpoint = float(total_area/2.0)+begin_vowel
new_area = float(percent_legnthen*total_area)
x = float(total_area/2.0)
y = float(new_area/x)

print('percent lengthen is: ')+str(percent_legnthen)
print('total area (before lengthening) is: ')+str(total_area)
print('adding new area of: ')+str(new_area)
print('for a total area of: ')+str(new_area+total_area)

print('midpoint is: ')+str(midpoint)
print('x is: ')+str(x)
print('y is: ')+str(y)
print('height of peak is: ')+str(y+1.0)

print('Creating new praat file')

file = open(file_name,'a')
file.write('Create DurationTier: \"'+tier_name+'\", '+ str(begin_vowel)+', '+str(end_vowel)+'\n')
file.write('Add point: '+str(begin_vowel)+', 1\n')
file.write('Add point: '+str(midpoint)+', '+str(y+1.0)+'\n')
file.write('Add point: '+str(end_vowel)+', 1\n')

file.close()


#  1.27959183673
#  1.43922902494

