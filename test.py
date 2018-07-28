from summariser import Summariser

def testSummariser():
    summariser = Summariser()

    # Test 1
    input = "Classifier4J is a java package for working with text. Classifier4J includes a summariser."
    expectedResult = "Classifier4J is a java package for working with text."

    result = summariser.summarise(input, 1)
    assert(expectedResult == result);

    # Test 2
    input = "Classifier4J is a java package for working with text. Classifier4J includes a summariser. A Summariser allows the summary of text. A Summariser is really cool. I don't think there are any other java summarisers.";
    expectedResult = "Classifier4J is a java package for working with text. Classifier4J includes a summariser.";

    result = summariser.summarise(input, 2);
    assert(expectedResult == result);

    # Test 3
    file = open('texts/techcrunch.txt')
    input = file.read()

    result = summariser.summarise(input, 3)

    # Test 4
    file = open('texts/techcrunch2.txt')
    input = file.read()

    result = summariser.summarise(input, 3)

    # Test 5
    file = open('texts/trump.txt')
    input = file.read()

    result = summariser.summarise(input, 3)

    # Test 6
    file = open('texts/techcrunch3.txt')
    input = file.read()

    result = summariser.summarise(input, 3)

if __name__ == "__main__":
    testSummariser()
