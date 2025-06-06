import streamlit as st
import datetime

# --- Sidebar: Your Info ---
st.sidebar.title("Your Profile")
name = st.sidebar.text_input("Name", "Saisriram Kancharla")
email = st.sidebar.text_input("Email", "ksaisriram2003@gmail.com")
phone = st.sidebar.text_input("Phone", "8125378063")
batch = st.sidebar.text_input("Batch Year", "2025")
skills = st.sidebar.text_area("Skills", "Python, Java, C, ML")

resume = st.sidebar.file_uploader("Upload Resume", type=["pdf"])

# --- Main ---
st.title("🤖 AI Agent for Fresher Jobs")
st.write("Helping you apply to jobs automatically!")

# Job list
jobs = [
    {"title": "Python Developer", "company": "Infosys"},
    {"title": "ML Intern", "company": "TCS"},
    {"title": "Java Trainee", "company": "Wipro"},
]

# Job selector
st.subheader("📌 Select Jobs")
selected = st.multiselect("Choose jobs:", [f"{j['title']} at {j['company']}" for j in jobs])

# Cover letter generator
st.subheader("✉️ Generate Cover Letter")
job_role = st.text_input("Job Role", "Python Developer")
company = st.text_input("Company Name", "Infosys")

if st.button("Generate Cover Letter"):
    st.success("Here's your AI Cover Letter:")
    st.text_area("Cover Letter", f"Dear {company},\n\nI am Saisriram, a 2025 CSE graduate skilled in {skills}. I am excited to apply for {job_role}. Please find my resume attached.\n\nThank you.\n\n- {name}", height=300)

# Track
st.subheader("📋 Application Tracker")
if "applied" not in st.session_state:
    st.session_state.applied = []

if st.button("Mark as Applied"):
    today = str(datetime.date.today())
    for job in selected:
        st.session_state.applied.append(f"{job} | Applied on {today}")

for j in st.session_state.applied:
    st.write("✅", j)
