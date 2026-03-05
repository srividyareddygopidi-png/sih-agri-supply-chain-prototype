import streamlit as st
from PIL import Image
import qrcode
from io import BytesIO

# --- Page selection ---
st.sidebar.title("Khetza Prototype")
page = st.sidebar.radio("Go to", ["Farmer Login", "Batch Creation", "Payment", 
                                  "Warehouse QC", "QR & Trust Score", "Buyer Login", 
                                  "Buyer Profiles", "IVR Service"])

# --- Farmer Login ---
if page == "Farmer Login":
    st.title("Farmer Login")
    farmer_name = st.text_input("Enter your name")
    farmer_id = st.text_input("Enter Farmer ID")
    if st.button("Login"):
        st.success(f"Welcome, {farmer_name}!")

# --- Batch Creation ---
elif page == "Batch Creation":
    st.title("Create Batch")
    crop_name = st.text_input("Crop Name")
    quantity = st.number_input("Quantity (kg)", min_value=1)
    harvest_date = st.date_input("Harvest Date")
    if st.button("Create Batch"):
        st.success(f"Batch for {crop_name} ({quantity} kg) created!")

# --- Payment ---
elif page == "Payment":
    st.title("Instant Payment")
    batch_id = st.text_input("Enter Batch ID")
    amount = st.number_input("Payment Amount", min_value=0)
    if st.button("Pay Farmer"):
        st.success(f"Payment of ₹{amount} done for Batch {batch_id}!")

# --- Warehouse QC ---
elif page == "Warehouse QC":
    st.title("Warehouse Quality Check")
    batch_id = st.text_input("Enter Batch ID for QC")
    quality = st.selectbox("Quality Status", ["Good", "Average", "Poor"])
    trust_score = st.slider("Assign Trust Score", 0, 100, 50)
    if st.button("Submit QC"):
        st.success(f"Batch {batch_id} QC done. Trust Score: {trust_score}")

# --- QR & Trust Score ---
elif page == "QR & Trust Score":
    st.title("QR Code & Trust Info")
    info = st.text_area("Enter info to encode in QR", "Batch details, farmer info, cost...")
    if st.button("Generate QR"):
        qr_img = qrcode.make(info)
        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        st.image(buf, caption="QR Code for Batch")
        st.info("Trust score displayed along with batch info.")

# --- Buyer Login ---
elif page == "Buyer Login":
    st.title("Buyer Login")
    buyer_name = st.text_input("Enter Buyer Name")
    buyer_id = st.text_input("Enter Buyer ID")
    if st.button("Login"):
        st.success(f"Welcome, {buyer_name}!")

# --- Buyer Profiles ---
elif page == "Buyer Profiles":
    st.title("Buyer Profiles")
    st.table({
        "Buyer ID": ["B001", "B002", "B003"],
        "Name": ["Company A", "Company B", "Company C"],
        "Previous Orders": [5, 2, 0]
    })

# --- IVR Service ---
elif page == "IVR Service":
    st.title("IVR Service Simulation")
    st.write("Simulate voice interaction for uneducated farmers.")
    choice = st.selectbox("Choose Option", ["Check Payment", "Check Batch Status", "Contact Support"])
    if st.button("Proceed"):
        st.success(f"You selected: {choice}")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.markdown("Prototype by Khetza - Blockchain-based Farmer App")