import streamlit as st
import requests

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

# 主標題
st.title("Business Plan Assistant")

# Executive Summary
st.header("Executive Summary")

# Business Overview
st.subheader("Business Overview")
st.session_state['business_overview'] = st.text_input("Brief Description of Business Idea", 
                                                      placeholder="Enter the business idea", 
                                                      value=st.session_state['business_overview'])

# Problem statement
st.session_state['problem_statement'] = st.text_input("Problem Statement / Pain of the Customer", 
                                                      placeholder="Enter the problem statement", 
                                                      value=st.session_state['problem_statement'])

# Mission and Vision Statements
st.subheader("Mission and Vision Statements")
st.session_state['mission_vision_statements'] = st.text_input("Goals and Future Aspirations of the Business", 
                                                              placeholder="Enter the goals and future aspirations", 
                                                              value=st.session_state['mission_vision_statements'])

# Management Team
st.subheader("Management Team")
st.session_state['number_of_team_members'] = st.number_input("Number of Team Members", min_value=1, step=1, 
                                                             value=st.session_state['number_of_team_members'])

for i in range(1, st.session_state['number_of_team_members'] + 1):
    if len(st.session_state['team_members']) < i:
        st.session_state['team_members'].append({
            "name": '',
            "role": '',
            "education": '',
            "expertise": ''
        })
    st.subheader(f"Team Member {i}")
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
st.header("Business Description")

st.session_state['business_structure'] = st.selectbox("Business Structure", ["B2B", "B2C", "C2C"], 
                                                      index=["B2B", "B2C", "C2C"].index(st.session_state['business_structure']))
st.session_state['unique_value_proposition'] = st.text_input("Unique Value Proposition (Optional)", 
                                                             placeholder="Enter what makes the business unique", 
                                                             value=st.session_state['unique_value_proposition'])

# Market Analysis
st.header("Market Analysis")

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
st.header("Product / Service Design")

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
            st.session_state['business_plan'] = response_data["received_data"]
            st.subheader("Business Plan")
            st.markdown(f"<div style='border-radius: 15px; border: 1px solid #e6e6e6; padding: 20px;'>{st.session_state['business_plan']}</div>", unsafe_allow_html=True)
        else:
            st.error("Failed to send data to backend")

if st.button("Start Over"):
    reset_outputs()
st.markdown("</div>", unsafe_allow_html=True)

# Credit centered at the bottom
st.markdown("<div style='text-align: center;'>© 2024 Gihyun Lee, Ghita Benboubker, Chen Bo Han. All rights reserved.</div>", unsafe_allow_html=True)
