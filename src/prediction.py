import os,pickle
from preprocessing import prepare_input
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..")); MODEL_PATH=os.path.join(ROOT,"models","student_model.pkl")
class StudentPerformancePredictor:
    def __init__(self,model_path=MODEL_PATH):
        if not os.path.exists(model_path): raise FileNotFoundError("Model not found. Run: python src\\train_model.py")
        with open(model_path,"rb") as f: self.model=pickle.load(f)
    def predict(self,study_hours,attendance,previous_marks,assignment_score,sleep_hours):
        row=prepare_input(study_hours,attendance,previous_marks,assignment_score,sleep_hours); pred=int(self.model.predict(row)[0]); conf=float(max(self.model.predict_proba(row)[0]))*100
        return {"result":"PASS" if pred==1 else "FAIL","confidence":conf}
def number(prompt):
    while True:
        try:return float(input(prompt))
        except ValueError: print("Please enter a valid number.")
if __name__=="__main__":
    print("\n===== STUDENT PERFORMANCE PREDICTOR =====")
    try:
        p=StudentPerformancePredictor(); r=p.predict(number("Study hours per day: "),number("Attendance percentage: "),number("Previous marks percentage: "),number("Assignment score percentage: "),number("Sleep hours per day: ")); print("\nPredicted Result:",r["result"]); print(f"Confidence: {r['confidence']:.2f}%")
    except (ValueError,FileNotFoundError) as e: print("\nError:",e)
