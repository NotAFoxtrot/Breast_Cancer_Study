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
    df2 = df.drop(columns=['Regional Node Examined', 'Reginol Node Positive','6th Stage', 'Survival Months', 'Race'])
    df2['Estrogen Status'] = df2['Estrogen Status'].map({'Positive': 1,'Negative': 0})
    df2['Progesterone Status'] = df2['Progesterone Status'].map({'Positive': 1,'Negative': 0})
    df2['Status'] = df2['Status'].map({'Alive':1,'Dead':0})
    df2 = pd.get_dummies(df2, columns=(["Marital Status", "T Stage ", "N Stage", "differentiate", "Grade", "A Stage"]), drop_first=True)
    return df2


def logistic_reg(parsed_df):
    y = parsed_df['Status']
    X = parsed_df.drop('Status', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=44)
    scaler = StandardScaler()
    clf = LogisticRegression()
    X_train= scaler.fit_transform(X_train,y_train)
    X_test= scaler.fit_transform(X_test,y_test)
    clf.fit(X_train, y_train)
    y_pred_proba = clf.predict_proba(X_test)[::,1]
    fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
    auc = metrics.roc_auc_score(y_test, y_pred_proba)
    print(auc)
    plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
    plt.legend(loc=4)
    plt.show()
    coef = clf.coef_[0]
    print(coef)
    plt.plot(coef)
    plt.show()
    print(X.info())

def hypothesis_test_graph(parsed_df):
    new_lst = []
    for i in (range(len(parsed_df.columns))):
        a = parsed_df[parsed_df['Status'] == 1][parsed_df.columns[i]]
        b = parsed_df[parsed_df['Status'] == 0][parsed_df.columns[i]]
        t, p = stats.ttest_ind(a, b, equal_var=False)
        new_lst.append(p)
    tuple_ex = list(zip(parsed_df.columns, new_lst))
    graphing_df = pd.DataFrame(tuple_ex, columns = ['Feature', 'P-Score'])
    plt.plot(graphing_df['Feature'], graphing_df['P-Score'])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def hypothesis_test_single(parsed_df):
    Sur_a = parsed_df[parsed_df['Status'] == 1]['Progesterone Status']
    Sur_b = parsed_df[parsed_df['Status'] == 0]['Progesterone Status']
    print(stats.ttest_ind(Sur_a, Sur_b, equal_var=False))

if __name__ == '__main__':
    path = 'data/Breast_Cancer.csv'
    hypothesis_test_single(data_look(path))
