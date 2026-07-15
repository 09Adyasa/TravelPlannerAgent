def load_css():
    return """
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(135deg,#eef5ff,#f8fbff);
}

section[data-testid="stSidebar"]{

background:linear-gradient(
180deg,
#0F172A,
#1E293B
);

}

/* Sidebar headings */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label{

    color:white !important;

}

.hero{
    background:linear-gradient(135deg,#2563eb,#06b6d4);
    padding:22px;
    min-height:140px;
    border-radius:18px;
    color:white;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0 10px 30px rgba(0,0,0,.2);
}

.card{
    background:white;
    border-radius:18px;
    padding:22px;
    box-shadow:0 10px 25px rgba(0,0,0,.08);
    margin-bottom:20px;
    transition:0.3s;
}

.card:hover{

    transform:translateY(-3px);

    box-shadow:0 15px 35px rgba(37,99,235,.15);

}

.metric-card{
    background:white;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
}

.agent{
    background:#ffffff;
    border-left:6px solid #2563eb;
    padding:20px;
    border-radius:15px;
    box-shadow:0 6px 18px rgba(0,0,0,.08);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

.stButton button{

width:100%;

height:55px;

font-size:18px;

font-weight:700;

border-radius:15px;

background:linear-gradient(
90deg,
#2563EB,
#06B6D4
);

color:white;

border:none;

transition:0.3s;

}

.stButton button:hover{

transform:scale(1.03);

}

/* ==========================
   INPUT BOXES
========================== */

.stTextInput input{
    background:white !important;
    color:black !important;
    border-radius:10px;
}

/* ==========================
   SELECT BOX
========================== */

.stSelectbox [data-baseweb="select"]{

    color:black !important;

}

.stSelectbox [data-baseweb="select"] > div{

    background:white !important;

    color:black !important;

}

.stSelectbox [data-baseweb="select"] span{

    color:black !important;

}

.stSelectbox svg{

    fill:#2563eb !important;

}

/* ==========================
   MULTISELECT
========================== */

.stMultiSelect div[data-baseweb="select"] > div{
    background:white !important;
    color:black !important;
}

/* ==========================
   SLIDER
========================== */

.stSlider{
    padding-top:10px;
}

/* ==========================
   LABELS
========================== */

/* Sidebar labels only */

section[data-testid="stSidebar"] label{

    color:white !important;

}
/* ===== Fix Selectbox Text ===== */


div[data-baseweb="popover"]{
    background:#ffffff !important;
}

div[role="listbox"]{
    background:#ffffff !important;
}

div[role="option"]{
    color:#000000 !important;
}

div[role="option"]:hover{
    background:#e6f0ff !important;
}
/* Metric titles */

[data-testid="stMetricLabel"]{

    color:#1f2937 !important;

    font-weight:700 !important;

}

/* Metric values */

[data-testid="stMetricValue"]{

    color:#2563eb !important;

    font-weight:700 !important;

}
</style>
"""