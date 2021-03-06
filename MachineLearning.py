from sklearn.model_selection import train_test_split
import MLUtility as util

def ml(standalone=True):
    #start preparing data
    ml_df, rank_df = util.read_csv()
    if standalone == False:
        STD = {}
        MM = {}
    rank_df = util.factorize(rank_df)
    scaled_df, scaler = util.std_scale_df(ml_df)
    mm_scaled_df, mm_scaler = util.MM_scale_df(ml_df)
    scaled_dfs = [mm_scaled_df, scaled_df]
    for index, dataframe in enumerate(scaled_dfs):
        X_train, X_test, y_train, y_test = train_test_split(scaled_df, rank_df, test_size=0.2, random_state=42)
        if standalone == True:
            KNN_n= util.find_best_estimators("KNN", X_train, y_train)
            RF_n = util.find_best_estimators("RF", X_train, y_train)
            DT_n = util.find_best_estimators("DT", X_train, y_train)
        if standalone == False: #manually input previously known best n's
            KNN_n  = 19
            DT_n = [8,13]
            RF_n  = 15
        # end preparing data

        ##GET MODELS
        KNN_Model = util.get_model("KNN", X_train, y_train, KNN_n)
        RF_Model = util.get_model("RF", X_train, y_train, RF_n)
        SVC_Model = util.get_model("SVC", X_train, y_train)
        DT_Model = util.get_model("DT", X_train, y_train, DT_n)
        NN_Model = util.get_model("NN", X_train, y_train)
        Bayes_Model = util.get_model("Bayes", X_train, y_train)
        ##END GET MODELS

        ##GET PREDICTIONS
        KNN_prediction = KNN_Model.predict(X_test)
        RF_prediction = RF_Model.predict(X_test)
        SVC_prediction = SVC_Model.predict(X_test)
        DT_prediction = DT_Model.predict(X_test)
        NN_prediction = NN_Model.predict(X_test)
        Bayes_prediction = Bayes_Model.predict(X_test)
        ##END GET PREDICTIONS

        KNN_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, KNN_prediction), 3)
        RF_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, RF_prediction), 3)
        SVC_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, SVC_prediction), 3)
        DT_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, DT_prediction), 3)
        NN_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, NN_prediction), 3)
        Bayes_prediction_f1 = round(util.calc_evaluation_val("f1", y_test, Bayes_prediction), 3)

        KNN_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, KNN_prediction), 3)
        RF_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, RF_prediction), 3)
        SVC_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, SVC_prediction), 3)
        DT_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, DT_prediction), 3)
        NN_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, NN_prediction), 3)
        Bayes_prediction_accuracy = round(util.calc_evaluation_val("accuracy", y_test, Bayes_prediction), 3)

        df = [{"SVC":[f"f1: {SVC_prediction_f1}", f"accuracy: {SVC_prediction_accuracy}"],
               "RF":[f"f1: {RF_prediction_f1}", f"accuracy: {RF_prediction_accuracy}"],
               "KNN":[f"f1: {KNN_prediction_f1}", f"accuracy: {KNN_prediction_accuracy}"],
              "DT": [f"f1: {DT_prediction_f1}", f"accuracy: {DT_prediction_accuracy}"],
              "NN": [f"f1: {NN_prediction_f1}", f"accuracy: {NN_prediction_accuracy}"],
              "Bayes": [f"f1: {Bayes_prediction_f1}", f"accuracy: {Bayes_prediction_accuracy}"]}]
        if standalone == True:
            if index == 0:
                print("STD:", df)
            else:
                print("MM:", df)

        if standalone == False:
            if index == 0:
                STD["KNN"] = [KNN_n, KNN_prediction_f1, KNN_prediction_accuracy]
                STD["RF"] = [RF_n, RF_prediction_f1, RF_prediction_accuracy]
                STD["SVC"] = [0, SVC_prediction_f1, SVC_prediction_accuracy]
                STD["DT"] = [DT_n, DT_prediction_f1, DT_prediction_accuracy]
                STD["NN"] = [0, NN_prediction_f1, NN_prediction_accuracy]
                STD["Bayes"] = [0, Bayes_prediction_f1, Bayes_prediction_accuracy]
            else:
                MM["KNN"] = [KNN_n, KNN_prediction_f1, KNN_prediction_accuracy]
                MM["RF"] = [RF_n, RF_prediction_f1, RF_prediction_accuracy]
                MM["SVC"] = [0, SVC_prediction_f1, SVC_prediction_accuracy]
                MM["DT"] = [DT_n, DT_prediction_f1, DT_prediction_accuracy]
                MM["NN"] = [0, NN_prediction_f1, NN_prediction_accuracy]
                MM["Bayes"] = [0, Bayes_prediction_f1, Bayes_prediction_accuracy]
    if standalone == False:
        return [STD, MM]
if __name__ == "__main__": #we do this cause we want to use the data from here in the ml page, but also want to leave the option to run this as a standalone
    ml()