from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


class PreProcessor:
    def readFile(self, path):
        try:
            return pd.read_csv(path)
        except BaseException as e:
            print("Error in reading file", e)
    
    def showHead(self, df):
        try:
            return df.head()
        except BaseException as e:
            print("Error in Showing head", e)

    def showTail(self, df):
        try:
            return df.tail()
        except BaseException as e:
            print("Error in Showing tail", e)
    

    def encodeTIPO(self, df):
        try:
            return df['TIPO'].map({'Maligna': 1, 'Benigna': 0})
        except BaseException as e:
            print("Error in encodeTIPO", e)

    def describeTheDataFrame(self, df):
        try:
            return df.describe(include='all')
        except BaseException as e:
            print("Error in describing the DF", e)

    def getCorrMatrix(self, df):
        try:
            return df.corr()
        except BaseException as e:
            print("Error in building Correlation Matrix", e)

    def getUpperCorrMatrix(self, df):
        try:
            matrix = self.getCorrMatrix(df)
            return matrix.where(np.triu(np.ones(matrix.shape), k=1).astype(np.bool))
        except BaseException as e:
            print("Error in building Upper Correlation Matrix", e)

    def getHighCorrColumns(self, df):
        try:
            highCorrList = []
            for i, j in df.iterrows():
                if j.TIPO > 0.1 or j.TIPO < -0.1:
                    highCorrList.append(i)
            # print(highCorrList)
            return highCorrList
        except BaseException as e:
            print("Error in building Correlation Matrix", e)

    def getColumnsToDrop(self, df, highCorrList):
        try:
            to_drop = [x for x in df.columns if x not in highCorrList]
            to_drop.remove('TIPO')
            return to_drop
        except BaseException as e:
            print("Error in getColumnsToDrop", e)

    def dropColumns(self, df, toDrop):
        try:
            return df.drop(columns=toDrop)
        except BaseException as e:
            print("Error in dropColumns", e)

    def checkNullAndDropNa(self, df):
        try:
            df[pd.isnull(df).any(axis=1)]
            df=df.dropna()
            return df
        except BaseException as e:
            print("Error in checkNullAndInterPolate", e)

    def saveData(self, df, file):
        try:
            dataset_with_dummies = pd.get_dummies(df, prefix_sep='--')
            dataset_with_dummies.to_csv(file+'.csv')
        except BaseException as e:
            print("Error in dropColumns", e)
    
    def extractXY(self, li):
        try:
            x=[]
            y=[]
            for i in li:
                x.append(i[0])
                y.append(i[1])
            return x,y
        except BaseException as e:
            print("Error in dropColumns", e)


class GraphBuilder:
    def buildHeatMap(self, df):
        try:
            return seaborn.heatmap(df.drop(['URL', 'CHARSET', 'SERVER'], axis=1).corr())
        except BaseException as e:
            print("Error in Building Heat Map", e)

    def buildCorrHeatMap(self, df, dropList):
        try:
            return seaborn.heatmap(df.drop(dropList, axis=1).corr(), annot=True, cmap="crest")
            # return seaborn.heatmap(df.drop(['CONTENT_LENGTH','TCP_CONVERSATION_EXCHANGE','DNS_QUERY_TIMES','APP_PACKETS','SOURCE_APP_BYTES','REMOTE_APP_BYTES','SOURCE_APP_PACKETS','REMOTE_APP_PACKETS','DIST_REMOTE_TCP_PORT','APP_BYTES','UDP_PACKETS'],axis=1).corr(),annot=True,cmap="crest")
        except BaseException as e:
            print("Error in BuildingCoorelation Heat Map", e)

    def buildBoxPlot(self, df, x, y):
        try:
            return seaborn.boxplot(data=df, x=x, y=y)
        except BaseException as e:
            print("Error in Building Box Plot", e)

    def buildHistogram(self, df):
        try:
            return df.hist()
        except BaseException as e:
            print("Error in Building Histogram", e)

    def buildBarPlot(self, xList, yList):
        try:
            plt.rcParams["figure.autolayout"] = True
            plt.bar(xList, yList)
            return plt.xticks(rotation=90)
        except BaseException as e:
            print("Error in Building BarPlot", e)


class ModelBuilder:

    def splitData(self, X, y):
        try:
            return train_test_split(X, y, test_size=0.3, random_state=42)
        except BaseException as e:
            print("Error in splitData", e)

    def forestClassifier(self):
        try:
            return RandomForestClassifier(n_estimators=100, n_jobs=-1, max_depth=30, criterion='entropy')
        except BaseException as e:
            print("Error in forestClassifier", e)

    def xgClassifier(self):
        try:
            return xgb.XGBClassifier()
        except BaseException as e:
            print("Error in xgClassifier", e)

    def fit(self, model, X_train, y_train):
        try:
            model.fit(X_train, y_train)
            print('Training Accuracy Score: {}'.format(
                model.score(X_train, y_train)))
            return model
        except BaseException as e:
            print("Error in fit", e)

    def predict(self, model, X_test):
        try:
            return model.predict(X_test)
        except BaseException as e:
            print("Error in predict", e)

    def testScores(self, model, X_test, y_test):
        try:
            print("Test results:\n")
            print('Accuracy Score: {0:.4f}\n'.format(
                accuracy_score(y_test, model.predict(X_test))))
            print('Classification Report:\n{}\n'.format(
                classification_report(y_test, model.predict(X_test))))
            print('Confusion Matrix:\n{}\n'.format(
                confusion_matrix(y_test, model.predict(X_test))))
        except BaseException as e:
            print("Error in getting scores", e)

    def printImpFeature(self, model, X):
        try:
            original_feature_dict = {}
            for feature, importance in zip(list(X), model.feature_importances_):
                # Check for our dummy variable delimeter --
                if '--' in feature:
                    original_feature_name = feature.split('--')[0]
                else:
                    original_feature_name = feature
                # Add to our original_feature_dict, incrememnt if it's already there
                if original_feature_name in original_feature_dict:
                    original_feature_dict[original_feature_name] += importance
                else:
                    original_feature_dict[original_feature_name] = importance
            # Sort the original_feature_dict
            sorted_importance = sorted(
                original_feature_dict.items(), key=lambda x: x[1], reverse=True)
            for feature, importance in sorted_importance:
                print(feature, importance)
            return sorted_importance
        except BaseException as e:
            print("Error in printImpFeature", e)
