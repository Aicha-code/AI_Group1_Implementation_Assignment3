# expert_system.py

# Define the diseases and their symptoms
diseases = {
    "Powdery Mildew": {
        "symptoms": ["white powdery spots", "yellowing of leaves", "leaf curling"]
    },
    "Leaf Rust": {
        "symptoms": ["orange or yellow spots", "rust-colored lesions", "deformed leaves"]
    },
    "Blight": {
        "symptoms": ["dark lesions", "wilting", "yellowing around the edges"]
    },
    "Healthy": {
        "symptoms": ["no symptoms", "healthy green leaves"]
    }
}

# Function to match symptoms with diseases
def diagnose_disease(symptoms):
    matches = []
    for disease, details in diseases.items():
        common_symptoms = set(symptoms).intersection(set(details["symptoms"]))
        if common_symptoms:
            matches.append((disease, len(common_symptoms)))
    
    # Sort matches by number of common symptoms
    matches.sort(key=lambda x: x[1], reverse=True)

    if matches:
        best_match = matches[0]
        return best_match[0]  # Disease name
    else:
        return "Unknown Disease"

# Example function to get prevention tips based on disease
def get_prevention_tips(disease):
    prevention_tips = {
        "Powdery Mildew": "Ensure proper spacing between plants, remove infected leaves, and apply fungicides.",
        "Leaf Rust": "Use resistant varieties, remove infected leaves, and apply fungicides.",
        "Blight": "Ensure proper irrigation, remove infected plant material, and apply fungicides.",
        "Healthy": "No intervention required.",
        "Unknown Disease": "Consult an expert for diagnosis."
    }
    return prevention_tips.get(disease, "No tips available for this disease.")
