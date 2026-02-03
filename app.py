import streamlit as st

st.title("Job Application Form")

st.header("Personal Information")
full_name = st.text_input("Full Name")
address = st.text_input("Address")
phone = st.text_input("Phone Number")
email = st.text_input("Email")

st.header("Position & Availability")
position = st.text_input("Postion You're Applying For")

availability = []
if st.checkbox("Part-time"):
  availability.append("Part-time")
if st.checkbox("Full-time"):
  availability.append("Full-time")
if st.checkbox("Weekdays"):
  availability.append("Weekdays")
if st.checkbox("Weekends"):
  availability.append("Weekends")
if st.checkbox("Evenings"):
  availabilty.append("Evenings")
    
st.header("Work_Hisotry")

#Job 1
st.subheader("Job #1")
job1_from = st.date_input("From (Job 1)", key="job_from")
job1_to = st.date_input("To (Job 1)", key="job1_to")
job1_position = st.text_input("Position (Job 1)")
job1_company = st.text_input("Company (Job 1)")
job1_employer = st.text_input("Employer (Job 1)")
job1_skills = st.text_area("Job Skills (Job 1)")

#Job 2
st.subheader("Job #2")
job2_from = st.date_input("From(Job 2)", key="job2_from")
job2_to = st.date_input("To (Job 2)", key="job2_to")
job2_position = st.text_input("Position (Job 2)")
job2_employer = st.text_input("Employer (Job 2)")
job2_skills = st.text_area("job Skills (Job 2)")

st.header("Education")
edu_from = st.date_input("From (Education)", key="edu_from")
edu_to = st.date_input("To (Education)", key="edu_to")
school_name = st.text_input("School Name")
school_city = st.text_input("City")
school_state = st.text_input("State")
school_zip = st.text_input("Zip Code")

if st.button("Submit Application"):
  st.success("Thank you for submitting your application!")

  st.write("### Summary of Submission")
  st.write(f"**Name:** {full_name}")
  st.write(f"**Address:** {address}")
  st. write(f"**Phone:** {phone}")
  st.write(f"**Email:** {email}")
  st.write(f"**Position:** {position}")
  st.write(f"**Availability:** {', '.join(availability)}")

  st.write("#### Job 1:")
  st.write(f"From: {job1_from} To: {job1_to}")
  st.write(f"Position: {job1_position}")
  st.write(f"Employer: {job1_employer}")
  st.write(f"Skills: {job1_skills}")
  
  st.write("#### Job 2:")
  st.write(f"From: {job2_from} to {job2_to}")
  st.write(f"Position: {job2_position}")
  st.write(f"Employer: {job2_employer}")
  st.write(f"Skills: {job2_skills}")

  st.write("#### Education:")
  st.write(f"From: {edu_from} To: {edu_to}")
  st.write(f"School: {school_name}")
  st.write(f"Location: {school_city}, {school_state}, {school_zip}")

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Custom CSS for fonts and colors
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

# Header
st.markdown('<div class="section-header">Job Application</div>', unsafe_allow_html=True)

name = st.text_input("Full Name")
address = st.text_input("Address")

col1, col2 = st.columns(2)
with col1:
    phone = st.text_input("Phone Number")
with col2:
    email = st.text_input("Email")

# Position and Availability Section
st.markdown('<div class="section-header">Position and Availability</div>', unsafe_allow_html=True)

position = st.text_input("Position You Are Applying For")

# Horizontal checkboxes
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    pt = st.checkbox("Part-time")
with col2:
    ft = st.checkbox("Full-time")
with col3:
    weekdays = st.checkbox("Weekdays")
with col4:
    weekends = st.checkbox("Weekends")
with col5:
    evenings = st.checkbox("Evenings")

availability = []
if pt: availability.append("Part-time")
if ft: availability.append("Full-time")
if weekdays: availability.append("Weekdays")
if weekends: availability.append("Weekends")
if evenings: availability.append("Evenings")

# Work History Section
st.markdown('<div class="section-header">Work History</div>', unsafe_allow_html=True)

job_position = st.text_input("Job Position")
col1, col2 = st.columns(2)
with col1:
    job_from = st.date_input("From", key="job_from")
with col2:
    job_to = st.date_input("To", key="job_to")
employer = st.text_input("Employer Name")
skills = st.text_area("Job Skills")

# Education Section
st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

school = st.text_input("School Name")
col1, col2 = st.columns(2)
with col1:
    edu_from = st.date_input("Education From", key="edu_from")
with col2:
    edu_to = st.date_input("Education To", key="edu_to")

col1, col2, col3 = st.columns(3)
with col1:
    city = st.text_input("City")
with col2:
    state = st.text_input("State")
with col3:
    zipcode = st.text_input("Zip Code")

# Submission
if st.button("Submit Application"):
    submission = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Full Name": name,
        "Address": address,
        "Phone": phone,
        "Email": email,
        "Position": position,
        "Availability": ", ".join(availability),
        "Job_Position": job_position,
        "From": job_from,
        "To": job_to,
        "Employer": employer,
        "Skills": skills,
        "School": school,
        "Edu_From": edu_from,
        "Edu_To": edu_to,
        "City": city,
        "State": state,
        "Zipcode": zipcode
    }

    # Save to CSV
    file_path = "submissions.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([submission])], ignore_index=True)
    else:
        df = pd.DataFrame([submission])
    df.to_csv(file_path, index=False)

    st.success("Thank you! Your application has been submitted.")

import pandas as pd
from datetime import datetime
import os

if st.button("Submit Application"):
    st.success("Thank you for submitting your application!")

    submission = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Full Name": full_name,
        "Address": address,
        "Phone": phone,
        "Email": email,
        "Position": position,
        "Availability": ", ".join(availability),
        "Job1_From": job1_from,
        "Job1_To": job1_to,
        "Job1_Position": job1_position,
        "Job1_Employer": job1_employer,
        "Job1_Skills": job1_skills,
        "Job2_From": job2_from,
        "Job2_To": job2_to,
        "Job2_Position": job2_position,
        "Job2_Employer": job2_employer,
        "Job2_Skills": job2_skills,
        "Edu_From": edu_from,
        "Edu_To": edu_to,
        "School": school_name,
        "School_City": school_city,
        "School_State": school_state,
        "School_Zip": school_zip
    }

    file_path = "submissions.csv"

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([submission])], ignore_index=True)
    else:
        df = pd.DataFrame([submission])

    df.to_csv(file_path, index=False)

