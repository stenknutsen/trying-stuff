import sys

##############################################
#
#   Calculates the "curve" for the Duration
#   Tier from data extracted by dur_swap.py
#   and creates a new Praat duration tier
#   file.
#
#
#
#
##############################################


def vowel_strectching_time(file_name, begin_v, end_v, percent_legnthen):
    print("Hi from VST!!!!")
    dif = end_v - begin_v
    perc = float(dif*0.40)
    begin_vowel = begin_v+perc
    end_vowel = end_v - perc
    print("begin vowel 40 percent is: ")+str(begin_vowel)
    print("end vowel 40 percent is: ")+str(end_vowel)
    total_area = end_v - begin_v
    midpoint = float((end_v-begin_v)/2.0)+begin_v
    new_area = float(percent_legnthen*total_area)
    x = float((end_vowel-begin_vowel)/2.0)
    y = float(new_area/x)
    print('percent lengthen is: ')+str(percent_legnthen)
    print('total area (before lengthening) is: ')+str(total_area)
    print('adding new area of: ')+str(new_area)
    print('for a total area of: ')+str(new_area+total_area)
    print('midpoint is: ')+str(midpoint)
    print('x is: ')+str(x)
    print('y is: ')+str(y)
    print('height of peak is: ')+str(y+1.0)
    tier_name = ("dur_"+ file_name.split(".")[0])
    print(tier_name)
    file_name = ("/Users/stenknutsen/Desktop/IO_folder/dur_"+file_name.split(".")[0]+".praat")
    print(file_name)
    print('Creating new praat file')

    file = open(file_name,'a')
    file.write('Create DurationTier: \"'+tier_name+'\", '+ str(begin_vowel)+', '+str(end_vowel)+'\n')
    file.write('Add point: '+str(begin_vowel)+', 1\n')
    file.write('Add point: '+str(midpoint)+', '+str(y+1.0)+'\n')
    file.write('Add point: '+str(end_vowel)+', 1\n')

    file.close()

