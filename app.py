import streamlit as st
import numpy as np
import joblib

# Modeli yükle
model = joblib.load('svm_diabetes_model.pkl')

# Sayfa başlığı
st.title("Diyabet Tahmin Uygulaması")

st.markdown("""
Bu uygulama, kullanıcıdan alınan medikal verilerle kişide diyabet riski olup olmadığını tahmin eder.
""")

# Kullanıcıdan veri alma formu
pregnancies = st.number_input('Gebelik sayısı', min_value=0, max_value=20, value=1)
glucose = st.number_input('Glikoz seviyesi', min_value=0, max_value=300, value=120)
blood_pressure = st.number_input('Kan basıncı', min_value=0, max_value=200, value=70)
skin_thickness = st.number_input('Deri kalınlığı', min_value=0, max_value=100, value=20)
insulin = st.number_input('İnsülin seviyesi', min_value=0, max_value=900, value=79)
bmi = st.number_input('BMI (Vücut Kitle İndeksi)', min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input('Yaş', min_value=1, max_value=120, value=33)

# Tahmin butonu
if st.button('Tahmin Et'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Yüksek diyabet riski tespit edildi.")
    else:
        st.success("✅ Düşük diyabet riski.")

