import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import joblib
import json
import base64

# Set page width
st.set_page_config(layout="wide")

# # Custom CSS styles
# st.markdown("""
#     <style>
#         .stApp {
#             background-color: #B4B4B8;
#         }
#         .stApp * {
#             color: white;
#         }
#         .sidebar .sidebar-content {
#             background-color: #378CE7;
#             color: #ffffff;
#         }
#         .sidebar .sidebar-content .block-container {
#             margin-top: 20px;
#         }
#         .stButton>button {
#             background-color: #2ecc71;
#             color: #ffffff;
#             border-radius: 5px;
#             padding: 10px 20px;
#             font-size: 16px;
#         }
#         .stButton>button:hover {
#             background-color: #27ae60;
#         }
#         .stTextInput>div>div>input {
#             border-radius: 5px;
#             padding: 10px;
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)



# Setting custom css
css = f"""
<style>

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

</style>
"""
st.markdown(css, unsafe_allow_html=True)


#impliment background formating
def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "jpg"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-repeat: no-repeat;
             background-position: right 50% bottom 50% ;
             background-size: cover;
             background-attachment: scroll;
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )

set_bg_hack("image/background_6.jpg")



# # Custom CSS styles
# st.markdown("""
#     <style>
#         .stApp {
#             background-color: #B4B4B8;
#         }
#         .sidebar .sidebar-content {
#             background-color: #378CE7;
#             color: #ffffff;
#         }
#         .sidebar .sidebar-content .block-container {
#             margin-top: 20px;
#         }
#         .stButton>button {
#             background-color: #2ecc71;
#             color: #ffffff;
#             border-radius: 5px;
#             padding: 10px 20px;
#             font-size: 16px;
#         }
#         .stButton>button:hover {
#             background-color: #27ae60;
#         }
#         .stTextInput>div>div>input {
#             border-radius: 5px;
#             padding: 10px;
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)

## Side Tab:
l=["Introduction","Predict your Credit Score"]
st.sidebar.subheader("Here's what you can do:")
option=st.sidebar.selectbox("Choose what you want to do:",l)

def page_1():
    ## Intro Tab::


    ## Headers:
    # st.set_page_config(page_title="Introduction")
    st.title("Welcome to Loan Eligibility Analyzer 🏦💵💵")
    st.header("Introduction 📝")
    st.write("""
        #### Loans constitute the fundamental business of banks, with the primary source of profit being the interest accrued on loans. Before granting a loan, financial institutions engage in a thorough process of verification and validation. Despite this, there remains uncertainty regarding whether the applicant possesses the capability to repay the loan without encountering difficulties. In this I construct a predictive model aimed at determining whether an applicant is likely to repay the loan to the lending company.
        """)
    st.markdown("---") 
    
    
    st.header("Problem Statement 🤔")
    st.write("""#### `Dream Housing Finance` company specializes in providing all types of loans across urban, semi-urban, and rural areas. Upon receiving a loan application, the company undertakes a validation process to determine the customer's eligibility. This validation process is based on various customer details provided during the online application, including age, house ownership, working experience, intent of loan, income, loan amount, credit history, among others. To streamline and automate this loan eligibility process in real-time, the company aims to identify specific customer segments that qualify for loan amounts. By targeting these eligible customer segments, the company can optimize its loan offerings and better serve its clientele.
                """)
    st.markdown("---") 

    st.header("A quick overview of dataset 🗃️")
    df = pd.read_csv("credit_risk_dataset_1.csv")
    st.dataframe(df.head())

    st.markdown("---")

    st.header("Top Insights 🧐")
    st.write("""
           - **Age Distribution**: Majority of borrowers are aged 20-35, indicating youthful loan applicants.
           - **Housing Status**: Half of our dataset resides in rented accommodations, while 40% have mortgaged homes.
           - **Loan Preference**: Educational loans are most popular, closely followed by medical loans. Personal and venture loans show similar demand.
           - **Default Rates**: While most borrowers have clean records, a small segment defaults 3-5 times.
           - **Loan Grades**: Grades A and B dominate, reflecting lower risk. Grades C-G signify higher risk, with fewer instances.
           - **Loan Amounts**: Loans of $5000-$10000 are most common, followed by $300-$5000 loans. A significant group borrows over $15000.

             """)
    
    st.markdown("---") 

    st.header("Technologies Used 🤖")
    st.write("""
            - SQLite: Database management system for storing and managing relational data.
            - Pandas: Python library for data manipulation and analysis.
            - Numpy: Python library for scientific computing.
            - Streamlit: Python library for building web applications.
            - Joblib: Python library for saving and loading machine learning models.
            - Scikit-learn: Python library for machine learning.
            - Plotly: Python library for interactive data visualization.
            - Machine learning algorithms: XG Boost, Random Forest, Logistic Regression, and Support Vector Machine.
            - SMOTE: Python library for oversampling data.
            """)
    st.markdown("---") 

    st.header("About the developer 👨🏻‍💻")
    st.markdown("""
                This app is developed by Akshat Sharma

        [![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)](https://github.com/Akshat8303)
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/akshat-sharma-278786273/)
               
             """)
    


def page_2():
    data = {}
    
    # Divide the page into three columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Details Tab:
    with col2:
        st.header("Give me your details and I will deliver magic!")

    # Full Name:
    with col2:
        first = st.text_input("Enter your First Name:")
        last = st.text_input("Enter your Last Name:")
        data["First Name"] = first
        data["Last Name"] = last

    name = first + " " + last
    data["Full Name"] = name

    # Age:
    with col2:
        age = st.slider("Enter your Age:", 20, 85)
        data["Age"] = age

    # Annual Income:
    with col2:
        ai = st.number_input("Enter your Annual Income:", 1, 100000)
        data["Annual Income"] = ai

    # Home Ownership:
    with col2:
        ho = st.selectbox("What is the type of House Ownership:", ["RENT", "OWN", "MORTGAGE", "OTHER"])
        data["Home Ownership"] = ho

    # Employment Length:
    with col2:
        el = st.number_input("Enter your Work Experience in years:", 2, 50)
        data["Employment Length"] = el

    # Loan Intent:
    with col2:
        li = st.selectbox("Why do you want a loan?", ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT'])
        data["Loan Intent"] = li

    # Loan Grade:
    with col2:
        lg = st.selectbox("Grade of Loan expected?", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        data["Loan Grade"] = lg

    # Loan Amount:
    with col2:
        la = st.number_input("Enter your Loan amount:", 100, 10000000000)
        data["Loan Amount"] = la

    # Loan Amount:
    with col2:
        lit = st.number_input("Enter Interest on Loan:", 1, 100)
        data["Loan Interest"] = lit

    # loan_percent_income:
    with col2:
        lpi = st.number_input("Enter your % Income to be used for repaying:", 0, 100)
        data["Loan Percent Income"] = lpi

    # cb_person_default_on_file:
    with col2:
        def_his = st.selectbox("Have you ever defaulted?", ["Y", "N"])
        data["Previous Defaults"] = def_his

        if def_his == "Y":
            # cb_person_cred_hist_length:
            n_def = st.slider("Total Number of Defaults:", 0, 10)
            data["Number of Defaults"] = n_def
        else:
            data["Number of Defaults"] = 0
            n_def = 0

    # Make a submit button:
    with col2:
        # Display the input data as a json:
        if st.button("Display Data", key=8):
            data_display = json.dumps(data)
            temp = pd.DataFrame(data, index=[0])  # making a record
            st.write("The data in JSON Format:")
            st.write(data_display)
            st.write("\nThe data in Tabular Format:")
            st.write(temp)

        # Display the prediction:
        if st.button("Check Eligibility", key=9):
            # Order of passing the data into the pipeline:
            cols = ['person_age', 'person_income', 'person_emp_length', 'loan_amnt', "loan_int_rate",
                    'loan_percent_income', 'cb_person_cred_hist_length',
                    'person_home_ownership', 'loan_intent', 'loan_grade',
                    'cb_person_default_on_file']  # List of columns of the original dataframe

            input_data = [[data["Age"], data["Annual Income"], data["Employment Length"], data["Loan Amount"],
                        data["Loan Interest"],
                        round(data["Loan Percent Income"] / 100, 2), data["Number of Defaults"],
                        data["Home Ownership"], data["Loan Intent"], data["Loan Grade"], data["Previous Defaults"]]]

            pipe = joblib.load('best_pipeline.pkl')  # Loading the pipeline

            input_data = pd.DataFrame(input_data, columns=cols)  # Converting input into a dataframe with respective columns

            res = pipe.predict(input_data)[0]  # Predicting the class
            prob = pipe.predict_proba(input_data)[0][res]  # Predicting the probability of the class
            out = {1: "The Customer is capable of DEFAULTING. Hence it is RISKY to provide loan!",
                0: "The Customer is capable of NOT DEFAULTING. Hence it is POSSIBLE to provide loan!"}
            st.write(f"The Final Predict obtained from the given model is that : {out[res]}, with the probability of {round(prob * 100, 2)}%")

            if res == 1:
                image_n = Image.open('image/Not_approve.png')
                st.image(image_n)
            else:
                image_a = Image.open('image/approved.png')
                st.image(image_a, width=400)




if option==l[0]:
    page_1()

if option==l[1]:
    page_2()