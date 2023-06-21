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
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_recall_fscore_support, classification_report


def data_look(filepath):
    df = pd.read_csv(filepath)
    df2 = df.drop(columns=['Regional Node Examined', 'Reginol Node Positive','6th Stage'])
    df2['Estrogen Status'] = df2['Estrogen Status'].map({'Positive': True,'Negative': False})
    df2['Progesterone Status'] = df2['Progesterone Status'].map({'Positive': True,'Negative': False})
    df2['Status'] = df2['Status'].map({'Alive':True,'Dead':False})
    df2.sample(4)

if __name__ == '__main__':
    path = 'data/Breast_Cancer.csv'
    data_look(path)