'''
Given a .txt file that has a list of a bunch of
names, count how many of each name there are in
the file, and print out the results to the screen.
I have a .txt file for you, if you want to use it!

Instead of using the .txt file from above (or instead
of, if you want the challenge), take this .txt file,
and count how many of each “category” of each image
there are. This text file is actually a list of
files corresponding to the SUN database scene
recognition database, and lists the file directory
hierarchy for the images. Once you take a look at
the first line or two of the file, it will be
clear which part represents the scene category.
'''
import pprint

#make count dictionary to keep track of each category
counter = {}
path = "C:\\Users\\Chris\\Desktop\\this_is_a_test.txt"

with open(path,'r') as f:
    #reads the first line
    line = f.readline()
    #if next line exists
    while line:
        #removes whitespace
        line = line.strip()
        if line in counter:
            counter[line] +=1
        else:
            counter[line] = 1
        #makes sure we move to the next line
        line = f.readline()
pprint.pprint(counter)
