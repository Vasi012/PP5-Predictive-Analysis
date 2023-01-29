import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.file_management import load_clean_data, load_pkl_file
from src.eval_pipeline_perf import regression_performance
from src.eval_pipeline_perf import regression_evaluation_plots


def page_predict_sale_price_body():

    # load sale price pipeline files
    ver = 'v2'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"
    sale_price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    feat_importance = pd.read_csv(f"{path}/feature_importance.csv")
    feat_importance_plot = plt.imread(f"{path}/feature_importance.png")
    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")
    y_train = pd.read_csv(f"{path}/y_train.csv")
    y_test = pd.read_csv(f"{path}/y_test.csv")

    st.write("### ML Pipeline: Predict House Sale Price")
    # display pipeline training summary conclusions
    st.warning(
        f"The Regressor model has been chosen to predict the sale price "
        f"for a given property.\n"
        f"* Both feature selection and PCA produced similar results and meet "
        f"business requirement 1. However, the feature selection "
        f"performed better. Therefore, the best pipeline to use will be "
        f"that. \n"
        f"* Feature selection achieved an R2 Score: 0.97 on the train set and "
        f"an R2 Score: 0.78 on the test set.\n"
        f"* My niece has required an R2 Score of 0.75+.\n"
        )
    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline to predict sale price")
    st.info(sale_price_pipe)
    st.write("---")

    # show best features
    st.write("### The features used to train the model and their importance:")
    cnt = 0
    for feat_str in feat_importance['Feature'].sort_values():
        if cnt == 0:
            new_str = feat_str
            cnt = 1
        else:
            new_str = new_str + ', ' + feat_str

    st.write(new_str)
    st.image(feat_importance_plot)
    st.write("---")

    # evaluate pipeline performance
    st.write("### Evaluating the Pipeline Performance.")
    regression_performance(X_train, y_train, X_test, y_test, sale_price_pipe)
    regr_eval_plots = plt.imread(f"{path}/regression_evaluation_plots.png")
    st.image(regr_eval_plots)
    st.write("---")
