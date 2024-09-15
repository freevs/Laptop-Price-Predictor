import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Import the model and DataFrame
pipe_voting = pickle.load(open('pipe_voting.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Predictor")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Company', df['Company'].unique())
    type_name = st.selectbox('Type', df['TypeName'].unique())
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input('Weight of the Laptop', format="%.2f")
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('IPS', ['No', 'Yes'])

with col2:
    screen_size = st.number_input('Screen Size of the Laptop', format="%.2f")
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())
    os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # Query processing
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create DataFrame for query with correct column names
    query_df = pd.DataFrame({
        'Company': [company],
        'TypeName': [type_name],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'Ips': [ips],
        'ppi': [ppi],
        'Cpu brand': [cpu],
        'Gpu brand': [gpu],
        'os': [os],
        'HDD': [hdd],
        'SSD': [ssd]
    })

    # Ensure the column names in query_df match exactly what is expected by ColumnTransformer
    expected_columns = ['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'ppi', 'Cpu brand', 'Gpu brand', 'os', 'HDD', 'SSD']
    for col in expected_columns:
        if col not in query_df.columns:
            st.error(f"Missing column: {col}")
            break

    # Predict price
    if all(col in query_df.columns for col in expected_columns):
        predicted_price = pipe_voting.predict(query_df)[0]
        st.markdown(f"<h1 style='text-align: center; color: #FF5733;'>₹{int(np.exp(predicted_price))}</h1>", unsafe_allow_html=True)
