from sklearn.model_selection import train_test_split
import MLUtility as util

#start preparing data
ml_df, rank_df = util.read_csv()

rank_df = util.factorize(rank_df)
scaled_df, scaler = util.std_scale_df(ml_df)
mm_scaled_df, mm_scaler = util.MM_scale_df(ml_df)
scaled_dfs = [mm_scaled_df, scaled_df]
for index, dataframe in enumerate(scaled_dfs):
    X_train, X_test, y_train, y_test = train_test_split(scaled_df, rank_df, test_size=0.2, random_state=42)
    KNN_n, _ = util.find_best_estimators("KNN", X_train, y_train)
    RF_n, _ = util.find_best_estimators("RF", X_train, y_train)
    # end preparing data

    ##GET MODELS
    LR_Model = util.get_model("LR", X_train, y_train)
    KNN_Model = util.get_model("KNN", X_train, y_train, KNN_n)
    RF_Model = util.get_model("RF", X_train, y_train, RF_n)
    SVC_Model = util.get_model("SVC", X_train, y_train)
    ##END GET MODELS

    ##GET PREDICTIONS
    LR_prediction = LR_Model.predict(X_test)
    KNN_prediction = KNN_Model.predict(X_test)
    RF_prediction = RF_Model.predict(X_test)
    SVC_prediction = SVC_Model.predict(X_test)
    ##END GET PREDICTIONS

    LR_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, LR_prediction), 3)
    KNN_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, KNN_prediction), 3)
    RF_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, RF_prediction), 3)
    SVC_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, SVC_prediction), 3)

    LR_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, LR_prediction), 3)
    KNN_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, KNN_prediction), 3)
    RF_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, RF_prediction), 3)
    SVC_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, SVC_prediction), 3)

    df = [{"LR": [f"f1: {LR_prediction_f1}", f"accuracy: {LR_prediction_accuracy}"],
           "SVC":[f"f1: {SVC_prediction_f1}", f"accuracy: {SVC_prediction_accuracy}"],
           "RF":[f"f1: {RF_prediction_f1}", f"accuracy: {RF_prediction_accuracy}"],
           "KNN":[KNN_prediction_f1, KNN_prediction_accuracy]}]
    if index == 0:
        print("STD:", df)
    else:
        print("MM:", df)