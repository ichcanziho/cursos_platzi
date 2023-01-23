import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor


def main():
    dataset = pd.read_csv("../datasets/happiness.csv")
    # La razón de eliminar el rank y el score,
    # es porque se quiere que los features no tengan ninguna correlación entre ellos.
    # Lo ideal es que exista correlación solo entre las features y la variable objetivo.
    data = dataset.drop(['country', 'rank', 'score'], axis=1)
    target = dataset['score']
    reg = RandomForestRegressor()
    parameters = {
        'n_estimators': range(4, 16),  # cuantos arboles compondrán mi arbol
        'criterion': ['friedman_mse', 'squared_error', 'poisson', 'absolute_error'],
        'max_depth': range(2, 11)
    }
    # Son 10 iteraciones del optimizador. Toma 10 combinaciones al azar del diccionario
    # cv = 3, parte en 3 partes el set de datos que le pasemos, para hacer Cross validation
    rand_est = RandomizedSearchCV(reg, parameters, n_iter=10, cv=3, scoring='neg_mean_absolute_error', random_state=17)
    rand_est.fit(data, target)
    print('=' * 64)
    print("Mejores estimadores")
    print('-' * 64)
    print(rand_est.best_estimator_)
    print('=' * 64)
    print("Mejores parámetros")
    print('-' * 64)
    print(rand_est.best_params_)
    print('=' * 64)
    print('Pruebas')
    print('-' * 64)
    y_hat = rand_est.predict(data.loc[[0]])
    print(f'Predict: {y_hat[0]}')
    print(f'Real:    {target.loc[0]}')
    print('=' * 64)


if __name__ == "__main__":
    main()
