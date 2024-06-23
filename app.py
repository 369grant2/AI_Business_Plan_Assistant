import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="AI Business Plan Assistant",
    page_icon="📈",
    initial_sidebar_state="expanded",
)

# CSS for the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(
        rgba(0, 0, 0, 0.6), /* This is the grey overlay; the last number is the opacity level */
        rgba(0, 0, 0, 0.5)
    ), url("https://images.unsplash.com/photo-1600712365047-26f7a4f04d44?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: 100vw 100vh; 
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

# Custom CSS for the rest
st.markdown("""
    <style>
        .header {
            text-align: center;
            color: white;
        }
        .subheader {
            color: white !important;
        }
        .stButton > button {
            background-color: white;
            color: black !important;
        }
        input, textarea {
            color: #808080 !important; /* Set the text color to black */
        }

        input::placeholder, textarea::placeholder {
            color: #808080 !important; /* Ensure all placeholders are black */
            opacity: 1 !important; /* Make sure placeholders are fully visible */
        }
        div[data-baseweb="select"] .st-bc {
            color: #808080 !important; /* Override to set text color to black */
        }
        div.stTextInput > label, 
        div.stTextArea > label,  
        div.stNumberInput > label,
        div.stExpander > label
        div.stRadio > label {
            color: white !important; /* Change color of the input labels */
        }
       
    </style>
""", unsafe_allow_html=True)

# Add logo
col1, col2, col3 = st.columns([2,2,1])
with col2:
    st.image("BP.png", width=150) 


# Initialize session state to store inputs and the generated business plan
if 'business_overview' not in st.session_state:
    st.session_state['business_overview'] = ''
if 'problem_statement' not in st.session_state:
    st.session_state['problem_statement'] = ''
if 'mission_vision_statements' not in st.session_state:
    st.session_state['mission_vision_statements'] = ''
if 'number_of_team_members' not in st.session_state:
    st.session_state['number_of_team_members'] = 1
if 'team_members' not in st.session_state:
    st.session_state['team_members'] = []
if 'business_structure' not in st.session_state:
    st.session_state['business_structure'] = 'B2B'
if 'unique_value_proposition' not in st.session_state:
    st.session_state['unique_value_proposition'] = ''
if 'industry_description' not in st.session_state:
    st.session_state['industry_description'] = ''
if 'target_market' not in st.session_state:
    st.session_state['target_market'] = ''
if 'geographical_location' not in st.session_state:
    st.session_state['geographical_location'] = ''
if 'product_service_description' not in st.session_state:
    st.session_state['product_service_description'] = ''
if 'key_features' not in st.session_state:
    st.session_state['key_features'] = ''
if 'key_benefits' not in st.session_state:
    st.session_state['key_benefits'] = ''
if 'business_plan' not in st.session_state:
    st.session_state['business_plan'] = ''
if 'revise_request' not in st.session_state:
    st.session_state['revise_request'] = ''

# Function to reset all input fields
def reset_outputs():
    # st.session_state['business_overview'] = ''
    # st.session_state['problem_statement'] = ''
    # st.session_state['mission_vision_statements'] = ''
    # st.session_state['number_of_team_members'] = 1
    # st.session_state['team_members'] = []
    # st.session_state['business_structure'] = 'B2B'
    # st.session_state['unique_value_proposition'] = ''
    # st.session_state['industry_description'] = ''
    # st.session_state['target_market'] = ''
    # st.session_state['geographical_location'] = ''
    # st.session_state['product_service_description'] = ''
    # st.session_state['key_features'] = ''
    # st.session_state['key_benefits'] = ''
    st.session_state['business_plan'] = ''
    st.session_state['revise_request'] = ''

# Main title with custom styling
st.markdown("<h1 class='header'>Business Plan Assistant</h1>", unsafe_allow_html=True)

# Executive Summary
st.markdown("<h2 class='subheader'>Executive Summary</h2>", unsafe_allow_html=True)

# Business Overview
st.markdown("<h3 class='subheader'>Business Overview</h3>", unsafe_allow_html=True)
st.session_state['business_overview'] = st.text_input("Brief Description of Business Idea", 
                                                      placeholder="Enter the business idea", 
                                                      value=st.session_state['business_overview'])

# Problem statement
st.session_state['problem_statement'] = st.text_input("Problem Statement / Pain of the Customer", 
                                                      placeholder="Enter the problem statement", 
                                                      value=st.session_state['problem_statement'])

# Mission and Vision Statements
st.markdown("<h3 class='subheader'>Mission and Vision Statements</h3>", unsafe_allow_html=True)
st.session_state['mission_vision_statements'] = st.text_input("Goals and Future Aspirations of the Business", 
                                                              placeholder="Enter the goals and future aspirations", 
                                                              value=st.session_state['mission_vision_statements'])

# Management Team
st.markdown("<h3 class='subheader'>Management Team</h3>", unsafe_allow_html=True)
st.session_state['number_of_team_members'] = st.number_input("Number of Team Members", min_value=1, step=1, 
                                                             value=st.session_state['number_of_team_members'])

# Sliding team members
for i in range(1, st.session_state['number_of_team_members'] + 1):
    if len(st.session_state['team_members']) < i:
        st.session_state['team_members'].append({
            "name": '',
            "role": '',
            "education": '',
            "expertise": ''
        })
    with st.expander(f"Team Member {i}"):
        st.session_state['team_members'][i-1]['name'] = st.text_input(f"Name of Member {i}", 
                                                                       placeholder="Enter name", 
                                                                       value=st.session_state['team_members'][i-1]['name'])
        st.session_state['team_members'][i-1]['role'] = st.text_input(f"Role of Member {i}", 
                                                                       placeholder="Enter role", 
                                                                       value=st.session_state['team_members'][i-1]['role'])
        st.session_state['team_members'][i-1]['education'] = st.text_input(f"Education / Qualification of Member {i}", 
                                                                            placeholder="Enter education or qualification", 
                                                                            value=st.session_state['team_members'][i-1]['education'])
        st.session_state['team_members'][i-1]['expertise'] = st.text_input(f"Expertise / Domain Knowledge of Member {i}", 
                                                                            placeholder="Enter expertise or domain knowledge", 
                                                                            value=st.session_state['team_members'][i-1]['expertise'])

# Business Description
st.markdown("<h2 class='subheader'>Business Description</h2>", unsafe_allow_html=True)

st.session_state['business_structure'] = st.selectbox("Business Structure", ["B2B", "B2C", "C2C"], 
                                                      index=["B2B", "B2C", "C2C"].index(st.session_state['business_structure']))
st.session_state['unique_value_proposition'] = st.text_input("Unique Value Proposition (Optional)", 
                                                             placeholder="Enter what makes the business unique", 
                                                             value=st.session_state['unique_value_proposition'])

# Market Analysis
st.markdown("<h2 class='subheader'>Market Analysis</h2>", unsafe_allow_html=True)

st.session_state['industry_description'] = st.text_input("Industry Description", 
                                                         placeholder="Overview of the industry", 
                                                         value=st.session_state['industry_description'])
st.session_state['target_market'] = st.text_input("Target Market Demographics (Optional)", 
                                                  placeholder="Demographics of target market (e.g., age, gender)", 
                                                  value=st.session_state['target_market'])
st.session_state['geographical_location'] = st.text_input("Geographical Location of Target Market (Optional)", 
                                                          placeholder="Geographical location of target market", 
                                                          value=st.session_state['geographical_location'])

# Product / Service Design
st.markdown("<h2 class='subheader'>Product / Service Design</h2>", unsafe_allow_html=True)

st.session_state['product_service_description'] = st.text_input("Product / Service Description", 
                                                                placeholder="Description of product or service", 
                                                                value=st.session_state['product_service_description'])
st.session_state['key_features'] = st.text_input("Key Features (Optional)", 
                                                 placeholder="Features and unique selling points", 
                                                 value=st.session_state['key_features'])
st.session_state['key_benefits'] = st.text_input("Key Benefits (Optional)", 
                                                 placeholder="Customer benefits", 
                                                 value=st.session_state['key_benefits'])

def check_non_optional_fields(activate = True):
    flag = True
    required_fields = [
        'business_overview',
        'problem_statement',
        'mission_vision_statements',
        'industry_description',
        'product_service_description'
    ]
    for field in required_fields:
        if not st.session_state[field]:
            st.warning(f"{field.replace('_', ' ').title()} is necessary.")
            flag = False
    for i, member in enumerate(st.session_state['team_members'], start=1):
        if not member['name'] or not member['role'] or not member['education'] or not member['expertise']:
            st.warning(f"Member {i}'s all entities are necessary")
            flag = False
    if activate:
        return flag
    else:
        return True

# Generate Business Plan and Start Over Buttons
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Generate Business Plan"):
    if check_non_optional_fields(activate = False):
        # Sending data to backend API
        backend_url = "http://localhost:5000/receive-data"  # Flask API endpoint
        data_to_send = {
            "business_overview": st.session_state['business_overview'],
            "mission_vision_statements": st.session_state['mission_vision_statements'],
            "number_of_team_members": st.session_state['number_of_team_members'],
            "team_members": st.session_state['team_members'],
            "business_structure": st.session_state['business_structure'],
            "unique_value_proposition": st.session_state['unique_value_proposition'],
            "industry_description": st.session_state['industry_description'],
            "target_market": st.session_state['target_market'],
            "geographical_location": st.session_state['geographical_location'],
            "product_service_description": st.session_state['product_service_description'],
            "key_features": st.session_state['key_features'],
            "key_benefits": st.session_state['key_benefits']
        }
        response = requests.post(backend_url, json=data_to_send)
        if response.status_code == 200:
            response_data = response.json()
            st.session_state['business_plan'] = response_data["business_plan"]
            st.session_state['evaluation'] = response_data["evaluation"]
            st.subheader("Business Plan")
            st.markdown(f"<div style='border-radius: 15px; border: 1px solid #e6e6e6; padding: 20px;'>{st.session_state['business_plan']}</div>", unsafe_allow_html=True)
            st.subheader("Plan Evaluation")
            st.markdown(f"<div style='border-radius: 15px; border: 1px solid #e6e6e6; padding: 20px;'>{st.session_state['evaluation']}</div>", unsafe_allow_html=True)
        else:
            st.error("Failed to send data to backend")

def check_BP_already(activate = True):
    flag = True
    required_fields = [
        'business_plan'
    ]
    for field in required_fields:
        if not st.session_state[field]:
            st.warning(f"{field.replace('_', ' ').title()} is necessary.")
            flag = False
    if activate:
        return flag
    else:
        return True

st.session_state['revise_request'] = st.text_input("Please enter your revision request below:",
                                                    placeholder="Enter revision request")

if st.button("Revise Business Plan"):
    if check_BP_already(activate = False):
        backend_url = "http://localhost:5000/receive-data"  # Flask API endpoint
        data_to_send = {
            "business_plan": st.session_state['business_plan'],
            "revise_request": st.session_state['revise_request']
        }
        response = requests.post(backend_url, json=data_to_send)
        if response.status_code == 200:
            response_data = response.json()
            st.session_state['business_plan'] = response_data["business_plan"]
            st.session_state['evaluation'] = response_data["evaluation"]
            st.subheader("Business Plan")
            st.markdown(f"<div style='border-radius: 15px; border: 1px solid #e6e6e6; padding: 20px;'>{st.session_state['business_plan']}</div>", unsafe_allow_html=True)
            st.subheader("Plan Evaluation")
            st.markdown(f"<div style='border-radius: 15px; border: 1px solid #e6e6e6; padding: 20px;'>{st.session_state['evaluation']}</div>", unsafe_allow_html=True)
        else:
            st.error("Failed to send data to backend")

if st.button("Start Over"):
    reset_outputs()
st.markdown("</div>", unsafe_allow_html=True)

# Credit centered at the bottom
st.markdown("<div style='text-align: center;'>© 2024 Chen Bo Han, Gihyun Lee, Ghita Benboubker. All rights reserved.</div>", unsafe_allow_html=True)