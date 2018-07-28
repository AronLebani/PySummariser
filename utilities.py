import re
import operator

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
