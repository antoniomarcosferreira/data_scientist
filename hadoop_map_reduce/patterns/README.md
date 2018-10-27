# Patterns
# Hadoop and Map Reduce
## Project: Inverted index

Write a MapReduce program that creates an index of all words that can be found in the body of a forum post and node ID where they can be found. Do not analyze the HML. Just divide the text into all the blanks, as well as the following characters:.,!?:; Eur-lex.europa.eu eur-lex.europa.eu

For the following questions, enter your responses in the video boxes:

How many times have the word "fantastic" been used in the forums? Be sure to create a case-sensitive index (eg "FANTASTIC" and "FANTASTIC" should be considered the same word).

For second question, list the nodes where the word "fantastically" can be found, separated by commas. The ordering of nodes must be increasing, eg. 1,2,3,4.

You can download the additional dataset [here] (http://content.udacity-data.com/course/hadoop/forum_data.tar.gz). To unzip it, download it to your VM, put the data directory and run: