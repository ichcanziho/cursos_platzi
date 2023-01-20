import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse


def fit_predict_score(model, x_train, y_train, x_test, y_test, metric) -> float:
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    score = metric(y_test, y_predict)
    return score


def main():
    dataset = pd.read_csv("../datasets/happines.csv")
    print(dataset.describe())
    # Vamos a elegir los features que vamos a usar
    X = dataset[['gdp', 'family', 'lifexp', 'freedom',
                 'corruption', 'generosity', 'dystopia']]
    # Definimos nuestro objetivo, que sera nuestro data set, pero solo en la columna score
    y = dataset[['score']]
    print(X.shape)
    print(y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    models = {"Linear Regression": LinearRegression(),
              "Lasso": Lasso(alpha=0.2),
              "Ridge": Ridge(alpha=1)}

    for name, model in models.items():
        score = fit_predict_score(model, X_train, y_train, X_test, y_test, mse)
        print(f"{name} loss: {score}")
    print("="*32)
    for name, model in models.items():
        print(f"Coef {name}: {model.coef_}")


if __name__ == '__main__':
    main()
