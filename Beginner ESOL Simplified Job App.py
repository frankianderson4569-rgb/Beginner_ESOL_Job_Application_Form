pip install streamlit
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
