import streamlit as st
from datetime import date

# ------------------------------------------------------------
# HEALTH INSURANCE WEBSITE DEMO
# Built with Python + Streamlit for an academic assignment.
# All prices/benefits below are illustrative, not real offers.
# ------------------------------------------------------------

st.set_page_config(
    page_title="CareShield | Health Insurance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #f5f8fc; color: #172b4d; }
.block-container { padding-top: 1rem; padding-bottom: 3rem; max-width: 1200px; }
.hero {
  background: linear-gradient(115deg, rgba(5,42,82,.96), rgba(10,91,137,.83)),
  url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1800&q=85');
  background-size: cover; background-position: center; border-radius: 24px;
  padding: 3.2rem 3rem; color: white; min-height: 360px;
}
.hero h1 { color: white; font-family: Manrope; font-size: clamp(2.2rem, 4vw, 3.5rem); line-height: 1.1; }
.hero p { color: #e6f2ff; font-size: 1.1rem; max-width: 620px; }
.eyebrow { color:#9ee7d0; font-weight:800; letter-spacing:2px; text-transform:uppercase; font-size:.78rem; }
.section-title { font-family: Manrope; color:#0a3157; font-size:1.9rem; font-weight:800; margin: 1.5rem 0 .3rem; }
.muted { color:#61748b; }
.plan-card {
 background:white; border:1px solid #e2eaf2; border-radius:18px; padding:22px;
 box-shadow:0 8px 24px rgba(20,55,90,.06); min-height:260px;
}
.plan-card h3 { color:#0a3157; margin-top:0; }
.price { color:#ed6a24; font-size:1.8rem; font-weight:800; }
.pill { display:inline-block; padding:5px 11px; border-radius:20px; background:#e7f7f1; color:#087b5b; font-size:.78rem; font-weight:700; }
.info-box { background:#eaf3fb; border-left:5px solid #0d78a8; padding:15px 18px; border-radius:10px; }
div[data-testid="stMetric"] { background:white; border:1px solid #e2eaf2; padding:14px; border-radius:14px; }
.stButton>button, .stDownloadButton>button {
 background:#ef6b24; color:white; border:0; border-radius:10px; font-weight:700;
 padding:.65rem 1.2rem;
}
.stButton>button:hover, .stDownloadButton>button:hover { background:#d95716; color:white; }
a { color:#087ba8 !important; }
footer {visibility:hidden;}
</style>


""", unsafe_allow_html=True)

# ---------- Navigation ----------

# ---------- Navigation ----------
st.markdown("""
<style>
.nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 20px;
    margin-bottom: 20px;
    background: #ffffff;
    border-radius: 12px;
    border: 1px solid #e2eaf2;
}

.nav-brand {
    font-size: 25px;
    font-weight: 800;
    color: #0a3157;
}

.nav-links {
    display: flex;
    gap: 28px;
}

.nav-links a {
    color: #0a3157 !important;
    text-decoration: none;
    font-weight: 600;
}

.nav-links a:hover {
    color: #ed6a24 !important;
}
</style>

<div class="nav-container">
    <div class="nav-brand">🛡️ CareShield</div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#plans">Plans</a>
        <a href="#benefits">Benefits</a>
        <a href="#faqs">FAQs</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ---------- Hero ----------
st.markdown("""
<div class="hero" id="home">
  <div class="eyebrow">Health cover made simpler</div>
  <h1>Good health deserves<br>great protection.</h1>
  <p>Explore flexible health insurance plans designed to help you prepare for
  hospital bills, medical emergencies and life's unexpected turns.</p>
  <p><span class="pill">✓ Cashless hospital network</span> &nbsp;
  <span class="pill">✓ Family-friendly options</span></p>
</div>
""", unsafe_allow_html=True)

st.write("")
m1, m2, m3 = st.columns(3)
m1.metric("Cashless care", "Network hospitals", "Across India*")
m2.metric("Flexible cover", "₹3L – ₹25L", "Choose your sum insured")
m3.metric("Support", "24 × 7", "Help when you need it")
st.caption("*These are demonstration labels for the student project. Replace with verified insurer data before any real-world use.")

# ---------- Quick quote calculator ----------
st.markdown("<div class='section-title'>Get a quick estimate</div>", unsafe_allow_html=True)
st.markdown("<p class='muted'>Tell us a little about the cover you are exploring. The estimate is illustrative only.</p>", unsafe_allow_html=True)

with st.container(border=True):
    q1, q2, q3 = st.columns(3)
    with q1:
        adults = st.number_input("Adults (18 years & above)", min_value=1, max_value=6, value=1, step=1)
    with q2:
        children = st.number_input("Children", min_value=0, max_value=6, value=0, step=1)
    with q3:
        age = st.selectbox("Age of eldest adult", ["18–30", "31–40", "41–50", "51–60", "Above 60"])
    q4, q5 = st.columns(2)
    with q4:
        cover = st.selectbox("Sum insured", [300000, 500000, 1000000, 1500000, 2500000],
                             format_func=lambda x: f"₹{x/100000:.0f} lakh")
    with q5:
        city = st.selectbox("City type", ["Metro", "Non-metro"])
    
    # Illness category
    st.markdown("**Existing Illness / Medical Condition**")
    st.caption("Select the applicable category for this demonstration.")

    illness = st.selectbox(
        "Illness",
        ["No illness", "Mild illness", "Critical illness"],
        label_visibility="collapsed"
    )
    
    age_factor = {"18–30": 1.0, "31–40": 1.18, "41–50": 1.45, "51–60": 1.9, "Above 60": 2.5}[age]
    city_factor = 1.12 if city == "Metro" else 1.0
    
# Sample illness adjustments
if illness == "No illness":
    illness_charge = 0
elif illness == "Mild illness":
    illness_charge = 1000
else:
    illness_charge = 3000

    base = (cover / 100000) * 420
    estimate = int((
    base * age_factor *
    (1 + 0.45 * children + 0.65 * max(adults-1, 0)) *
    city_factor + illness_charge
) / 100) * 100
    if st.button("Calculate indicative premium", use_container_width=True):
        st.success(f"Illustrative annual premium: ₹{estimate:,} (excluding taxes and underwriting adjustments).")
        st.caption("This is a classroom demonstration formula, not an insurer quotation. Actual premiums depend on policy wording, age, location, medical history and underwriting.")

# ---------- Plans ----------
st.markdown("<div class='section-title' id='plans'>Choose a plan that fits your life</div>", unsafe_allow_html=True)
st.markdown("<p class='muted'>Compare sample plan tiers. Benefits and prices are fictional placeholders for this assignment.</p>", unsafe_allow_html=True)

plans = [
    ("Essential", "₹3 lakh", "₹4,999", "Everyday medical protection", ["Hospitalisation cover", "Day-care procedures", "Pre & post-hospitalisation"]),
    ("Plus", "₹10 lakh", "₹8,499", "A little more room to breathe", ["All Essential benefits", "Annual health check-up", "No-claim bonus*"]),
    ("Family Max", "₹25 lakh", "₹13,999", "One policy for your family", ["All Plus benefits", "Family floater option", "Restore benefit*"]),
]
cols = st.columns(3)
for col, plan in zip(cols, plans):
    name, sum_insured, premium, tagline, benefits = plan
    with col:
        st.markdown(f"""
        <div class="plan-card">
          <span class="pill">DEMO PLAN</span>
          <h3>{name}</h3>
          <p class="muted">{tagline}</p>
          <div class="price">{sum_insured}</div>
          <small class="muted">Sample sum insured</small>
          <hr>
          <b>Illustrative from {premium}/year</b>
          <ul>{''.join(f'<li>{b}</li>' for b in benefits)}</ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Explore {name}", key=f"plan_{name}", use_container_width=True):
            st.session_state["selected_plan"] = name
            st.info(f"{name} selected. Continue to the enquiry form below.")
st.caption("*Terms, exclusions and waiting periods would apply in a real policy. Refer to official policy wording.")

# ---------- Benefits with image ----------
st.markdown("<div class='section-title' id='benefits'>Protection beyond hospital bills</div>", unsafe_allow_html=True)
left, right = st.columns([1.05, 1])
with left:
    st.image(
        "https://images.unsplash.com/photo-1559757175-0eb30cd8c063?auto=format&fit=crop&w=1000&q=85",
        caption="Preventive care and healthier tomorrows",
        use_container_width=True
    )
with right:
    st.subheader("What can a health policy help cover?")
    benefits = {
        "Hospitalisation": "Eligible room, nursing, treatment and other covered hospital expenses.",
        "Day-care procedures": "Specified treatments that may not require a 24-hour hospital stay.",
        "Pre & post-hospitalisation": "Eligible medical expenses before and after a covered admission.",
        "Preventive health check-ups": "Check-ups where included in the selected policy.",
        "Cashless treatment": "Treatment at a network hospital, subject to approval and policy terms.",
        "Family floater": "A shared sum insured for covered family members under one policy."
    }
    for title, desc in benefits.items():
        with st.expander(title):
            st.write(desc)

# ---------- How it works ----------
st.markdown("<div class='section-title'>How it works</div>", unsafe_allow_html=True)
steps = st.columns(4)
for col, number, title, detail in zip(
    steps, ["01", "02", "03", "04"],
    ["Choose cover", "Share details", "Review terms", "Get insured"],
    ["Compare plans and sum insured.", "Provide accurate proposer details securely.", "Read exclusions, limits and waiting periods.", "Complete payment through the insurer."]
):
    with col:
        st.markdown(f"<div class='plan-card'><span class='eyebrow'>{number}</span><h3>{title}</h3><p class='muted'>{detail}</p></div>", unsafe_allow_html=True)

# ---------- Enquiry form ----------
st.markdown("<div class='section-title'>Request a call back</div>", unsafe_allow_html=True)
st.markdown("<p class='muted'>Use sample details for your classroom demonstration. This form does not submit data to an insurer.</p>", unsafe_allow_html=True)
with st.form("callback_form"):
    f1, f2 = st.columns(2)
    with f1:
        full_name = st.text_input("Full name")
        mobile = st.text_input("Mobile number", max_chars=10, placeholder="10-digit mobile number")
    with f2:
        email = st.text_input("Email address")
        preferred = st.selectbox("Preferred contact time", ["Morning", "Afternoon", "Evening"])
    consent = st.checkbox("I agree to be contacted for this demonstration enquiry.")
    submitted = st.form_submit_button("Submit enquiry", use_container_width=True)
    if submitted:
        if not full_name.strip() or len(mobile) != 10 or not mobile.isdigit() or "@" not in email:
            st.error("Please enter a name, a valid 10-digit mobile number and a valid email address.")
        elif not consent:
            st.warning("Please tick the consent box to continue.")
        else:
            st.success(f"Thank you, {full_name}! Your demo enquiry has been recorded on this page.")
            st.info("No personal information has been transmitted or stored. Connect a secure backend only if this becomes a real application.")

# ---------- Claims ----------
st.markdown("<div class='section-title'>Need to make a claim?</div>", unsafe_allow_html=True)
claim_col1, claim_col2 = st.columns([1, 1])
with claim_col1:
    st.image("https://images.unsplash.com/photo-1584515933487-779824d29309?auto=format&fit=crop&w=1000&q=85",
             caption="Support through the claims journey", use_container_width=True)
with claim_col2:
    st.subheader("A simple claims checklist")
    st.markdown("""
    1. Inform the insurer or claims helpdesk as early as possible.
    2. For cashless treatment, visit a network hospital and request pre-authorisation.
    3. For reimbursement, retain original bills, prescriptions and discharge summaries.
    4. Submit the required documents within the policy's stated timelines.
    5. Track the claim using the reference number provided by the insurer.
    """)
    st.markdown("<div class='info-box'>A claim is assessed against the policy wording, limits, exclusions and submitted documents. Approval is not automatic.</div>", unsafe_allow_html=True)

# ---------- FAQ ----------
st.markdown("<div class='section-title' id='faqs'>Frequently asked questions</div>", unsafe_allow_html=True)
faqs = {
    "What is health insurance?": "Health insurance is a contract in which an insurer covers specified healthcare expenses in return for a premium, subject to policy terms.",
    "What is a sum insured?": "It is the maximum amount payable by the insurer for covered claims during the policy period, subject to the policy wording.",
    "What is a waiting period?": "It is a specified period at the start of a policy during which certain illnesses or treatments may not be covered.",
    "What is a cashless claim?": "At a network hospital, the insurer may settle eligible expenses directly with the hospital after required approval.",
    "Can I cover my family?": "Some policies offer individual cover or a family floater. Check who is eligible and how the shared sum insured works.",
    "Are all treatments covered?": "No. Exclusions, sub-limits, co-payments, waiting periods and other conditions may apply."
}
for question, answer in faqs.items():
    with st.expander(question):
        st.write(answer)

# ---------- Footer ----------
st.markdown("---")
foot1, foot2 = st.columns([2, 1])
with foot1:
    st.markdown("### 🛡️ CareShield")
    st.caption("A student-built health insurance website prototype.")
with foot2:
    st.markdown("**Quick links**")
    st.markdown("[Plans](#plans) · [Benefits](#benefits) · [FAQs](#faqs)")
st.caption("DISCLAIMER: CareShield is a fictional educational prototype. It is not affiliated with ICICI Lombard or any insurer. Plan names, premiums, limits, features and network references are illustrative only. Do not use this demo to purchase insurance or submit real personal/medical information.")
