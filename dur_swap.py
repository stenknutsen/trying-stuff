import sys
from os import listdir
from open_and_extract import extract_xmin_xmax
from open_and_extract import extract_period
from vst import vowel_strectching_time
from dur_swap_logger import create_log

##############################################
#
#   Extracts active/passive verb stem vowel
#   information from Praat TextGrid files and
#   creates new Duration Tiers which will
#   effectively "swap" the duration of the
#   active and passive verb stems.
#
#
#
##############################################


input_filenames_raw = listdir("/Users/stenknutsen/Desktop/IO_folder")
print input_filenames_raw

input_filenames=[]
for f in input_filenames_raw:
    if f.startswith("."):
        continue
    else:
        input_filenames.append(f)


print(input_filenames)


active_filename = input_filenames[0]
passive_filename = input_filenames[1]


print(active_filename)
print(passive_filename)

active_xmin_xmax = extract_xmin_xmax("/Users/stenknutsen/Desktop/IO_folder/"+ active_filename)
passive_xmin_xmax = extract_xmin_xmax("/Users/stenknutsen/Desktop/IO_folder/"+ passive_filename)

print(active_xmin_xmax)
print(passive_xmin_xmax)

active_xmin = active_xmin_xmax["xmin"]
print(active_xmin)
active_xmax = active_xmin_xmax["xmax"]
print(active_xmax)
passive_xmin = passive_xmin_xmax["xmin"]
passive_xmax = passive_xmin_xmax["xmax"]
print(passive_xmin)
print(passive_xmax)

active_vowel_dur = active_xmax - active_xmin
passive_vowel_dur = passive_xmax - passive_xmin
print("active vowel dur:")
print(active_vowel_dur)
print("passive vowel dur:")
print(passive_vowel_dur)

active_period = extract_period("/Users/stenknutsen/Desktop/IO_folder/" + active_filename)
print("active period:")
print(active_period)
passive_period = extract_period("/Users/stenknutsen/Desktop/IO_folder/" + passive_filename)
print("passive period:")
print(passive_period)

#let the swapping begin!
#
new_active_vowel_dur = active_vowel_dur
new_passive_vowel_dur = passive_vowel_dur

while (new_active_vowel_dur<passive_vowel_dur):
    new_active_vowel_dur = new_active_vowel_dur + active_period


while (new_passive_vowel_dur>active_vowel_dur):
    new_passive_vowel_dur = new_passive_vowel_dur - passive_period

print("new active vowel dur:")
print(new_active_vowel_dur)
print("new passive vowel dur:")
print(new_passive_vowel_dur)


#Find percentage increase/decrease for active/passive
#
percent_lengthen_active = (new_active_vowel_dur/active_vowel_dur)-1
print("percent lengthen active:")
print(percent_lengthen_active)

percent_shorten_passive = (-1)*(1-(new_passive_vowel_dur/passive_vowel_dur))
print("percent shorten passive:")
print(percent_shorten_passive)


#Create log for set of files
#
create_log(active_filename,passive_filename,active_vowel_dur,passive_vowel_dur,active_period,
           passive_period,new_active_vowel_dur,new_passive_vowel_dur,percent_lengthen_active,percent_shorten_passive)

vowel_strectching_time(active_filename, active_xmin, active_xmax, percent_lengthen_active)
vowel_strectching_time(passive_filename, passive_xmin, passive_xmax, percent_shorten_passive)








