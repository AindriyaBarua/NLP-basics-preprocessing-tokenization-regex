#1.a Import the regex module
import re
#2.a Import the sent_tokenize and word_tokenize functions from nltk.tokenize.
from nltk.tokenize import word_tokenize, sent_tokenize, TweetTokenizer, regexp_tokenize
my_string = "Let's write some RegularExpressions!  All should participate equally. Won't that be great?  All 56 students must upload the assignments"
#1.b Write a pattern to match sentence endings:
print(re.findall("[.?!]",my_string))

print(re.split('[A-Za-z]*[.?!]\?!',my_string))
#1.d Find all capitalized words in my_string and print the result
print(re.findall(r"[A-Z]\w+",my_string))
#1.e Split my_string on spaces and print the result
print(re.split(r"\s",my_string))
#1.f Find all digits in my_string and print the result
print(re.findall(r"\d+", my_string))
#2.b Tokenize all the sentences using the sent_tokenize() function.
r1 = sent_tokenize(my_string)
print(r1)
#2.c Tokenize the fourth sentence, which you can access as sentences[3], using the word_tokenize() function.
print(word_tokenize(r1[3]))
#2.d Find the unique tokens by using word_tokenize() and then converting it into a set using set().
r2 = word_tokenize(my_string)
r3 = set(r2)
print(r3)
my_string_2 = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
string = re.split(r"#\d\w+\?!",my_string_2)
print(string)
tweets=['I’ve retrieved the best #nlp exercise  for the class till now! It is done #python',      '#NLP is super cool!   #learning', 'Thanks @analytics :) #nlp #python']
pattern1 = r"#\w+"
print(regexp_tokenize(tweets[1],pattern1))
pattern2 = r"[#|@]\w+"
print(regexp_tokenize(tweets[2],pattern2))
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)
