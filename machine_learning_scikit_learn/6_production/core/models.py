from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings("ignore")


class Models:

    def __init__(self):
        self.classifiers = {"DecisionTree": DecisionTreeClassifier(),
                            "RandomForest": RandomForestClassifier(),
                            "Bagging_KNN": BaggingClassifier(base_estimator=KNeighborsClassifier(),
                                                             n_jobs=-1, n_estimators=30)
                            }
        self.classifiers_params = {
            "DecisionTree": {"criterion": ["gini", "entropy", "log_loss"],
                             "splitter": ["best", "random"]},
            "RandomForest": {"n_estimators": [50, 100, 150],
                             "criterion": ["gini", "entropy", "log_loss"],
                             "n_jobs": [-1]},
            "Bagging_KNN": {"base_estimator__n_neighbors": [5, 10, 15]}
        }
        self.cv = 3

    def get_best_model(self, x, y):
        best_score = 0
        best_model = None
        for name, model in self.classifiers.items():
            print(f"Im evaluating {name}")
            grid_model = GridSearchCV(model, self.classifiers_params[name], cv=self.cv, scoring='roc_auc')
            grid_model.fit(x, y)
            score = grid_model.best_score_
            if score > best_score:
                best_score = score
                best_model = grid_model.best_estimator_
            print(score, grid_model.best_estimator_)
        return best_model, best_score
