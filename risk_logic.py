def predict_risk(bmi, glucose):
    if bmi >= 30 or glucose >= 140:
        return "HIGH RISK"
    else:
        return "LOW RISK"


if __name__ == "__main__":
    result = predict_risk(24.9, 100)
    print("Predicted Risk:", result)
