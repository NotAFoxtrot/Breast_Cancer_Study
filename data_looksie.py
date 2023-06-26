from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import scipy.stats as stats 
import sklearn.metrics as metrics 
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_recall_fscore_support, classification_report, roc_curve, confusion_matrix, RocCurveDisplay, auc



def data_look(filepath):
    df = pd.read_csv(filepath)
    df2 = df.drop(columns=['Regional Node Examined', 'Reginol Node Positive','6th Stage'])
    df2['Estrogen Status'] = df2['Estrogen Status'].map({'Positive': 1,'Negative': 0})
    df2['Progesterone Status'] = df2['Progesterone Status'].map({'Positive': 1,'Negative': 0})
    df2['Status'] = df2['Status'].map({'Alive':1,'Dead':0})
    df2 = pd.get_dummies(df2, columns=(["Race", "Marital Status", "T Stage ", "N Stage", "differentiate", "Grade", "A Stage"]), drop_first=True)
    return df2


def logistic_reg(parsed_df):
    y = parsed_df['Status']
    X = parsed_df.drop('Status', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=44)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    y_pred_proba = clf.predict_proba(X_test)[::,1]
    fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
    auc = metrics.roc_auc_score(y_test, y_pred_proba)
    plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
    plt.legend(loc=4)
    plt.show()
    print(clf.coef_)
    print(X.info())

if __name__ == '__main__':
    path = 'data/Breast_Cancer.csv'
    logistic_reg(data_look(path))
