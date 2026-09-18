
import streamlit as st
from pathlib import Path
import sys

# Allow Python to find our feature extractor
sys.path.append(str(Path(__file__).parent / "src"))

from feature_extractor import extract_rtl_features
from ppa_predictor import predict_ppa
from ml_model import predict_ml_ppa


# Page configuration
st.set_page_config(
    page_title="RTL-Insight",
    page_icon="⚡",
    layout="wide"
)

# Title
st.title("RTL-Insight")
st.subheader("Intelligent Pre-Synthesis PPA Analysis")

st.write(
    "Analyze Verilog RTL designs and extract structural features."
)


# Upload RTL Verilog file

st.header("Upload RTL Design")

uploaded_file = st.file_uploader(
    "Choose a Verilog RTL file",
    type=["v"]
)

if uploaded_file is not None:

    # Save uploaded file
    rtl_file = (
        Path(__file__).parent
        / "sample_alu.v"
    )

    rtl_file.write_bytes(
        uploaded_file.getvalue()
    )

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

else:

    # Use default sample design
    rtl_file = (
        Path(__file__).parent
        / "rtl"
        / "sample_alu.v"
    )
# Check if file exists
if rtl_file.exists():

    features = extract_rtl_features(rtl_file)

    st.success("RTL file loaded successfully!")

    st.header("RTL Feature Summary")

    # Display features
    col1, col2, col3 = st.columns(3)

    col1.metric("Modules", features["modules"])
    col2.metric("Inputs", features["inputs"])
    col3.metric("Outputs", features["outputs"])

    col4, col5, col6 = st.columns(3)

    col4.metric("Registers", features["registers"])
    col5.metric("Always Blocks", features["always_blocks"])
    col6.metric("Case Statements", features["case_statements"])
 
    st.header("RTL Operation Analysis")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Adders", features["adders"])
    col2.metric("Subtractors", features["subtractors"])
    col3.metric("AND Operations", features["and_operations"])
    col4.metric("OR Operations", features["or_operations"])

    st.header("Complete Feature Details")

    st.json(features)
    
    st.header("PPA Prediction")

    ppa_results = predict_ppa(features)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Estimated Area",
        ppa_results["estimated_area"]
    )

    col2.metric(
        "Estimated Power",
        ppa_results["estimated_power"]
    )

    col3.metric(
        "Estimated Performance",
        ppa_results["estimated_performance"]
    )



        
    st.header("PPA Comparison Chart")

    import pandas as pd

    ppa_chart_data = pd.DataFrame({
        "Metric": ["Area", "Power", "Performance"],
        "Value": [
            ppa_results["estimated_area"],
            ppa_results["estimated_power"],
            ppa_results["estimated_performance"]
        ]
    })

    st.bar_chart(
        ppa_chart_data.set_index("Metric")
    )
    
    # ML-Based PPA Prediction

    st.header("ML-Based PPA Prediction")

    ml_results = predict_ml_ppa(features)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "ML Estimated Area",
        ml_results["ml_area"]
    )

    col2.metric(
        "ML Estimated Power",
        ml_results["ml_power"]
    )

    col3.metric(
        "ML Estimated Performance",
        ml_results["ml_performance"]
    )


    
    st.header("Baseline vs ML Comparison")

    comparison_data = pd.DataFrame({
        "Metric": ["Area", "Power", "Performance"],
        "Baseline": [
            ppa_results["estimated_area"],
            ppa_results["estimated_power"],
            ppa_results["estimated_performance"]
        ],
        "ML Prediction": [
            ml_results["ml_area"],
            ml_results["ml_power"],
            ml_results["ml_performance"] 
        ]
    })

    st.dataframe(
        comparison_data,
        use_container_width=True
    )

    st.bar_chart(
        comparison_data.set_index("Metric")
    )
   

else:
    st.error("RTL file not found!")