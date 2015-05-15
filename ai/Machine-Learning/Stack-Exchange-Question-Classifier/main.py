from __future__ import division
from sklearn import svm, preprocessing
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import json

def solve():
    training = []
    annotation = []
    # download training file and sample test file from the problem description
    # url: https://www.hackerrank.com/challenges/stack-exchange-question-classifier

    with open("training.json") as f:
        f.readline()
        for line in f:
            data = json.loads(line)
            annotation.append(data['topic'])
            training.append(data['question'])

    count_vect = CountVectorizer(ngram_range = (1, 2), \
                                token_pattern = r'\b\w+\b',\
                                min_df = 1)
    training_counts = count_vect.fit_transform(training)

    tfidf_transformer = TfidfTransformer()
    training_tfidf = tfidf_transformer.fit_transform(training_counts)

    classifier = svm.LinearSVC().fit(training_tfidf, annotation)

    q = int(raw_input())
    qs = []
    for _ in range(q):
        data = json.loads(raw_input().strip())
        qs.append(data['question'])

    qs_counts = count_vect.transform(qs)
    qs_tfidf = tfidf_transformer.transform(qs_counts)
    ans = classifier.predict(qs_tfidf)

    for a in ans:
        print a

if __name__ == '__main__':
    solve()
