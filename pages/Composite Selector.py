import streamlit as st

# Prevent unauthorized access
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()

st.title("CompApp: Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Selector Version 1.0")
st.write("Click on the properties you want in your composite/polymer. Then fill in the blank spaces with the values of the parameters you desire. The application will provide you a list of composites which are suitable for your project's requirements.")

# Composite Datasets
datasets = {
    "PEEK": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (70, 90), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (50, 60), "Glass Transition Temperature (°C)": (143, 157), "Cost (USD/kg)": (50, 110), "Strength (GPa)": (3.79, 3.95), "Shrinkage (%)": (1.00, 1.21), "Density (kg/m³)": (1300, 1320)},
    "PPS": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (30, 50), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (48.6, 88.2), "Glass Transition Temperature (°C)": (81, 97), "Cost (USD/kg)": (10, 20), "Strength (GPa)": (3.23, 3.39), "Shrinkage (%)": (0.60, 1.40), "Density (kg/m³)": (1340, 1360)},
    "PESU": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 60), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (54.7, 56.9), "Glass Transition Temperature (°C)": (210, 235), "Cost (USD/kg)": (20, 30), "Strength (GPa)": (2.76, 2.90), "Shrinkage (%)": (0.70, 1.00), "Density (kg/m³)": (1360, 1380)},
    "PEI": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (90, 110), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (84.6, 101), "Glass Transition Temperature (°C)": (215, 217), "Cost (USD/kg)": (30, 50), "Strength (GPa)": (2.89, 3.04), "Shrinkage (%)": (0.50, 0.70), "Density (kg/m³)": (1260, 1280)},
    "PC": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (10, 30), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (120, 125), "Glass Transition Temperature (°C)": (142, 158), "Cost (USD/kg)": (2, 4), "Strength (GPa)": (2.32, 2.44), "Shrinkage (%)": (0.50, 0.70), "Density (kg/m³)": (1190, 1210)},
    "PA": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (9.3, 29.3), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (141, 147), "Glass Transition Temperature (°C)": (58, 62), "Cost (USD/kg)": (3, 6), "Strength (GPa)": (0.94, 1.18), "Shrinkage (%)": (1.20, 1.80), "Density (kg/m³)": (1060, 1080)},
    "PEEK 30% GF": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (70, 90), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (15, 20), "Glass Transition Temperature (°C)": (133, 153), "Cost (USD/kg)": (50, 110), "Strength (GPa)": (9, 10), "Shrinkage (%)": (0.20, 1.00), "Density (kg/m³)": (1490, 1540)},
    "PEEK 30% CF": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (70, 90), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (15, 40), "Glass Transition Temperature (°C)": (133, 153), "Cost (USD/kg)": (110, 125), "Strength (GPa)": (13, 20), "Shrinkage (%)": (0.10, 0.40), "Density (kg/m³)": (1420, 1460)},
    "PPS 20-30% GF": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (30, 50), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (10, 40), "Glass Transition Temperature (°C)": (88, 93), "Cost (USD/kg)": (10, 20), "Strength (GPa)": (6, 11), "Shrinkage (%)": (0.20, 0.50), "Density (kg/m³)": (1450, 1550)},
    "PPS 40% GF": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (30, 50), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (10, 30), "Glass Transition Temperature (°C)": (88, 93), "Cost (USD/kg)": (10, 20), "Strength (GPa)": (8, 14), "Shrinkage (%)": (0.20, 0.50), "Density (kg/m³)": (1600, 1700)},
    "PPS 20% CF": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (30, 50), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (10, 20), "Glass Transition Temperature (°C)": (88, 93), "Cost (USD/kg)": (10, 20), "Strength (GPa)": (16, 18), "Shrinkage (%)": (0.20, 0.50), "Density (kg/m³)": (1350, 1450)},
    "PPS GF + MINERAL": {"Interfacial Properties with Carbon Fiber (IFSS, MPa)": (30, 50), "Coefficient Thermal Expansion (CTE) (µstrain/°C)": (10, 20), "Glass Transition Temperature (°C)": (88, 93), "Cost (USD/kg)": (10, 20), "Strength (GPa)": (10, 17), "Shrinkage (%)": (0.30, 0.70), "Density (kg/m³)": (1800, 2000)}
}

all_properties = set()
for dataset in datasets.values():
    all_properties.update(dataset.keys())

if "selected_properties" not in st.session_state:
    st.session_state.selected_properties = set()

for prop in sorted(all_properties):
    if st.button(f"Filter by {prop}"):
        if prop in st.session_state.selected_properties:
            st.session_state.selected_properties.remove(prop)
        else:
            st.session_state.selected_properties.add(prop)

user_inputs = {}

for prop in st.session_state.selected_properties:
    user_inputs[prop] = st.number_input(f"Enter value for property {prop}:", min_value=0.00, step=0.01)

matching_datasets = []
for dataset, properties in datasets.items():
    match = True
    for prop in st.session_state.selected_properties:
        if not (properties[prop][0] <= user_inputs[prop] <= properties[prop][1]):
            match = False
            break  

    if match:
        matching_datasets.append(dataset)

if matching_datasets:
    result = f"The input values match with dataset(s): **{', '.join(matching_datasets)}**"
elif st.session_state.selected_properties:
    result = "No dataset includes the selected values."
else:
    result = "Please select at least one property to filter by."

st.write(result)
