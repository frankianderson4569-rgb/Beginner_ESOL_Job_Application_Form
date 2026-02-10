import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import base64
import json

# ---- STYLE ----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display&display=swap');

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

# ---- FORM FIELDS ----
st.markdown('<div class="section-header">Job Application</div>', unsafe_allow_html=True)

full_name = st.text_input("Full Name", key="full_name")
address = st.text_input("Address", key="address")

col1, col2 = st.columns(2)
with col1:
    phone = st.text_input("Phone Number", key="phone")
with col2:
    email = st.text_input("Email", key="email")

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

st.markdown('<div class="section-header">Work History</div>', unsafe_allow_html=True)

job_position = st.text_input("Job Position", key="job_position")
col1, col2 = st.columns(2)
with col1:
    job_from = st.date_input("From", key="job_from")
with col2:
    job_to = st.date_input("To", key="job_to")
employer = st.text_input("Employer Name", key="employer")
skills = st.text_area("Job Skills", key="skills")

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

# ---- SUBMISSION ----
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

    # Load or create CSV
    csv_filename = "submissions.csv"
    try:
        df_existing = pd.read_csv(csv_filename)
        df = pd.concat([df_existing, pd.DataFrame([submission])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([submission])
    df.to_csv(csv_filename, index=False)

    # ---- Upload to GitHub ----
    def upload_to_github(repo, path, token, content):
        url = f"https://api.github.com/repos/{repo}/contents/{path}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Check if file exists to get SHA
        get_response = requests.get(url, headers=headers)
        if get_response.status_code == 200:
            sha = get_response.json()["sha"]
        else:
            sha = None

        encoded_content = base64.b64encode(content.encode()).decode()

        payload = {
            "message": "Update job application submission",
            "content": encoded_content,
            "branch": "main"
        }
        if sha:
            payload["sha"] = sha

        response = requests.put(url, headers=headers, data=json.dumps(payload))
        return response.status_code

    # GitHub credentials
    GITHUB_TOKEN = st.secrets["github_token"]
    GITHUB_REPO = "frankianderson4569-rgb/Beginner_ESOL_Job_Application_Form"
    GITHUB_PATH = "submissions.csv"

    with open("submissions.csv", "r") as file:
        content = file.read()

    status = upload_to_github(GITHUB_REPO, GITHUB_PATH, GITHUB_TOKEN, content)

    if status in [200, 201]:
        st.success("✅ Application submitted and saved to GitHub!")
    else:
        st.error("❌ Submission failed to upload to GitHub.")
