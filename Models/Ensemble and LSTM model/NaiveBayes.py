from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from preprocessing import wordEmbeddings
import os
import matplotlib.pyplot as plt
import numpy as np
try:
    import scikitplot.plotters as skplt
except ImportError:
    os.sys.exit(0)


def utills():
    if not os.path.isfile('./xtr.npy') or not os.path.isfile('./xte.npy') or not os.path.isfile('./ytr.npy') or not os.path.isfile('./yte.npy'):
        print('generating doc2vec transforms on dataset')
        xtr, xte, ytr, yte = wordEmbeddings(
            os.path.join(os.getcwd(), 'train.csv'))
        np.save('./xtr', xtr)
        np.save('./xte', xte)
        np.save('./ytr', ytr)
        np.save('./yte', yte)

    print('testing on pretrained sample dataset')
    xtr = np.load('./xtr.npy')
    xte = np.load('./xte.npy')
    ytr = np.load('./ytr.npy')
    yte = np.load('./yte.npy')
    gnb = GaussianNB()
    gnb.fit(xtr, ytr)
    y_pred = gnb.predict(xte)
    m = yte.shape[0]
    n = (yte != y_pred).sum()
    print("Accuracy = " + format(round((m-n)/m*100, 2)) + "%")   # 72.94%
    # Draw the confusion matrix
    skplt.confusion_matrix(yte, y_pred)
    plt.show()


utills()

# utills()
# gnb.fit()
