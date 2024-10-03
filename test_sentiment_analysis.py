import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        #Caso para positive sentiment
        resultado1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(resultado1['label'],'SENT_POSITIVE')

        #Caso para negative sentiment
        resultado2 = sentiment_analyzer('I hate working with Pyhton')
        self.assertEqual(resultado2['label'], 'SENT_NEGATIVE')

        #Caso para neutral sentiment
        resultado3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(resultado3['label'], 'SENT_NEUTRAL')

unittest.main()