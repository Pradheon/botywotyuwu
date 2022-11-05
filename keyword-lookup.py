import nltk #Speech tagging. https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/
nltk.download('averaged_perceptron_tagger')

class KeywordLookup:
    def __init__(self, keywords):
        self.keywords = keywords
        self.tag = ""
        self.wordlist = [] #Our txt holding words from questions
        self.questionList = [] #Every CSV question

        self.mostMatched = []

    def lookup(self, keyword):
        #lookup word with nltk and tag doing this to track keywords..
        if keyword not in self.wordlist:
            text = keyword
            word = nltk.pos_tag()
            val = word[0][1]
            #add to file with word and tag

    def matching(self):
        #Find if in our keywords document.. Make a txt with all nouns and verbs implemented in CSV
        for question in self.questionList:
            for word in self.keywords.split():
                if word in self.wordlist:
                    self.match(self, question)
        # Tells us which question input matches most
        matchedQuestion = self.mostMatched.index(max(self.mostMatched))
        print(self.questionList[matchedQuestion]) #The matched question
        #print(answer-to-question)




    def match(self, question):
        #Get question from CSV and check which ones match the most
        splitText = self.keywords.split()
        matches = 0
        for word in splitText:
            if word in question:
                matches = matches + 1
        self.mostMatched.append(matches)




