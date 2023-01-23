import pandas as pd
from sklearn.cluster import MiniBatchKMeans
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def main():
    dataset = pd.read_csv('../datasets/candy.csv')
    print(dataset.head())
    # al ser aprendizaje no supervisado, no separamos nuestro datasets en partes
    # eliminaremos los nombres de los caramelos, ya que eso no nos sirve para el algoritmo
    X = dataset.drop('competitorname', axis=1)
    kmeans = MiniBatchKMeans(n_clusters=4, batch_size=8)
    kmeans.fit(X)
    print('Total de centros: ', len(kmeans.cluster_centers_))
    print('=' * 64)
    col_name = "clusters"
    dataset[col_name] = kmeans.predict(X)
    print(dataset)
    sns.pairplot(dataset[['sugarpercent', 'pricepercent', 'winpercent', col_name]], hue=col_name, palette='colorblind')
    plt.savefig("pares.png")
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()
