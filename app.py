import streamlit as st
import joblib
import pandas as pd
import altair as alt

# ============================================================
# PAGE CONFIG - MUST BE FIRST
# ============================================================

st.set_page_config(
    page_title="SocialShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("models/fake_account_model.pkl")

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background: #f4f7ff;
}

/* Page width */
.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Remove excessive top space */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Brand */
.brand {
    font-size: 28px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 2px;
}

.brand-sub {
    color: #6b7280;
    font-size: 12px;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #2563eb, #4f46e5, #7c3aed);
    padding: 28px 32px;
    border-radius: 18px;
    color: white;
    margin-top: 15px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(79,70,229,0.20);
}

.hero h1 {
    color: white;
    font-size: 30px;
    margin-bottom: 6px;
}

.hero p {
    color: #e0e7ff;
    font-size: 14px;
}

/* Cards created with native containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 15px rgba(31,41,55,0.05);
}

/* Section headings */
.section-title {
    color: #111827;
    font-size: 20px;
    font-weight: 800;
    margin-top: 22px;
    margin-bottom: 10px;
}

/* Inputs */
div[data-baseweb="input"] {
    background: white !important;
    border: 1px solid #d1d5db !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    color: #111827 !important;
    background: white !important;
}

div[data-baseweb="select"] > div {
    background: white !important;
    border: 1px solid #d1d5db !important;
    border-radius: 8px !important;
}

div[data-baseweb="select"] span {
    color: #111827 !important;
}

/* Input labels */
.stNumberInput label,
.stSelectbox label {
    color: #374151 !important;
    font-weight: 600 !important;
}

/* Analyze button */
div.stButton > button {
    background: #2563EB !important;
    background-color: #2563EB !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    min-height: 45px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 14px rgba(37,99,235,0.25) !important;
}

div.stButton > button:hover {
    background: #1D4ED8 !important;
    background-color: #1D4ED8 !important;
    color: white !important;
}

/* Result text */
.result-good {
    color: #15803d;
    font-size: 24px;
    font-weight: 800;
}

.result-warning {
    color: #b91c1c;
    font-size: 24px;
    font-weight: 800;
}

/* Probability numbers */
.prob-good {
    color: #16a34a;
    font-size: 26px;
    font-weight: 800;
}

.prob-warning {
    color: #dc2626;
    font-size: 26px;
    font-weight: 800;
}

/* Footer */
.footer {
    text-align: center;
    color: #6b7280;
    font-size: 12px;
    padding: 30px 0 10px;
}

/* ------------------------------------------------------------------ */
/* Text visibility fixes: make normal text dark while preserving colors */
/* ------------------------------------------------------------------ */
/* Make general text dark on the light background */
body, p, label, span, div {
    color: #111827 !important;
}

/* Re-apply important exceptions so hero, buttons, result colors, and graphs stay intact */
.hero, .hero * {
    color: white !important;
}
.result-good, .result-good * {
    color: #15803d !important;
}
.result-warning, .result-warning * {
    color: #b91c1c !important;
}
.prob-good, .prob-good * {
    color: #16a34a !important;
}
.prob-warning, .prob-warning * {
    color: #dc2626 !important;
}
div.stButton > button {
    /* keep button text white */
    color: white !important;
}

/* Metrics: ensure values and labels are dark and readable */
div[data-testid="stMetric"] .stMetricValue, div[data-testid="stMetric"] .stMetricLabel, .stMetricValue, .stMetricLabel {
    color: #111827 !important;
}

/* Inputs: enforce darker labels */
.stNumberInput label,
.stSelectbox label {
    color: #374151 !important;
    font-weight: 600 !important;
}

/* Footer: medium/dark gray */
.footer {
    color: #6B7280 !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="brand">🛡️ SocialShield</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="brand-sub">AI-Powered Social Media Fraud Detection</div>',
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">
    <h1>Detect Suspicious Accounts with AI</h1>
    <p>
        Analyze social media account characteristics using a
        Random Forest machine learning model and generate a
        probability-based risk assessment.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# STATISTICS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="🎯 Model Accuracy",
        value="96.5%"
    )

with c2:
    st.metric(
        label="📊 Dataset Records",
        value="1,000"
    )

with c3:
    st.metric(
        label="🧠 Training Records",
        value="800"
    )

with c4:
    st.metric(
        label="🧪 Testing Records",
        value="200"
    )

# ============================================================
# MAIN SECTION
# ============================================================

left, right = st.columns([1, 1], gap="large")

# ============================================================
# ACCOUNT PROFILE
# ============================================================

with left:

    st.markdown(
        '<div class="section-title">👤 Account Profile</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:

            followers = st.number_input(
                "Followers",
                min_value=0,
                value=100,
                step=1
            )

            posts = st.number_input(
                "Posts",
                min_value=0,
                value=10,
                step=1
            )

            friend_requests = st.number_input(
                "Friend Requests",
                min_value=0,
                value=100,
                step=1
            )

        with col2:

            friends = st.number_input(
                "Friends",
                min_value=0,
                value=500,
                step=1
            )

            account_age_days = st.number_input(
                "Account Age (days)",
                min_value=0,
                value=100,
                step=1
            )

            profile_complete = st.selectbox(
                "Profile Complete?",
                ["Yes", "No"]
            )

        verified = st.selectbox(
            "Verified Account?",
            ["Yes", "No"]
        )

        profile_complete_value = (
            1 if profile_complete == "Yes" else 0
        )

        verified_value = (
            1 if verified == "Yes" else 0
        )

        st.write("")

        analyze_button = st.button(
            "🔍 Analyze Account",
            use_container_width=True
        )

# ============================================================
# RESULT
# ============================================================

with right:

    st.markdown(
        '<div class="section-title">📊 AI Detection Result</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        if analyze_button:

            # Create input data
            data = pd.DataFrame([{
                "followers": followers,
                "friends": friends,
                "posts": posts,
                "account_age_days": account_age_days,
                "friend_requests": friend_requests,
                "profile_complete": profile_complete_value,
                "verified": verified_value
            }])

            # Match exact training feature order
            data = data[model.feature_names_in_]

            # Prediction
            prediction = model.predict(data)[0]

            # Probability
            probability = model.predict_proba(data)[0]

            real_probability = probability[0] * 100
            fake_probability = probability[1] * 100

            # Risk
            if fake_probability < 30:
                risk = "Low Risk"
            elif fake_probability <= 70:
                risk = "Medium Risk"
            else:
                risk = "High Risk"

            # Result
            if prediction == 1:

                st.markdown(
                    '<div class="result-warning">'
                    '🚨 POTENTIALLY SUSPICIOUS'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.warning(
                    "The model detected characteristics associated "
                    "with potentially suspicious account behavior. "
                    "This is a model prediction, not proof of fraud."
                )

            else:

                st.markdown(
                    '<div class="result-good">'
                    '✓ LIKELY AUTHENTIC'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.success(
                    "The model did not detect strong characteristics "
                    "associated with suspicious account behavior."
                )

            st.write("")

            # Risk
            st.markdown(
                f"**Risk Level:** `{risk}`"
            )

            st.divider()

            # Probability values
            p1, p2 = st.columns(2)

            with p1:

                st.markdown(
                    "**🔴 Suspicious Probability**"
                )

                st.markdown(
                    f'<div class="prob-warning">'
                    f'{fake_probability:.2f}%'
                    f'</div>',
                    unsafe_allow_html=True
                )

            with p2:

                st.markdown(
                    "**🟢 Authentic Probability**"
                )

                st.markdown(
                    f'<div class="prob-good">'
                    f'{real_probability:.2f}%'
                    f'</div>',
                    unsafe_allow_html=True
                )

            st.write("")

            # ==================================================
            # LINE GRAPH
            # ==================================================

            st.markdown("### Probability Assessment")

            chart_data = pd.DataFrame({
                "Type": [
                    "Suspicious",
                    "Authentic"
                ],
                "Probability": [
                    fake_probability,
                    real_probability
                ]
            })

            base = alt.Chart(chart_data).encode(
                x=alt.X(
                    "Type:N",
                    sort=["Suspicious", "Authentic"],
                    title=None,
                    axis=alt.Axis(
                        labelFontSize=13,
                        labelAngle=0
                    )
                ),
                y=alt.Y(
                    "Probability:Q",
                    title="Probability (%)",
                    scale=alt.Scale(domain=[0, 100]),
                    axis=alt.Axis(
                        values=[0, 25, 50, 75, 100]
                    )
                )
            )

            line = base.mark_line(
                color="#64748B",
                strokeWidth=3
            )

            points = base.mark_point(
                filled=True,
                size=180
            ).encode(
                color=alt.Color(
                    "Type:N",
                    scale=alt.Scale(
                        domain=["Suspicious", "Authentic"],
                        range=["#DC2626", "#16A34A"]
                    ),
                    legend=None
                )
            )

            labels = base.mark_text(
                dy=-15,
                fontSize=13,
                fontWeight="bold"
            ).encode(
                text=alt.Text(
                    "Probability:Q",
                    format=".2f"
                ),
                color=alt.value("#111827")
            )

            chart = (
                line + points + labels
            ).properties(
                height=280
            ).configure_view(
                stroke=None,
                fill="white"
            ).configure_axis(
                gridColor="#E5E7EB",
                labelColor="#374151",
                titleColor="#374151"
            )

            st.altair_chart(
                chart,
                use_container_width=True
            )

            st.caption(
                "Comparison of the model's predicted probabilities "
                "for this account."
            )

        else:

            st.info(
                "🛡️ **Ready for Analysis**\n\n"
                "Enter account information on the left and click "
                "**Analyze Account** to generate an AI assessment."
            )

# ============================================================
# HOW SOCIALSHIELD WORKS
# ============================================================

st.markdown(
    '<div class="section-title">⚙️ How SocialShield Works</div>',
    unsafe_allow_html=True
)

w1, w2, w3 = st.columns(3, gap="medium")

with w1:

    with st.container(border=True):

        st.markdown("### 01")
        st.markdown("**Enter Account Details**")

        st.write(
            "Provide the account profile information "
            "required for analysis."
        )

with w2:

    with st.container(border=True):

        st.markdown("### 02")
        st.markdown("**AI Analyzes Behavior**")

        st.write(
            "A Random Forest model evaluates the "
            "selected account features."
        )

with w3:

    with st.container(border=True):

        st.markdown("### 03")
        st.markdown("**Receive Detection Result**")

        st.write(
            "Get a probability-based assessment "
            "of the account's risk level."
        )

# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown(
    '<div class="section-title">📈 Model Performance</div>',
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4, gap="medium")

with m1:

    with st.container(border=True):

        st.metric(
            "Accuracy",
            "96.5%"
        )

with m2:

    with st.container(border=True):

        st.metric(
            "Training Samples",
            "800"
        )

with m3:

    with st.container(border=True):

        st.metric(
            "Testing Samples",
            "200"
        )

with m4:

    with st.container(border=True):

        st.metric(
            "Algorithm",
            "Random Forest"
        )

# ============================================================
# FOOTER
# ============================================================

# ============================================================
# MODEL ANALYTICS (ADDED)
# ============================================================

st.markdown(
        '<div class="section-title">📊 Model Analytics</div>',
        unsafe_allow_html=True
)

am1, am2, am3, am4 = st.columns(4, gap="medium")

with am1:
        with st.container(border=True):
                st.metric("Accuracy", "96.5%")

with am2:
        with st.container(border=True):
                st.metric("Precision", "97%")

with am3:
        with st.container(border=True):
                st.metric("Recall", "95%")

with am4:
        with st.container(border=True):
                st.metric("F1 Score", "96%")

# Confusion matrix and explanation
with st.container(border=True):
        st.markdown("""
        <div style="display:flex;gap:20px;align-items:flex-start;">
            <div style="flex:0 0 360px;background:white;border:1px solid #E5E7EB;border-radius:12px;padding:16px;">
                <div style="font-weight:800;color:#111827;margin-bottom:8px">Confusion Matrix</div>
                <table style="width:100%;border-collapse:collapse;text-align:center;font-family:inherit">
                    <thead>
                        <tr>
                            <th style="text-align:left;padding:6px 8px;color:#374151"></th>
                            <th style="padding:6px 8px;background:#F9FAFB;color:#374151;border:1px solid #F1F5F9">Predicted Real</th>
                            <th style="padding:6px 8px;background:#F9FAFB;color:#374151;border:1px solid #F1F5F9">Predicted Fake</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="text-align:left;padding:8px;color:#374151;font-weight:700">Actual Real</td>
                            <td style="padding:8px;color:#111827;font-weight:800;border:1px solid #F1F5F9">129</td>
                            <td style="padding:8px;color:#111827;font-weight:800;border:1px solid #F1F5F9">0</td>
                        </tr>
                        <tr>
                            <td style="text-align:left;padding:8px;color:#374151;font-weight:700">Actual Fake</td>
                            <td style="padding:8px;color:#111827;font-weight:800;border:1px solid #F1F5F9">7</td>
                            <td style="padding:8px;color:#111827;font-weight:800;border:1px solid #F1F5F9">64</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div style="flex:1;min-width:200px;color:#374151">
                <div style="font-weight:700;color:#111827;margin-bottom:8px">About this matrix</div>
                <div style="color:#374151;font-size:14px;line-height:1.45">
                    The confusion matrix shows how the Random Forest model classified
                    real and potentially fake accounts on the test dataset.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    🛡️ SocialShield · AI-Based Social Media Fraud Detection
    <br>
    Built with Python · Streamlit · Machine Learning
</div>
""", unsafe_allow_html=True)