from core.utils import Utils
from core.models import Models


def main():
    model = Models()
    df = Utils.load_from_csv("data/heart.csv")
    data, target = Utils.feature_target(dataset=df, drop_cols=["target"], y="target")
    best_model, score = model.get_best_model(x=data, y=target)
    print(best_model, score)
    Utils.model_export(clf=best_model, score=score, path="models")


if __name__ == '__main__':
    main()

