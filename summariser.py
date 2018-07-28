from utilities import Utilities

class Summariser:

    def __init__(self):
        self.utes = Utilities()

    def findMaxValue(list):
        list.sort(reverse=True)
        return list[0]

    def getMostFrequentWords(count, wordFrequencies):
        return self.utes.getMostFrequentWords(count, wordFrequencies)

    def reorderSentences(sentences, input):
        # Reorder sentences to the order they were in the original text
        return sentences

    def summarise(input, numSentences):
        # Get the frequency of each word in the input
        wordFrequencies = self.utes.getWordFrequency(input)

        # Now create a set of the X most frequent words
        mostFrequentWords = self.getMostFrequentWords(100, wordFrequencies)

        # Break the input up into sentences
        # workingSentences is used for the analysis, but
        # actualSentences is used in the results so that the
        # capitalisation will be correct
        workingSentences = self.utes.getSentences(input.toLower())
        actualSentences = self.utes.getSentences(input)

        # Iterate over the most frequent words, and add the first sentence
        # that includes each word to the result
        outputSentences = []
        for word in mostFrequentWords:
            for index in range(workingSentences):
                if workingSentences[index].indexOf(word) >= 0:  # indexOf is a java function. Need to work out exactly what this does...
                    outputSentences.append(actualSentences[i])
                    break
                if len(outputSentences) >= numSentences:
                    break
            if len(outputSentences) >= numSentences:
                break

        reorderedOutputSentences = self.reorderSentences(outputSentences, input)

        result = ""
        for sentence in reorderedOutputSentences:
            result.append(sentence)
            result.append(".")  # This isn't always correct - perhaps it should be whatever symbol the sentence finished with
            if sentence != reorderedOutputSentences[len(reorderedOutputSentences)]:
                # Last sentence
                result.append(" ")

        return result
