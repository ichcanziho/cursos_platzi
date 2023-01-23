import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error


def train_test_split_kf(data: np.array, target: np.array, train: np.array, test: np.array) -> np.array:
    x_train = data[train]
    x_test = data[test]
    y_train = target[train]
    y_test = target[test]
    return x_train, x_test, y_train, y_test


def evaluate_model(model, metric, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    score = metric(y_pred, y_test)
    return score


def main():
    dataset = pd.read_csv("../datasets/happiness.csv")
    data = dataset.drop(["country", "score", "rank"], axis=1)
    target = dataset["score"]

    models = {"DecisionTreeRegressor": DecisionTreeRegressor()}
    print('---- Easy Implementation ----')
    for name, model in models.items():
        score = cross_val_score(model, data, target, cv=3, scoring='neg_mean_squared_error')
        print("Scores:", score)
        print("Mean score: ", np.abs(np.mean(score)))
    print("=" * 64)

    kf = KFold(n_splits=3, shuffle=True, random_state=42)
    scores = []
    print('---- Full Implementation ----')
    for name, model in models.items():
        print(f"I'm evaluating: {name}")
        for n_fold, (train, test) in enumerate(kf.split(data)):
            print(f"\t-I'm running fold {n_fold + 1}")
            x_train, x_test, y_train, y_test = train_test_split_kf(data.values, target.values, train, test)
            score = evaluate_model(model, mean_squared_error, x_train, x_test, y_train, y_test)
            print("\t\t-score:", score)
            scores.append(score)
        print("="*64)
        print("Scores:", scores)
        print("Mean score: ", np.mean(scores))


if __name__ == '__main__':
    main()
