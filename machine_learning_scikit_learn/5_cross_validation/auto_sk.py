import pandas as pd
from sklearn.model_selection import train_test_split
from autosklearn.classification import AutoSklearnClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from pprint import pprint


def main():

    df = pd.read_csv("../datasets/heart.csv")
    data = df.drop(columns=["target"])
    target = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=17)
    print("Instanciando clasificador")
    cls = AutoSklearnClassifier(time_left_for_this_task=120, n_jobs=4, seed=5, per_run_time_limit=30)
    print("Entrenando modelo")
    cls.fit(x_train, y_train)
    print("Realizando predicciones")
    y_pred = cls.predict(x_test)
    score = roc_auc_score(y_test, y_pred)
    # View the models found by auto-sklearn
    print(cls.leaderboard())
    # Print the final ensamble constructed by auto-sklearn
    pprint(cls.show_models(), indent=4)
    acc = accuracy_score(y_test, y_pred)
    print("Accuracy score:", acc)
    print("AUC:", score)


if __name__ == '__main__':
    main()
