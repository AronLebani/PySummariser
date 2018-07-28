from summariser import Summariser

def testSummariser():
    input = "Classifier4J is a java package for working with text. Classifier4J includes a summariser."
    expectedResult = "Classifier4J is a java package for working with text."

    summariser = Summariser()
    result = summariser.summarise(input, 1)
    assert(expectedResult == result);

    input = "Classifier4J is a java package for working with text. Classifier4J includes a summariser. A Summariser allows the summary of text. A Summariser is really cool. I don't think there are any other java summarisers.";
    expectedResult = "Classifier4J is a java package for working with text. Classifier4J includes a summariser.";

    result = summariser.summarise(input, 2);
    assert(expectedResult == result);

if __name__ == "__main__":
    testSummariser()
