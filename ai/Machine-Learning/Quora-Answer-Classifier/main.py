from __future__ import division
from sklearn import svm, preprocessing
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

def solve():
    n, m = map(int, raw_input().strip().split())
    params = []
    annotations = []
    names = []

    for _ in range(n):
        line = raw_input().strip().split()
        params.append(map(lambda x: float(x.split(':')[1]), line[2:]))
        annotations.append(int(line[1]))

    q = int(raw_input())

    for _ in range(q):
        line = raw_input().strip().split()
        params.append(map(lambda x: float(x.split(':')[1]), line[1:]))
        names.append(line[0])

    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    # params = sel.fit_transform(params)

    # clf = svm.LinearSVC(max_iter = 3000, dual = False)
    clf = RandomForestClassifier(min_samples_split = 4, criterion = "entropy")

    params_normalized = preprocessing.normalize(params, axis = 0)

    params_scaled = preprocessing.scale(params_normalized)

    clf.fit(params_scaled[:-q], annotations)

    ans = clf.predict(params_scaled[-q:])

    for i in range(len(names)):
        print '%s %+d' % (names[i], ans[i])

if __name__ == '__main__':
    solve()
