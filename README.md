pin_generator
=============

This is a pin number generator that is mainly just an exercise in markov probabilities. There's an option to add a file or not, if you don't then it will just give you N number of 4 digit pin numbers. However if you choose to add a file then the program really gets interesting. 

You will need to add a .txt file of words or something for which the program can get some text. project Gutenberg is good for this. Once the file is selected, the program parses out each word and collects counts on individual letters and the letters following them in the word. 

Now in a normal Markov probability the largest count of the letters has the highest statistical probability of following the previous letter. This is used to help make things that are pronounceable. However for pin numbers you want the most random, least predictable numbers. In order to go about this I construct the followers table as normal and then I invert the counts for the table. This way the formerly least probable letters now have a higher probability of being selected. from here 4 letter chains are constructed and then passed to a function which maps all of the letters to the digits 0-9. And from this you get your random pin number.

Honestly this is a fairly trivial program, in terms of the end result, however it was fun to write up.
