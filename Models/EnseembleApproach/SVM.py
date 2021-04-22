from sklearn.svm import SVC
from preprocessing import wordEmbeddings
import os
import matplotlib.pyplot as plt
import numpy as np
try:
    import scikitplot.plotters as skplt
except ImportError:
    os.sys.exit(0)

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
svc = SVC()
svc.fit(xtr, ytr)
y_pred = svc.predict(xte)
m = yte.shape[0]
n = (yte != y_pred).sum()
print("Accuracy = " + format((m-n)/m*100, '.2f') + "%")
skplt.confusion_matrix(yte, y_pred)
plt.show()
