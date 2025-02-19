import streamlit as st
from src.data_import import data_import_page
from src.data_visualization import data_visualization_page
from src.data_preparation import data_preparation_page
from src.ml_modeling import ml_modeling_page
from src.evaluation import evaluation_page
from src.guide import guide_page



def home_page():
    """
    Enhanced Home Page for the ML Exploration App with Sidebar and Modern Icons
    """
    # Custom CSS
    st.markdown("""
        <style>
            /* General Page Styling */
            body {
                background-color: #DCE4C9;
                font-family: 'Arial', sans-serif;
            }

            /* Header Section */
            .header {
                text-align: center;
                background-color: #272727;
                color: #FFFFFF;
                padding: 30px;
                border-radius: 10px;
            }
            .header h1 {
                font-size: 3rem;
                margin: 0;
                color: #E07B39;
            }
            .header p {
                font-size: 1.3rem;
                margin: 10px 0 0 0;
                color: #B6A28E;
            }

            /* Features Section */
            .features {
                display: flex;
                justify-content: center;
                gap: 30px;
                margin: 40px 0;
            }
            .feature-card {
                text-align: center;
                background-color: #F5F5DC;
                border-radius: 10px;
                padding: 20px;
                width: 22%;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }
            .feature-card:hover {
                transform: translateY(-5px);
                background-color: #E07B39;
                color: #FFFFFF;
            }
            .feature-icon {
                display: inline-block;
                width: 60px;
                height: 60px;
                margin-bottom: 15px;
                background-size: contain;
                background-repeat: no-repeat;
                margin: 0 auto;
            }
            .feature-title {
                font-size: 1.2rem;
                font-weight: bold;
                color: #272727;
            }
            .feature-description {
                font-size: 1rem;
                color: #555555;
            }

            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background-color: #DCE4C9 !important;
                padding: 15px;
            }
            .sidebar-button {
                width: 100%;
                text-align: left;
                padding: 8px 10px;
                margin: 5px 0;
                background-color: transparent;
                border: none;
                cursor: pointer;
                color: #272727;
                font-size: 1rem;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            .sidebar-button:hover {
                background-color: #FFFFFF;
                color: #FFFFFF;
            }
                .header {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #272727;
            color: #FFFFFF;
            padding: 30px;
            border-radius: 10px;
        }
        .header h1 {
            font-size: 3rem;
            margin: 0 15px 0 0; /* Add space between logo and title */
            color: #E07B39;
        }
        .header p {
            font-size: 1.3rem;
            margin: 10px 0 0 0;
            color: #B6A28E;
        }
        .header img {
            height: 80px; /* Adjust the size of the logo */
            margin-right: 15px; /* Add space between logo and text */
        }
        </style>
    """, unsafe_allow_html=True)

    # # Header Section
    # st.markdown("""
    #     <div class="header">
    #         <h1>ML Academy</h1>
    #         <p>Your intuitive guide to a complete machine learning workflow.</p>
    #     </div>
    # """, unsafe_allow_html=True)
    st.markdown(f"""
   
    <div class="header">
        <div>
            <h1>ML Academy</h1>
            <p>Your intuitive guide to a complete machine learning workflow.</p>
        </div>
    </div>
""", unsafe_allow_html=True)


    # Features Section
    st.markdown("""
        <div class="features">
            <div class="feature-card">
                <div class="feature-icon" style="background-image: url('https://img.icons8.com/ios/50/000000/upload-to-cloud.png');"></div>
                <div class="feature-title">Data Import</div>
                <div class="feature-description">Upload datasets with ease.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon" style="background-image: url('https://img.icons8.com/ios/50/000000/combo-chart.png');"></div>
                <div class="feature-title">Visualization</div>
                <div class="feature-description">Analyze your data with clear visualizations.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon" style="background-image: url('https://img.icons8.com/ios/50/000000/broom.png');"></div>
                <div class="feature-title">Data Preparation</div>
                <div class="feature-description">Clean and structure your data.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon" style="background-image: url('https://img.icons8.com/ios/50/000000/artificial-intelligence.png');"></div>
                <div class="feature-title">Modeling</div>
                <div class="feature-description">Train and test ML models.</div>
            </div>
                <div class="feature-card">
                <div class="feature-icon" style="background-image: url('https://img.icons8.com/ios/50/000000/rating.png');"></div>
                <div class="feature-title">Model Evaluation</div>
                <div class="feature-description">Assess model performance with metrics.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def app():
    """
    Main Application Entry Point
    """
    st.set_page_config(
        page_title="ML Academy App",
        page_icon="uploads/logo.ico",  # Path to your .ico file
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    


    # Initialize session state for navigation if not exists
    if 'current_page' not in st.session_state:
       st.session_state.current_page = "Home"

    # Sidebar navigation using buttons
    with st.sidebar:
        if st.button(" Home", key="home", use_container_width=True):
            st.session_state.current_page = "Home"
        if st.button(" Data Handling", key="data_import", use_container_width=True):
            st.session_state.current_page = "Data Import"
        if st.button(" Visualization", key="visualization", use_container_width=True):
            st.session_state.current_page = "Data Visualization"
        if st.button(" Data Preparation", key="preparation", use_container_width=True):
            st.session_state.current_page = "Data Preparation"
        if st.button(" Modeling", key="modeling", use_container_width=True):
            st.session_state.current_page = "ML Modeling"
        if st.button(" Evaluation", key="evaluation", use_container_width=True):
            st.session_state.current_page = "Evaluation"
        if st.button(" Guide", key="guide", use_container_width=True):  # New button for guide page
            st.session_state.current_page = "Guide"
        

    # Page Routing based on session state
    if st.session_state.current_page == "Home":
        home_page()
    elif st.session_state.current_page == "Data Import":
        data_import_page()
    elif st.session_state.current_page == "Data Visualization":
        data_visualization_page()
    elif st.session_state.current_page == "Data Preparation":
        data_preparation_page()
    elif st.session_state.current_page == "ML Modeling":
        ml_modeling_page()
    elif st.session_state.current_page == "Evaluation":
        evaluation_page()
    elif st.session_state.current_page == "Guide":
        guide_page()  # Load the guide page
    
    
if __name__ == "__main__":
    app()