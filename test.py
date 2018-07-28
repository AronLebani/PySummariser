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
    file = open('techcrunch.txt')
    input = file.read()
    expectedResult = "Magic Leap just updated its developer documentation and a host of new details and imagery are being spread around on Reddit and Twitter, sharing more specifics on how the company’s Lumin OS will look like on their upcoming Magic Leap One device. It’s mostly a large heaping of nitty-gritty details, but we also get a more prescient view into how Magic Leap sees interactions with their product looking and the directions that developers are being encouraged to move in. Alright, first, this is what the Magic Leap One home screen will apparently look like, it’s worth noting that it appears that Magic Leap will have some of its own stock apps on the device, which was completely expected but they haven’t discussed much about."


    result = summariser.summarise(input, 3)
    assert(expectedResult == result)

    # Test 4
    file = open('techcrunch2.txt')
    input = file.read()
    expectedResult = "Magic Leap  still hasn’t released a product, but they’re continuing to raise a lot of cash to get there. The Plantation, Florida-based augmented reality startup announced today that it has raised $461 million from the Kingdom of Saudi Arabia’s sovereign investment arm, The Public Investment Fund. The total Series D funding now stands at $963 million, the company says."

    result = summariser.summarise(input, 3)
    assert(expectedResult == result)

if __name__ == "__main__":
    testSummariser()
