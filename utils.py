import requests

def encode(var=str, values=str):
    """
    Encode a variable.
    """
    try:
        data = {"GENDER": ("Male", "Female"),
                "MARRIAGE": ("Married", "Single", "Other"),
                "EDUCATION": ("Graduate School", "University", "High School", "Others")}
        
        if var == "GENDER":
            return data[var].index(values)

        return data[var].index(values) + 1
    except:
        return

def predict(features):
    """
    Predict the default risk.
    """
    # Check connection
    URL = "https://default-prediction.onrender.com"
    
    req = requests.get(URL)
    if req.status_code != 200:
        return "Error: Cannot connect to the server !"
    
    URL += "/predict"
    result = requests.post(URL, json={"data": [features]})
    return result.json()