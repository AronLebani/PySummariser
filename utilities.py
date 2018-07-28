import re
import operator
import nltk

class Utilities:

    def __init__(self):
        self.punctuationChars = '[.!?]'
        self.sentenceEnders = '[.!?]'

    def findWordsWithFrequency(self, wordFrequencies, frequency):
        if wordFrequencies is None or frequency is None:
            return []
        else:
            results = []
            for word in wordFrequencies:
                if wordFrequencies[word] == frequency:
                    results.append(word)

            return results

    def getMostFrequentWords(self, count, wordFrequencies):
        result = []

        freq = wordFrequencies[max(wordFrequencies, key=wordFrequencies.get)]

        while len(result) < count and freq > 0:
            words = self.findWordsWithFrequency(wordFrequencies, freq)
            result += words
            freq -= 1

        return result

    def getWordFrequency(self, paragraph, caseSensitive=True):
        convertedParagraph = paragraph
        if not caseSensitive:
            convertedParagraph = paragraph.lower()

        # Remove punctuation characters
        paragraph = re.sub(self.punctuationChars, '', paragraph)

        # Split paragraph into words and sort
        words = paragraph.split(" ")
        words.sort()

        uniqueWords = self.getUniqueWords(words)

        result = {}
        for word in uniqueWords:
            result[word] = self.countWords(word, words)

        return result

    def getUniqueWords(self, words):
        if words is None:
            return ''
        else:
            result = set()
            for word in words:
                result.add(word)

            return result

    def countWords(self, wordToCount, words):
        counter = 0
        for word in words:
            if wordToCount == word:
                counter += 1

        return counter

    def getSentences(self, paragraph):
        # Split sentences
        sentenceEnders = re.compile(self.sentenceEnders)
        paragraph = sentenceEnders.split(paragraph)

        # Remove leading and trailing whitespace
        paragraph[:] = [sentence.strip() for sentence in paragraph]

        return paragraph

    def removeWordsOfType(self, words, type):
        taggedWords = nltk.pos_tag(words)

        for word, tag in taggedWords:
            if type == 'noun':
                if tag == ('NN' or 'NNS' or 'NNP' or 'NNPS'):
                    taggedWords.remove((word, tag))
            elif type == 'verb':
                if tag == ('VB' or 'VBD' or 'VBG' or 'VBN' or 'VBP' or 'VBZ'):
                    taggedWords.remove((word, tag))
            elif type == 'adjective':
                if tag == ('JJ' or 'JJR' or 'JJS'):
                    taggedWords.remove((word, tag))
            elif type == 'adverb':
                if tag == ('RB' or 'RBR' or 'RBS'):
                    taggedWords.remove((word, tag))
            elif type == 'pronoun':
                if tag == ('PRP' or 'PRP$'):
                    taggedWords.remove((word, tag))
            elif type == 'wh-pronoun':
                if tag == ('WP' or 'WP$'):
                    taggedWords.remove((word, tag))
            elif type == 'preposition':
                if tag == 'IN':
                    taggedWords.remove((word, tag))
            elif type == 'conjunction':
                if tag == 'CC':
                    taggedWords.remove((word, tag))
            elif type == 'determiner':
                if tag == 'DT':
                    taggedWords.remove((word, tag))

        result = []
        for word, tag in taggedWords:
            result.append(word)

        return result
