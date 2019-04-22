import csv
import os
import nltk

#
# this program goes through all the reviews/text in the train/test file and remove the words/characters which are not alpha 
#

# test_otherStopWordsRemoved.csv is our output file 
# change the path of the file accordingly, we used ours..
exists = os.path.isfile('C:\\Users\\Shivalika\\.spyder-py3\Correct\DoubleCorrect\test_otherStopWordsRemoved.csv')
if exists:
    # if the output file test_otherStopWordsRemoved.csv exists, then remove it
    os.remove("test_otherStopWordsRemoved.csv")
# if the output file test_otherStopWordsRemoved.csv does not exist, then create one
f= open("test_otherStopWordsRemoved.csv","w+")
# test.csv is our input file, to read from  
with open('test.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    row_count = 0
    for row in csv_reader:
        if row_count != 0: #this is to not evaluate the first column which is text and class 
            # extracting the words into tokens
            tokens = nltk.word_tokenize(row[0])
            
            result = []
            for a in tokens:
                if a.isalpha():
                    result.append(a) #only adding the tokens which contain all alpha letters to the array result
            
            result = " ".join(str(x) for x in result)
            f.write(result+"\n") # writing the result array into the output file
        row_count = row_count + 1
# close both input and output files
csvfile.close() 
f.close() 

