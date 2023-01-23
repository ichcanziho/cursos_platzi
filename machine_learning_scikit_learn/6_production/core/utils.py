import pandas as pd
import joblib


class Utils:

    @staticmethod
    def load_from_csv(path):
        return pd.read_csv(path)

    @staticmethod
    def load_from_mysql():
        pass

    @staticmethod
    def feature_target(dataset, drop_cols, y):
        X = dataset.drop(drop_cols, axis=1)
        y = dataset[y]
        return X.values, y.values

    @staticmethod
    def model_export(clf, score, path):
        print('Score: ', score)
        score = round(score, 3)
        joblib.dump(clf, f'{path}/best_model_{score}.pkl')

    @staticmethod
    def load_model(path):
        return joblib.load(path)
