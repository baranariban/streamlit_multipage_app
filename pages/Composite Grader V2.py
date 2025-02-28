import streamlit as st

# Prevent unauthorized access
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()

import pandas as pd

st.title("CompApp - Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Grader Version 2.0")
st.write("Write the thermal and physical properties of the composite below. For each property, also write the weighing. The application will provide you a grade out of 3 and a total grade out of 100.") 

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Type of the composite", "Interfacial Properties with Carbon Fiber Grade", "Coefficient of Thermal Expansion Grade", "Glass Transition Temperature Grade", "Cost Grade", "Strength Grade", "Processing Temperature Grade", "Shrinkage Grade", "Density Grade", "Total Grade"])

composite = st.text_input("Type of the composite (UNFILLED, GF, CF, MINERAL, CONDUCTIVE): ")
col1, col2 = st.columns(2)
with col1:
    ifss = st.number_input("Interfacial Properties with Carbon Fiber (IFSS, in MPa): ")
with col2:
    ifss_weighing = st.number_input("Weighing of Interfacial Properties with Carbon Fiber (%): ")

col3, col4 = st.columns(2)
with col3:
    cte = st.number_input("Coefficient of Thermal Expansion (CTE, in microstrain/°C): ")
with col4:
    cte_weighing = st.number_input("Weighing of Coefficient of Thermal Expansion (%): ")

col5, col6 = st.columns(2)
with col5:
    tg = st.number_input("Glass Transition Temperature (Tg, in °C): ")
with col6:
    tg_weighing = st.number_input("Weighing of Glass Transition Temperature (%): ")

col7, col8 = st.columns(2)
with col7:
    cost = st.number_input("Cost (in USD/kg): ")
with col8:
    cost_weighing = st.number_input("Weighing of Cost (%): ")

col9, col10 = st.columns(2)
with col9:
    strength = st.number_input("Strength (Tensile Modulus or Flexural Modulus, in GPa): ")
with col10:
    strength_weighing = st.number_input("Weighing of Strength (%): ")

col11, col12 = st.columns(2)
with col11:
    tp = st.number_input("Processing Temperature (Tp, in °C): ")
with col12:
    tp_weighing = st.number_input("Weighing of Processing Temperature (%): ")

col13, col14 = st.columns(2)
with col13:
    shrinkage = st.number_input("Shrinkage (in %): ")
with col14:
    shrinkage_weighing = st.number_input("Weighing of Shrinkage (%): ")

col15, col16 = st.columns(2)
with col15:
    density = st.number_input("Density (in kg/m^3): ")
with col16:
    density_weighing = st.number_input("Weighing of Density (%): ")

if ifss_weighing+cte_weighing+tg_weighing+cost_weighing+strength_weighing+tp_weighing+shrinkage_weighing+density_weighing<100 or ifss_weighing+cte_weighing+tg_weighing+cost_weighing+strength_weighing+tp_weighing+shrinkage_weighing+density_weighing>100:
    st.markdown("### :red[WARNING: Make sure that the sum of the weighings equals 100!]")

if ifss>=100:
    ifss_grade = 3.00
else:
    ifss_grade = 3.00 - 3.00*((100-ifss)/100)
    ifss_grade = round(ifss_grade,2)

if composite in ["UNFILLED", "CF", "MINERAL", "CONDUCTIVE"]:
    if cte == 7.5:
        cte_grade = 3.00
    elif 0 < cte < 7.5:
        cte_grade = round(3.00 - 3.00 * ((7.5 - cte) / 7.5), 2)
    elif 7.5 < cte < 144:
        cte_grade = round(3.00 - 3.00 * ((cte - 7.5) / (144 - 7.5)), 2)
    else:
        cte_grade = 0
elif composite == "GF":  
    if cte == 22.5:
        cte_grade = 3.00
    elif 0 < cte < 22.5:
        cte_grade = round(3.00 - 3.00 * ((22.5 - cte) / 22.5), 2)
    elif 22.5 < cte < 40:
        cte_grade = round(3.00 - 3.00 * ((cte - 22.5) / (40 - 22.5)), 2)
    else:
        cte_grade = 0
else:
    cte_grade = 0  

if tg<180:
    tg_grade = 0
elif tg>=180:
    tg_grade = 3.00

if cost>=117.5:
    cost_grade = 0
else:
    cost_grade = 3.00 - 3.00*((0-cost)/(0-117.5))
    cost_grade = round(cost_grade,2)

if strength>=18:
    strength_grade = 3.00
else:
    strength_grade = 3.00 - 3.00*((18-strength)/(18-0))
    strength_grade = round(strength_grade,2)

if tp<=119.5:
    tp_grade = 3.00
elif tp>=400:
    tp_grade = 0
else:
    tp_grade = 3.00 - 3.00*((119.5-tp)/(119.5-400))
    tp_grade = round(tp_grade,2)

if shrinkage<=0.5:
    shrinkage_grade = 3.00
elif shrinkage>=1.5:
    shrinkage_grade = 0
else:
    shrinkage_grade = 3.00 - 3.00*((0.5-shrinkage)/(0.5-1.5))
    shrinkage_grade = round(shrinkage_grade,2)

if density == 1400:
    density_grade = 3.00
elif 1000 < density < 1400:
    density_grade = 3.00 - 3.00*((1400-density)/(1400-1000))
    density_grade = round(density_grade,2)
elif 2000 > density > 1400:
    density_grade = 3.00 - 3.00*((1400-density)/(1400-2000))
    density_grade = round(density_grade,2)
else:
    density_grade = 0

total_grade = ((ifss_grade*ifss_weighing)+(cte_grade*cte_weighing)+(tg_grade*tg_weighing)+(cost_grade*cost_weighing)+(strength_grade*strength_weighing)+(tp_grade*tp_weighing)+(shrinkage_grade*shrinkage_weighing)+(density_grade*density_weighing))/3.00
total_grade = round(total_grade,2)

st.write("The individual and total grades are given below.")

if st.button("Add Column"):
    new_row = pd.DataFrame({
    "Type of the composite": [composite],
    "Interfacial Properties with Carbon Fiber Grade": [ifss_grade],
    "Coefficient of Thermal Expansion Grade": [cte_grade],
    "Glass Transition Temperature Grade": [tg_grade],
    "Cost Grade": [cost_grade],
    "Strength Grade": [strength_grade],
    "Processing Temperature Grade": [tp_grade],
    "Shrinkage Grade": [shrinkage_grade],
    "Density Grade": [density_grade],
    "Total Grade": [total_grade]
})
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)

st.write(st.session_state.data.T)
