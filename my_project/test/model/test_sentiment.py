import csv
from textblob import TextBlob
import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2] / "src/model"))
from sentiment import extract_sentiment

testdata =["Borussia Dortmund’s loss was heartbreaking as they failed to gain momentums from their  two goals advance. Very disappointing results for our Algerian player Bensebaini.","Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"]
with open('soccer_sentiment_analysis.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for element in csvreader :
        testdata.append(''.join(element))
@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    neg_sentiment = extract_sentiment(sample)

    assert neg_sentiment <= 0
    # assert neg_sentiment >= 0