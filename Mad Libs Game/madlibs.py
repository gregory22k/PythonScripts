import re
#mad lib template

class MadLibs:
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
        
#user input
    
word_descriptions = []
words = []
sentence = []
final = []


with open("template.txt") as myfile:
    for myline in myfile.read().split():
        
        myline = myline.lower()
        if 'adjective' in myline:
            word_descriptions.append('adjective')
        elif 'noun' in myline:
            word_descriptions.append('noun')
        elif 'verb,' in myline:
            word_descriptions.append('verb, past tense')
        elif 'adverb' in myline:
            word_descriptions.append('adverb')
        elif 'verb' in myline:
            word_descriptions.append('verb')
    
    
print("Please provide the following types of words: ")
for desc in word_descriptions:
    user_input = input(desc +': \n')
    words.append(user_input)

fuckoff = '''Today I went to the zoo. I saw a(n)
___________(1.adjective) _____________(2.noun) jumping up and down in its tree.
He _____________(3.verb, past tense) __________(4.adverb)
through the large tunnel that led to its _______(5.adjective)
__________(6.noun). I got some peanuts and passed
them through the cage to a gigantic gray _______(7.noun)
towering above my head. Feeding that animal made
me hungry. I went to get a __________(8.adjective) scoop
of ice cream. It filled my stomach. Afterwards I had to
__________(9.verb) __________ (10.adverb) to catch our bus.
When I got home I __________(11.verb, past tense) my
mom for a __________(12.adjective) day at the zoo.'''
print(words)

for i in range(12):
    pattern = (r'\_+\s?\(\d+\.\s?[a-zA-Z,\s]+\)')
    print(words[i])
    fuckoff = re.sub(pattern,words[i],fuckoff)
    
print(fuckoff)

