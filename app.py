import streamlit as st
from expert_system import diagnose_disease, get_prevention_tips

# Streamlit UI Styling
st.set_page_config(page_title="Crop Disease Expert System", page_icon="🌱", layout="wide")
st.title("🌿 Crop Disease Expert System 🌾")
st.write("This system helps in detecting and preventing crop diseases based on symptoms you provide.")

# Add a header section
st.markdown(
    """
    <style>
    .css-1v3fvcr {
        background-color: #88c99d;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Available symptoms and diseases
symptom_dict = {
    "Powdery Mildew": {
        "symptoms": ["white powdery spots", "yellowing of leaves", "leaf curling"],
        "icon": "fas fa-cloud-sun"
    },
    "Leaf Rust": {
        "symptoms": ["orange or yellow spots", "rust-colored lesions", "deformed leaves"],
        "icon": "fas fa-sun"
    },
    "Blight": {
        "symptoms": ["dark lesions", "wilting", "yellowing around the edges"],
        "icon": "fas fa-cloud-showers-heavy"
    },
    "Healthy": {
        "symptoms": ["no symptoms", "healthy green leaves"],
        "icon": "fas fa-leaf"
    }
}

# Dropdown for symptoms
st.sidebar.header("Step 1: Select Symptoms")
symptoms_selected = []

# Display symptom options with icons
for disease, data in symptom_dict.items():
    st.sidebar.subheader(f"{disease} ({data['icon']})")
    for symptom in data["symptoms"]:
        if st.sidebar.checkbox(symptom):
            symptoms_selected.append(symptom)

# Diagnose disease if symptoms are selected
if symptoms_selected:
    st.write(f"**Symptoms Selected**: {', '.join(symptoms_selected)}")

    # Call the expert system for disease diagnosis
    disease = diagnose_disease(symptoms_selected)
    st.write(f"**Predicted Disease**: {disease}")

    # Prevention tips based on the disease
    prevention_tips = get_prevention_tips(disease)
    st.write(f"**Prevention Tips**: {prevention_tips}")
else:
    st.write("Please select symptoms from the sidebar to diagnose the disease.")

# Footer with credits
st.markdown(
    """
    <footer style="text-align:center;">
        <p>Made with ❤️ by Your AI Crop Disease Team | 🌾</p>
    </footer>
    """,
    unsafe_allow_html=True
)
