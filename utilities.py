import re

class Utilities:

    def __init__(self):
        self.punctuationChars = '[.!?]'
        self.sentenceEnders = '[.!?]'

    def findWordsWithFrequency(wordFrequencies, frequecy):
        if wordFrequencies is None or frequency is None:
            return []
        else:
            results = []
            for word in wordFrequencies:
                if wordFrequencies[word] == frequency
                    results.append(word)

            return results

    def getMostFrequentWords(count, wordFrequencies):
        result = []

        max = max(wordFrequencies)

        freq = int(max)
        while len(result) < count and freq > 0:
            words = self.findWordsWithFrequency(wordFrequencies, freq)
            result += words
            freq -= freq

        return result

    def getWordFrequency(paragraph, caseSensitive=True):
        convertedParagraph = paragraph
        if not caseSensitive:
            convertedParagraph = paragraph.toLower()

        # Remove punctuation characters
        paragraph = re.sub(self.punctuationChars, '', paragraph)

        # Split paragraph into words and sort
        words = paragraph.split(" ")
        words.sort()

        uniqueWords = self.getUniqueWords(words)

        result = {}
        for word in uniqueWords:
            result[word] = self.countWords(word, words)

        return results

    def getUniqueWords(words):
        if words is None:
            return ''
        else:
            result = []
            for word in words:
                if word not in result:
                    result.append(word)

            return result

    def countWords(wordToCount, words):
        counter = 0
        for word in words:
            if wordToCount == word:
                counter += 1

        return counter

    def getSentences(paragraph):
        sentenceEnders = re.compile(self.sentenceEnders)
        paragraph = sentenceEnders.split(paragraph)

        return paragraph
