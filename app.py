# 1. IMPORTS (at the top)
import sys
import streamlit as st
import pandas as pd
from datetime import datetime
import base64
import requests
from io import StringIO

# 2. CUSTOM CSS
st.markdown("""
    <style>
    ...your CSS here...
    </style>
""", unsafe_allow_html=True)

# 3. GITHUB FUNCTION (right after CSS, before the form)
def save_to_github(submission):
    try:
        token = st.secrets["github_token"]
        owner = "frankianderson4569-rgb"
        repo = "Beginner_ESOL_Job_Application_Form"
        file_path = "submissions.csv"
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        get_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
        response = requests.get(get_url, headers=headers)
        
        if response.status_code == 200:
            file_data = response.json()
            content = base64.b64decode(file_data["content"]).decode()
            df = pd.read_csv(StringIO(content))
            df = pd.concat([df, pd.DataFrame([submission])], ignore_index=True)
            sha = file_data["sha"]
        else:
            df = pd.DataFrame([submission])
            sha = None
        
        csv_content = df.to_csv(index=False)
        encoded_content = base64.b64encode(csv_content.encode()).decode()
        
        push_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
        payload = {
            "message": f"New job application submission - {submission['Timestamp']}",
            "content": encoded_content,
            "branch": "main"
        }
        
        if sha:
            payload["sha"] = sha
        
        push_response = requests.put(push_url, json=payload, headers=headers)
        
        return push_response.status_code == 201 or push_response.status_code == 200
    except Exception as e:
        st.error(f"Error saving to GitHub: {e}")
        return False

st.markdown('<div class="section-header">Job Application</div>', unsafe_allow_html=True)

# Custom CSS: Plum background, pale blue text, Red Hat font, black inputs
st.markdown("""
    <style>
    @import url('https://fonts.com/css2?family=Red+Hat+Display&display=swap');

    html, body, [class*="css"] {
        font-family: 'Red Hat Display', sans-serif;
    }

    .section-header {
        background-color: #801259;
        color: #E1E2F2;
        padding: 0.75em;
        font-size: 1.3em;
        font-weight: bold;
        border-radius: 0.3em;
        margin-top: 1.5em;
    }

    input, textarea {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

full_name = st.text_input("Full Name", key="full_name")
address = st.text_input("Address", key="address")

col1, col2 = st.columns(2)
with col1:
    phone = st.text_input("Phone Number", key="phone")
with col2:
    email = st.text_input("Email", key="email")

# --- Section: Position and Availability ---
st.markdown('<div class="section-header">Position and Availability</div>', unsafe_allow_html=True)

position = st.text_input("Position You Are Applying For", key="position")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    pt = st.checkbox("Part-time", key="pt")
with col2:
    ft = st.checkbox("Full-time", key="ft")
with col3:
    weekdays = st.checkbox("Weekdays", key="weekdays")
with col4:
    weekends = st.checkbox("Weekends", key="weekends")
with col5:
    evenings = st.checkbox("Evenings", key="evenings")

availability = []
if pt: availability.append("Part-time")
if ft: availability.append("Full-time")
if weekdays: availability.append("Weekdays")
if weekends: availability.append("Weekends")
if evenings: availability.append("Evenings")

# --- Section: Work History ---
st.markdown('<div class="section-header">Work History</div>', unsafe_allow_html=True)

job_position = st.text_input("Job Position", key="job_position")
col1, col2 = st.columns(2)
with col1:
    job_from = st.date_input("From", key="job_from")
with col2:
    job_to = st.date_input("To", key="job_to")
employer = st.text_input("Employer Name", key="employer")
skills = st.text_area("Job Skills", key="skills")

# --- Section: Education ---
st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

school = st.text_input("School Name", key="school")
col1, col2 = st.columns(2)
with col1:
    edu_from = st.date_input("Education From", key="edu_from")
with col2:
    edu_to = st.date_input("Education To", key="edu_to")

col1, col2, col3 = st.columns(3)
with col1:
    city = st.text_input("City", key="city")
with col2:
    state = st.text_input("State", key="state")
with col3:
    zipcode = st.text_input("Zip Code", key="zip")

# --- Submit and Save ---
if st.button("Submit Application", key="submit"):
    submission = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Full Name": full_name,
        "Address": address,
        "Phone": phone,
        "Email": email,
        "Position": position,
        "Availability": ", ".join(availability),
        "Job_Position": job_position,
        "Job_From": job_from,
        "Job_To": job_to,
        "Employer": employer,
        "Skills": skills,
        "School": school,
        "Edu_From": edu_from,
        "Edu_To": edu_to,
        "City": city,
        "State": state,
        "Zipcode": zipcode
    }

    file_path = "submissions.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([submission])], ignore_index=True)
    else:
        df = pd.DataFrame([submission])

    df.to_csv(file_path, index=False)
    st.success("✅ Thank you! Your application has been submitted.")




