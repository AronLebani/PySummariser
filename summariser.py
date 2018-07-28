from utilities import Utilities

class Summariser:

    def __init__(self):
        self.utes = Utilities()

    def findMaxValue(self, list):
        list.sort(reverse=True)
        return list[0]

    def getMostFrequentWords(self, count, wordFrequencies):
        return self.utes.getMostFrequentWords(count, wordFrequencies)

    def reorderSentences(self, sentences, input):
        # Reorder sentences to the order they were in the original text
        orderHash = {}
        outputSentences = []
        for sentence in sentences:
            idx = input.index(sentence)
            orderHash[idx] = sentence

        for key in sorted(orderHash):
            outputSentences.append(orderHash[key])

        return outputSentences

    def summarise(self, input, numSentences):
        # Get the frequency of each word in the input
        wordFrequencies = self.utes.getWordFrequency(input)

        # Now create a set of the X most frequent words
        mostFrequentWords = self.getMostFrequentWords(100, wordFrequencies)

        # Break the input up into sentences
        # workingSentences is used for the analysis, but
        # actualSentences is used in the results so that the
        # capitalisation will be correct
        workingSentences = self.utes.getSentences(input.lower())
        actualSentences = self.utes.getSentences(input)

        # Iterate over the most frequent words, and add the first sentence
        # that includes each word to the result
        outputSentences = set()
        for word in mostFrequentWords:
            for sentence in workingSentences:
                if word.lower() in sentence:
                    idx = workingSentences.index(sentence)
                    outputSentences.add(actualSentences[idx])
                    break
                if len(outputSentences) >= numSentences:
                    break
            if len(outputSentences) >= numSentences:
                break

        reorderedOutputSentences = self.reorderSentences(outputSentences, input)

        result = ""
        for sentence in reorderedOutputSentences:
            result += sentence
            result += "."  # This isn't always correct - perhaps it should be whatever symbol the sentence finished with
            if sentence != list(reorderedOutputSentences)[len(reorderedOutputSentences)-1]:
                result += " "

        return result
