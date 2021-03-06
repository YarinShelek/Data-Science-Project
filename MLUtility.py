import pandas as pd
from sklearn import metrics
from sklearn.metrics import make_scorer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt
from Consts import Consts


def read_csv():
    with open(Consts.Clean_Data_File, "r") as DataFile:
        df = pd.read_csv(DataFile)
        return df.drop("Rank", axis=1), pd.Series(df["Rank"])

def factorize(Column):
    return Column.replace(Consts.replace_map)

def std_scale_df(dataset):
    scaler = StandardScaler()
    return scaler.fit_transform(dataset), scaler

def MM_scale_df(dataset):
    scaler = MinMaxScaler(feature_range=(0, 1))
    return scaler.fit_transform(dataset), scaler

def get_model(type, ml_df, rank_df, n=0):
    if type == "SVC":
        return SVC().fit(ml_df, rank_df)
    if type == "RF":
        return RandomForestClassifier(n_estimators=n).fit(ml_df, rank_df)
    if type == "KNN":
        return KNeighborsClassifier(n_neighbors=n).fit(ml_df, rank_df)
    if type == "DT":
        return DecisionTreeClassifier(max_depth=n[0], min_samples_split=n[1]).fit(ml_df, rank_df)
    if type == "Bayes":
        return GaussianNB().fit(ml_df, rank_df)
    if type == "NN":
        return MLPClassifier(random_state=69).fit(ml_df, rank_df)

def calc_evaluation_val(eval_metric, y_test, y_predicted):
    if eval_metric == 'accuracy':
        evaluation_val = metrics.accuracy_score(y_true=y_test, y_pred=y_predicted)
    if eval_metric == 'precision':
        evaluation_val = metrics.precision_score(y_true=y_test, y_pred=y_predicted, average="weighted")
    if eval_metric == 'recall':
        evaluation_val = metrics.recall_score(y_true=y_test, y_pred=y_predicted, average="weighted")
    if eval_metric == 'f1':
        evaluation_val = metrics.f1_score(y_true=y_test, y_pred=y_predicted, average="weighted")
    if eval_metric == 'confusion_matrix':
        evaluation_val = metrics.confusion_matrix(y_true=y_test, y_pred=y_predicted)
    return evaluation_val

def find_best_estimators(type,X_train, y_train):
    if type == "KNN":
        parameters = {'n_neighbors': range(3,20)}
        rf = KNeighborsClassifier()
    if type == "RF":
        parameters = {'n_estimators': range(3,20)}
        rf = RandomForestClassifier()
    if type == "DT":
        parameters = {'max_depth':range(3,20),"min_samples_split":range(3,20)}
        rf = DecisionTreeClassifier()

    clf = GridSearchCV(rf, parameters,scoring=make_scorer(metrics.f1_score, average="weighted"))
    clf.fit(X_train, y_train)
    if type == "KNN":
        best_num_estimators = clf.best_params_['n_neighbors']
    if type == "RF":
        best_num_estimators = clf.best_params_['n_estimators']
    if type == "DT":
        best_num_estimators = [clf.best_params_["max_depth"], clf.best_params_["min_samples_split"]]

    return best_num_estimators


def scale_palyer_data(scaler, player_df):
    return scaler.transform(np.array(player_df).reshape(-1, 9))

def predict_player_rank(player_df):
    ml_df, rank_df = read_csv()
    rank_df = factorize(rank_df)
    scaled_df, scaler = std_scale_df(ml_df)
    X_train, _, y_train, _ = train_test_split(scaled_df, rank_df, test_size=0.2, random_state=42)
    model = get_model("NN", X_train, y_train)
    scaled_player = scale_palyer_data(scaler, player_df)
    result = model.predict(scaled_player)[0]
    probab = model.predict_proba(scaled_player)[0]
    labels = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Apex"]
    plt.figure()
    wedges, texts = plt.pie(probab, labels=labels, colors=Consts.Color_List, textprops={"color": "Gold"}) #https://stackoverflow.com/questions/54564641/different-colors-for-each-label-in-my-pie-chart
    for text, color in zip(texts, Consts.Color_List):
        text.set_color(color)
    plt.savefig("Plots/PiePlot.png", transparent=True)
    return Consts.replace_list[result], Consts.Color_List[result]
