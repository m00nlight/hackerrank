from __future__ import division
from sklearn import svm, preprocessing
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from collections import defaultdict
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingRegressor
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def feature_selection(data, name_map, win, lose):
    features = [0] * 97

    for i in range(5):
        features[name_map[data[i]]] = 1.0

    for i in range(5, 10):
        features[name_map[data[i]]] = -1.0

    # for hero in data:
    #   features.append(win[hero] / (win[hero] + lose[hero]))

    # features.append(sum([sigmoid(win[x] - lose[x]) for x in data[:5]]))
    # features.append(sum([sigmoid(win[x] - lose[x]) for x in data[5:10]]))

    return features

def solve():
    params = []
    annotations = []
    cc = 0
    name_map = {}
    win, lose = defaultdict(int), defaultdict(int)

    with open("trainingdata.txt") as f:
        for line in f:
            data = line.strip().split(',')
            for hero in data[:-1]:
                if not hero in name_map:
                    name_map[hero] = cc
                    cc += 1
            if int(data[-1]) == 1:
                for hero in data[:5]:
                    win[hero] += 1
                for hero in data[5:10]:
                    lose[hero] += 1
            else:
                for hero in data[:5]:
                    lose[hero] += 1
                for hero in data[5:10]:
                    win[hero] += 1

            params.append(feature_selection(data[:-1], name_map, win, lose))
            annotations.append(int(data[-1]) if int(data[-1]) == 1 else -1)


    classifier = LogisticRegression(C = 0.1)
    #classifier = RandomForestClassifier(n_estimators = 10)
    classifier.fit(params, annotations)

    q = int(raw_input())
    for _ in range(q):
        data = raw_input().strip().split(',')
        
        res = classifier.predict(feature_selection(data, name_map, win, lose))[0]
        print 1 if res == 1 else 2

if __name__ == '__main__':
    solve()
