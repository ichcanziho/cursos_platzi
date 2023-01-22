import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore")


def main():
    df_heart = pd.read_csv('../datasets/heart.csv')
    print(df_heart['target'].describe())
    print('=' * 64)
    X = df_heart.drop(['target'], axis=1)
    y = df_heart['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    classifiers = {
        'KNeighbors': KNeighborsClassifier(),
        'LogisticRegression': LogisticRegression(),
        'LinearSCV': LinearSVC(),
        'SVC': SVC(),
        'SGDC': SGDClassifier(),
        'DecisionTree': DecisionTreeClassifier()
    }

    print("Base Results:")
    for name, model in classifiers.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"{name}'s Accuracy:", accuracy_score(y_pred, y_test))

    print('=' * 64)

    print("Bagging Results:")
    for name, estimator in classifiers.items():
        bag_class = BaggingClassifier(base_estimator=estimator, n_estimators=30)
        bag_class.fit(X_train, y_train)
        y_pred = bag_class.predict(X_test)
        print(f"{name}'s Accuracy:", accuracy_score(y_pred, y_test))

    print('=' * 64)


if __name__ == "__main__":
    main()
