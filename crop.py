import streamlit as st

# Expanded disease knowledge base with Cassava added

disease_data = {
    "Maize": {
        "Maize Lethal Necrosis": {
            "symptoms": ["Yellowing leaves", "Drying of young leaves", "Wilting", "Stunted growth", "Necrosis on leaves"],
            "advice": "Destroy affected plants, use virus-free seeds, and control insect vectors."
        },
        "Common Rust": {
            "symptoms": ["Red-brown spots on leaves", "Powdery pustules on both leaf surfaces", "Yellowing around spots", "Reduced yield"],
            "advice": "Apply fungicides, use resistant varieties, and rotate crops."
        },
        "Gray Leaf Spot": {
            "symptoms": ["Gray rectangular lesions", "Necrotic spots merging to form large dead areas", "Leaf curling"],
            "advice": "Improve field drainage, apply foliar fungicides, and avoid excessive nitrogen use."
        }
    },
    "Coffee": {
        "Coffee Leaf Rust": {
            "symptoms": ["Yellow-orange spots on leaves", "Premature leaf drop", "Defoliation", "Reduced coffee yield"],
            "advice": "Prune infected leaves, apply copper-based fungicides, and maintain plant nutrition."
        },
        "Coffee Berry Disease": {
            "symptoms": ["Dark spots on berries", "Shriveled berries", "Premature berry drop"],
            "advice": "Remove infected berries, spray fungicides, and ensure good air circulation."
        },
        "Fusarium Wilt": {
            "symptoms": ["Wilting", "Yellowing of lower leaves", "Brown discoloration in stems"],
            "advice": "Use resistant coffee varieties and avoid waterlogging."
        }
    },
    "Avocado": {
        "Root Rot": {
            "symptoms": ["Wilting leaves", "Dark roots", "Poor fruit development", "Leaf yellowing"],
            "advice": "Improve soil drainage, avoid overwatering, and apply phosphite-based treatments."
        },
        "Anthracnose": {
            "symptoms": ["Black sunken lesions on fruit", "Leaf tip dieback", "Dark spots on stems"],
            "advice": "Harvest early, apply copper-based fungicides, and store fruits in a dry environment."
        },
        "Avocado Sunblotch": {
            "symptoms": ["Yellow streaks on leaves", "Cracked bark", "Deformed fruit"],
            "advice": "Use virus-free seedlings and remove infected trees."
        }
    },
    "Bananas": {
        "Panama Disease": {
            "symptoms": ["Yellowing leaves", "Wilting", "Stem splitting", "Dark streaks inside the pseudostem"],
            "advice": "Use resistant varieties, avoid infected soil, and maintain proper drainage."
        },
        "Black Sigatoka": {
            "symptoms": ["Black streaks on leaves", "Premature leaf drop", "Yellowing between veins"],
            "advice": "Prune infected leaves, apply fungicides, and increase potassium fertilizer."
        },
        "Banana Bunchy Top Virus": {
            "symptoms": ["Leaves bunched at the top", "Dark green streaks on leaf veins", "Stunted growth"],
            "advice": "Destroy infected plants and control aphid vectors."
        }
    },
    "Cassava": {
        "Cassava Mosaic Disease": {
            "symptoms": ["Yellowing leaves", "Mosaic leaf pattern", "Distorted leaves", "Stunted growth"],
            "advice": "Use virus-free planting materials, control whiteflies, and remove infected plants."
        },
        "Cassava Brown Streak Disease": {
            "symptoms": ["Brown streaks on stems", "Root necrosis", "Yellowing leaves", "Reduced yield"],
            "advice": "Plant resistant cassava varieties and remove infected plants promptly."
        },
        "Bacterial Blight": {
            "symptoms": ["Water-soaked lesions on leaves", "Wilted leaves", "Gummy exudate on stems"],
            "advice": "Ensure proper field sanitation, use disease-free cuttings, and rotate crops."
        }
    }
}

# Streamlit App
st.title("🌱 Plant Disease Expert System")
st.write("Select a plant and check the symptoms you observe to diagnose possible diseases.")

# Select Plant
plant = st.selectbox("🌿 Select a Plant", list(disease_data.keys()))

# Display Checkboxes for Symptoms
if plant:
    st.subheader("✔️ Select Symptoms")
    all_symptoms = {symptom for disease in disease_data[plant].values() for symptom in disease["symptoms"]}
    selected_symptoms = {symptom: st.checkbox(symptom) for symptom in all_symptoms}

    # Diagnose Disease
    if st.button("🔍 Diagnose"):
        user_selected_symptoms = [symptom for symptom, checked in selected_symptoms.items() if checked]
        best_match = None
        max_matches = 0

        # Find the disease with the most matching symptoms
        for disease, details in disease_data[plant].items():
            match_count = sum(1 for symptom in details["symptoms"] if symptom in user_selected_symptoms)
            if match_count > max_matches:
                max_matches = match_count
                best_match = (disease, details["advice"])

        # Display Results
        if best_match:
            disease, advice = best_match
            st.success(f"Detected Disease: {disease}")
            st.info(f"Advice: {advice}")
        else:
            if user_selected_symptoms:
                st.warning("No disease found. Try selecting more symptoms.")
            else:
                st.write("General Advice: Ensure proper watering, fertilization, and pest control.")

# Footer 
st.markdown("""
    <hr style="border:1px solid gray">
    <p style="text-align:center; color:gray;">© Group1 INES-Ruhengeri SWE3 A 2025<br> Github Repository: <a href="https://github.com/Aicha-code/AI_Group1_Implementation_Assignment3">Link</a></p>
""", unsafe_allow_html=True)
