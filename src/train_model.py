import os,pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from data_loader import load_data
from preprocessing import prepare_data
from evaluation import evaluate_model
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..")); DATA_PATH=os.path.join(ROOT,"data","student_performance.csv"); MODEL_PATH=os.path.join(ROOT,"models","student_model.pkl")
def train():
    print("Loading dataset..."); df=load_data(DATA_PATH); print(f"Loaded {len(df)} records.")
    X,y=prepare_data(df); Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.20,random_state=42,stratify=y)
    print("Training Decision Tree..."); model=DecisionTreeClassifier(max_depth=20,min_samples_leaf=10,random_state=42); model.fit(Xtr,ytr)
    m=evaluate_model(model,Xte,yte); print(f"Accuracy : {m['accuracy']:.2%}"); print(f"Precision: {m['precision']:.2%}"); print(f"Recall   : {m['recall']:.2%}"); print(f"F1 Score : {m['f1_score']:.2%}"); print("Confusion Matrix:"); print(m["confusion_matrix"])
    os.makedirs(os.path.dirname(MODEL_PATH),exist_ok=True)
    with open(MODEL_PATH,"wb") as f: pickle.dump(model,f)
    print(f"\nModel saved successfully: {MODEL_PATH}")
if __name__=="__main__": train()
