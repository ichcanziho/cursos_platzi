import pandas as pd
from sklearn.linear_model import RANSACRegressor, HuberRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")
import seaborn as sns
sns.set()


def read_split_data(data, x_columns, y_column, test_size, rs):
    dataset = pd.read_csv(data)
    X = dataset[x_columns]
    y = dataset[[y_column]]
    return train_test_split(X, y, test_size=test_size, random_state=rs)


def main():
    input_cols = ["gdp", "family", "lifexp", "freedom", "generosity", "corruption", "dystopia"]
    target = "score"
    X_train, X_test, y_train, y_test = read_split_data(data="../datasets/happines_corrupt.csv",
                                                       x_columns=input_cols, y_column=target, test_size=0.3, rs=42)

    estimadores = {
        'SVR': SVR(gamma='auto', C=1.0, epsilon=0.1),
        'RANSAC': RANSACRegressor(),  # Meta estimador
        'HUBER': HuberRegressor(epsilon=1.35,)
    }
    # plt.scatter(y_test, y_test)
    # Graficamos
    plt.ylabel('Predicted Score')
    plt.xlabel('Real Score')
    plt.title(f'Predicted VS Real')
    for name, estimador in estimadores.items():
        # Entrenamos
        estimador.fit(X_train, y_train)
        # Predecimos
        predictions = estimador.predict(X_test)
        # Medimos
        mse = mean_squared_error(y_test, predictions)
        print(f'{name} MSE: ', round(mse, 10))
        print('=' * 64)
        plt.scatter(y_test, predictions, label=f'{name}. MSE: {round(mse, 10)}')
        plt.plot(predictions, predictions, "--")
    plt.legend()
    plt.savefig("regresion_results.png")
    plt.show()

    plt.close()


if __name__ == "__main__":
    main()
