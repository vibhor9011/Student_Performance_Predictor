from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
def evaluate_model(model,X_test,y_test):
    p=model.predict(X_test)
    return {"accuracy":accuracy_score(y_test,p),"precision":precision_score(y_test,p,zero_division=0),"recall":recall_score(y_test,p,zero_division=0),"f1_score":f1_score(y_test,p,zero_division=0),"confusion_matrix":confusion_matrix(y_test,p)}
