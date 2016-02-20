import sys

file_name = raw_input('Enter name of file: ')+'.praat'
tier_name = raw_input('Enter tier name: ')
begin_vowel = float(raw_input('Enter beginning time of vowel: '))
end_vowel = float(raw_input('Enter end time of vowel: '))
percent_legnthen = float(raw_input('Enter percent lengthen: '))/100
total_area = end_vowel - begin_vowel
midpoint = (total_area/2)+begin_vowel
new_area = (percent_legnthen*total_area)
x = total_area/2
y = new_area/x

print('percent lengthen is: ')+str(percent_legnthen)
print('total area (before lengthening) is: ')+str(total_area)
print('adding new area of: ')+str(new_area)
print('for a total area of: ')+str(new_area+total_area)

print('midpoint is: ')+str(midpoint)
print('x is: ')+str(x)
print('y is: ')+str(y)
print('height of peak is: ')+str(y+1)

print('Creating new praat file')



file = open(file_name,'a')   # Trying to create a new file or open one
file.write('Create DurationTier: \"'+tier_name+'\", '+ str(begin_vowel)+', '+str(end_vowel)+'\n')

file.write('Add point: '+str(begin_vowel)+', 1\n')
file.write('Add point: '+str(midpoint)+', '+str(y+1)+'\n')
file.write('Add point: '+str(end_vowel)+', 1\n')

file.close()


#  .648327
#  .797098

