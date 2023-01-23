import pandas as pd
from sklearn.cluster import MeanShift
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def main():
    dataset = pd.read_csv('../datasets/candy.csv')
    X = dataset.drop('competitorname', axis=1)
    meanshift = MeanShift(bandwidth=None)
    meanshift.fit(X)
    print(meanshift.labels_)
    # Aquí el algoritmo nos devolvió 3 clusters, porque le pareció que esa era la cantidad
    # correcta teniendo en cuenta como se distrubuye la densidad de nuestros datos
    print(max(meanshift.labels_))
    print('=' * 64)
    # Imprimamos la ubicación de los centros que puso sobre nuestros datos.
    # Hay que recordar que estos algoritmos crean un centro y
    # a partir de ahí se ajustan a todos los datos que lo rodean
    print(meanshift.cluster_centers_)
    cname = "meanshift"
    dataset[cname] = meanshift.labels_
    print('=' * 64)
    print(dataset.head())
    sns.pairplot(dataset[['sugarpercent', 'pricepercent', 'winpercent', cname]], hue=cname, palette='colorblind')
    plt.savefig("meanshift.png")
    plt.show()


if __name__ == "__main__":
    main()
