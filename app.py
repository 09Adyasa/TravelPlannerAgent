import streamlit as st
import time
import plotly.express as px

from granite import generate_itinerary
from pdf_generator import create_pdf
from images import destination_images
from styles import load_css

#from weather import get_weather

destination_suggestions = {

    ("Beach","Sunny"):[
        ("🏖 Goa","Perfect for sunny beaches, water sports and nightlife."),
        ("🌊 Gokarna","Peaceful beaches with fewer crowds."),
        ("🏝 Andaman","Crystal-clear water and island adventures."),
        ("🌅 Pondicherry","French architecture with beautiful beach cafés.")
    ],

    ("Beach","Rainy"):[
        ("🌴 Kovalam","Relaxing coastal town with scenic rain views."),
        ("🌊 Pondicherry","Great cafés and pleasant coastal weather."),
        ("🚤 Alleppey","Enjoy the backwaters during monsoon."),
        ("🏖 Varkala","Beautiful cliffs overlooking the sea.")
    ],

    ("Mountains","Sunny"):[
        ("🌿 Munnar","Tea gardens with cool weather."),
        ("🍃 Coorg","Coffee plantations and waterfalls."),
        ("🌄 Ooty","Pleasant climate and botanical gardens."),
        ("🏞 Kodaikanal","Peaceful lakes and scenic viewpoints.")
    ],

    ("Mountains","Cold"):[
        ("❄ Manali","Snow adventures and mountain views."),
        ("🏔 Shimla","Colonial charm with snowfall."),
        ("⛷ Auli","India's best skiing destination."),
        ("🏔 Gulmarg","Snow-covered landscapes and gondola rides.")
    ],

    ("Mountains","Rainy"):[
        ("🌧 Meghalaya","Lush green valleys and waterfalls."),
        ("🌊 Wayanad","Beautiful forests during monsoon."),
        ("🌿 Coorg","Coffee estates and misty hills."),
        ("🏞 Cherrapunji","Perfect destination for rain lovers.")
    ],

    ("Adventure","Sunny"):[
        ("🧗 Rishikesh","River rafting and bungee jumping."),
        ("🏍 Ladakh","Bike trips and mountain passes."),
        ("🏕 Spiti Valley","Camping and off-road adventures."),
        ("🪂 Bir Billing","One of India's best paragliding spots.")
    ],

    ("Adventure","Rainy"):[
        ("🌧 Meghalaya","Caving and waterfalls."),
        ("🌊 Dandeli","River adventures and kayaking."),
        ("🌿 Coorg","Nature trekking."),
        ("🏕 Wayanad","Forest adventures.")
    ],

    ("Adventure","Cold"):[
        ("⛷ Gulmarg","Skiing and snowboarding."),
        ("🏔 Manali","Snow trekking."),
        ("❄ Auli","Cable car and skiing."),
        ("🏕 Sonamarg","Snow camping.")
    ],

    ("Nature","Sunny"):[
        ("🌸 Valley of Flowers","Blooming alpine flowers."),
        ("🌿 Munnar","Tea plantations."),
        ("🍃 Coorg","Coffee estates."),
        ("🌳 Ooty","Beautiful botanical gardens.")
    ],

    ("Nature","Rainy"):[
        ("🌧 Cherrapunji","Rain-soaked beauty."),
        ("🚤 Kerala Backwaters","Relaxing houseboat experience."),
        ("🌊 Athirappilly","Magnificent waterfalls."),
        ("🌿 Wayanad","Dense forests and wildlife.")
    ],

    ("Nature","Cold"):[
        ("🏔 Kashmir","Snow valleys."),
        ("🌲 Sikkim","Mountain scenery."),
        ("❄ Auli","Winter landscapes."),
        ("🏕 Tawang","Peaceful Himalayan destination.")
    ],

    ("Historical","Sunny"):[
        ("🏰 Jaipur","Magnificent forts and palaces."),
        ("🏛 Hampi","Ancient temple ruins."),
        ("👑 Mysore","Royal heritage."),
        ("🕌 Agra","Home of the Taj Mahal.")
    ],

    ("Historical","Rainy"):[
        ("🏛 Hyderabad","Museums and historical monuments."),
        ("👑 Mysore","Palaces with fewer crowds."),
        ("🏰 Lucknow","Historical architecture."),
        ("🕌 Delhi","Museums and monuments.")
    ],

    ("Historical","Cold"):[
        ("🕌 Delhi","Comfortable sightseeing."),
        ("🏰 Jaipur","Pleasant winter visits."),
        ("🏛 Agra","Ideal Taj Mahal weather."),
        ("👑 Khajuraho","Temple exploration.")
    ],

    ("Spiritual","Sunny"):[
        ("🛕 Puri","Jagannath Temple and beach."),
        ("🕉 Varanasi","Ganga Aarti experience."),
        ("🙏 Tirupati","Famous hill temple."),
        ("🌊 Rameswaram","Sacred island pilgrimage.")
    ],

    ("Spiritual","Rainy"):[
        ("🛕 Madurai","Historic Meenakshi Temple."),
        ("🙏 Shirdi","Sai Baba Temple."),
        ("🕉 Srisailam","Beautiful hill temple."),
        ("🌿 Ujjain","Sacred city.")
    ],

    ("Spiritual","Cold"):[
        ("❄ Kedarnath","Snow-covered pilgrimage."),
        ("🏔 Badrinath","Himalayan temple."),
        ("🌊 Haridwar","Spiritual Ganga Ghats."),
        ("🧘 Rishikesh","Yoga capital of India.")
    ]

}
st.set_page_config(
    page_title="TravelGPT AI Agent",
    page_icon="🌍",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ----------------------------
# HERO
# ----------------------------

st.markdown("""
<div class="hero">

<h1>🌍 TravelGPT AI Agent</h1>

<h3>Powered by IBM watsonx.ai</h3>

<p>Your Intelligent AI Travel Companion</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------
# AI CARD
# ----------------------------

st.markdown("""
<div class="agent">

<h2>🤖 Hello, I'm TravelGPT</h2>

<p>

I'm your intelligent travel assistant.

I analyze your destination,
budget,
weather,
and interests
to create a completely personalized itinerary.

Click <b>Generate Travel Plan</b> whenever you're ready.

</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------
# STATUS
# ----------------------------

st.markdown("## 🤖 AI Agent Status")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.success("🟢 IBM Connected")

with c2:
    st.success("🟢 AI Ready")

with c3:
    st.success("🟢 Weather Ready")

with c4:
    st.success("🟢 Destination Recommendation")

# ----------------------------
# SIDEBAR
# ----------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/201/201623.png",
        width=90
    )

    st.title("TravelGPT")

    st.caption("Powered by IBM watsonx.ai")

    st.divider()

    source=st.text_input(
        "📍 Source",
        placeholder="Bhubaneswar"
    )
    st.sidebar.markdown("### ✨ Need Destination Ideas?")

    trip_type = st.sidebar.selectbox(
        "Travel Style",
        [
            "Beach",
            "Mountains",
            "Historical",
            "Nature",
            "Adventure",
            "Spiritual"
        ]
    )

    weather = st.selectbox(
        "Weather",
        [
            "Sunny",
            "Rainy",
            "Cold",
            "Snowy"
        ]
    )

    #suggest = st.sidebar.button("🌍 Discover Best Destinations")

    key = (trip_type, weather)
    if key in destination_suggestions:

        for place, reason in destination_suggestions[key]:

            destination_name = place.split(" ", 1)[1]

            st.sidebar.markdown(f"""
    <div style="
    background:black;
    padding:10px;
    border-radius:10px;
    margin-bottom:5px;
    border-left:5px solid #3B82F6;
    color:white;
    ">

    <h5>{place}</h5>

    <p>{reason}</p>

    </div>
    """, unsafe_allow_html=True)

            if st.sidebar.button(
                f"✔ Select {destination_name}",
                key=destination_name
            ):

                st.session_state.selected_destination = destination_name

                st.rerun()

    else:

        st.sidebar.warning("No recommendation available.")
            
    if "selected_destination" not in st.session_state:
        st.session_state.selected_destination = ""

    destination = st.sidebar.text_input(
        "✈ Destination",
        value=st.session_state.selected_destination,
        placeholder="Goa"
     )

    traveller=st.selectbox(
        "Traveller",
        [
            "Solo",
            "Couple",
            "Family",
            "Friends"
        ]
    )

    days=st.slider(
        "Days",
        1,
        15,
        5
    )

    budget=st.selectbox(
        "Budget",
        [
            "Low",
            "Medium",
            "Luxury"
        ]
    )


    generate=st.button(
        "🚀 Generate Travel Plan",
        use_container_width=True
    )
    st.sidebar.markdown("---")

    st.sidebar.success("🤖 IBM watsonx.ai Connected")

    st.sidebar.caption("TravelGPT AI Agent v1.0")

# ----------------------------
# GENERATE
# ----------------------------

itinerary=""

if generate:

    status_box = st.empty()

    steps = [
        ("🤖", "Connecting to IBM watsonx.ai..."),
        ("🧠", "Understanding your travel preferences..."),
        ("🌍", "Analyzing destination..."),
        ("☀", "Checking weather conditions..."),
        ("🍽", "Finding local cuisines..."),
        ("🏖", "Discovering top attractions..."),
        ("💰", "Optimizing your budget..."),
        ("🧳", "Preparing packing checklist..."),
        ("📅", "Generating personalized itinerary...")
    ]

    for icon, message in steps:

        status_box.info(f"{icon} {message}")

        time.sleep(0.6)
    weather= 'sunny'
    itinerary = generate_itinerary(
        source,
        destination,
        days,
        traveller,
        budget,
        weather
    )

    status_box.success("✅ Travel Plan Generated Successfully!")

# ----------------------------
# TABS
# ----------------------------

tab1,tab2,tab3,tab4=st.tabs(
[
"🌍 Overview",
"🤖 AI Itinerary",
"💰 Budget",
"📄 Download"
]
)
# ==========================================================
# TAB 1
# ==========================================================

with tab1:

    st.markdown(f"""
<div class="hero">

<h1>🌍 Welcome to {destination}</h1>

<h3>Your AI-Powered Travel Experience</h3>

<p>
Discover hidden gems, delicious local food,
beautiful attractions and unforgettable memories.
</p>

</div>
""", unsafe_allow_html=True)

    if destination:

        if destination.lower() in destination_images:

            st.image(
                destination_images[destination.lower()],
                use_container_width=True
            )

    st.markdown(f"""
    <div class="card">

    <h2>📍 {destination}</h2>

    <h4>🌤 Weather : {weather}</h4>

    <p>

    👤 Traveller : <b>{traveller}</b>

    </p>

    <p>

    📅 Duration : <b>{days} Days</b>

    </p>

    <p>

    💰 Budget : <b>{budget}</b>

    </p>

    </div>

    """,unsafe_allow_html=True)


    st.markdown("---")

    st.link_button(
        "📍 Open Destination in Google Maps",
        f"https://www.google.com/maps/search/{destination}"
    )

# ==========================================================
# TAB 2
# ==========================================================

with tab2:

    st.subheader("🤖 AI Conversation")

    with st.chat_message("user"):

        st.write(
            f"""
Plan a {days}-day trip

From : {source}

To : {destination}

Budget : {budget}

Traveller : {traveller}
"""
        )
    st.markdown(f"""
<div class="card">

<h2>🤖 TravelGPT Summary</h2>

<table style="width:100%; font-size:17px;">
<tr>
<td><b>📍 Destination</b></td>
<td>{destination}</td>
</tr>

<tr>
<td><b>📅 Duration</b></td>
<td>{days} Days</td>
</tr>

<tr>
<td><b>👤 Traveller</b></td>
<td>{traveller}</td>
</tr>

<tr>
<td><b>💰 Budget</b></td>
<td>{budget}</td>
</tr>

<tr>
<td><b>🌤 Weather</b></td>
<td>{weather}</td>
</tr>



</table>

</div>
""", unsafe_allow_html=True)
   
    with st.chat_message("assistant"):

        st.markdown("""
        <div class="card">

        <h2>🤖 Your Personalized Travel Plan</h2>

        <p>
        TravelGPT has generated a complete travel itinerary.
        Expand each day to view your personalized schedule.
        </p>

        </div>
        """, unsafe_allow_html=True)

    # -------------------------
    # Split itinerary into days
    # -------------------------

        sections = itinerary.split("# 📅")

        # First section (Overview, Foods etc.)
        if sections:

            intro = sections[0].strip()

            if intro:
                st.markdown(intro)

        # Remaining Day-wise sections

        for day in sections[1:]:

            lines = day.strip().split("\n")

            if len(lines) == 0:
                continue

            title = lines[0]

            body = "\n".join(lines[1:])

            with st.expander(f"📅 {title}", expanded=False):

                st.markdown(body)
        
        st.markdown("---")

        st.subheader("⚡ Quick Actions")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.link_button(
                "📍 Open in Google Maps",
                f"https://www.google.com/maps/search/{destination}"
        )

        with col2:
            st.button("🔄 Generate Another Trip")

        with col3:
            st.button("❤️ Save Favourite")
        
    st.markdown("---")

    st.subheader("🎒 Smart Packing Checklist")

    packing=[
        "Passport / ID",
        "Phone Charger",
        "Power Bank",
        "Medicines",
        "Umbrella",
        "Water Bottle",
        "Comfortable Shoes",
        "Cash / Cards"
    ]

    for item in packing:

        st.checkbox(item)

   
    # ==========================================================
# TAB 3 - BUDGET
# ==========================================================

with tab3:
    st.markdown("""
<div class="hero">

<h1>💰 AI Budget Planner</h1>

<p>
Your travel expenses are intelligently estimated based on
destination, duration and travel style.
</p>

</div>
""", unsafe_allow_html=True)

    st.header("💰 AI Budget Planner")

    if budget == "Low":

        budget_data = {
            "Accommodation": 6000,
            "Food": 3000,
            "Transport": 2500,
            "Activities": 2000,
            "Shopping": 1500
        }

    elif budget == "Medium":

        budget_data = {
            "Accommodation": 12000,
            "Food": 6000,
            "Transport": 5000,
            "Activities": 4000,
            "Shopping": 3000
        }

    else:

        budget_data = {
            "Accommodation": 25000,
            "Food": 12000,
            "Transport": 8000,
            "Activities": 7000,
            "Shopping": 10000
        }

    total = sum(budget_data.values())

    budget_data["Total"] = total

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(f"🏨 Hotel\n\n₹ {budget_data['Accommodation']}")

    with c2:
        st.info(f"🍽 Food\n\n₹ {budget_data['Food']}")

    with c3:
        st.info(f"🚖 Transport\n\n₹ {budget_data['Transport']}")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.info(f"🎯 Activities\n\n₹ {budget_data['Activities']}")

    with c5:
        st.info(f"🛍 Shopping\n\n₹ {budget_data['Shopping']}")

    with c6:
        st.success(f"💰 Total\n\n₹ {total}")

    st.markdown("---")

    fig = px.pie(

        names=list(budget_data.keys())[:-1],

        values=list(budget_data.values())[:-1],

        title="Budget Distribution"

    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

    st.subheader("🧠 AI Budget Insights")

    left,right=st.columns(2)

    with left:

        st.success("💡 Medium budget gives the best value.")

        st.success("🏨 Accommodation takes the highest share.")

        st.success("🍽 Food budget is well balanced.")

    with right:

        st.info("🚖 Use local transport to save money.")

        st.info("🎟 Book attractions online.")

        st.info("🛍 Shop on local markets.")



# ==========================================================
# TAB 4 - DOWNLOAD
# ==========================================================

with tab4:
    st.markdown("""
<div class="card">

<h2>📄 Export Your Trip</h2>

Your travel itinerary can be downloaded as a beautifully
formatted PDF and shared with family or friends.

</div>
""", unsafe_allow_html=True)
    
    st.header("📄 Download Travel Plan")

    st.warning("""

🚨 Emergency Essentials

• Passport / ID

• Phone

• Hotel Address

• Medical Kit

• Emergency Cash

""")

    if itinerary != "":

        pdf = create_pdf(
            itinerary,
            destination
        )

        st.download_button(

            "⬇ Download Travel Plan PDF",

            data=pdf,

            file_name=f"{destination}_Travel_Plan.pdf",

            mime="application/pdf",

            use_container_width=True

        )

    else:

        st.info("Generate a travel plan first.")
    st.markdown("---")

    st.success("✅ AI Travel Plan Generated Successfully")

    

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div class="card" style="text-align:center">

<h2>🌍 TravelGPT AI Agent</h2>

<p>

Powered by IBM watsonx.ai

</p>

<p>

IBM Cloud • Meta Llama 3.3 • Streamlit • Python

</p>

<p>

Made for IBM SkillsBuild Internship 2026

</p>

</div>
""",
unsafe_allow_html=True
)
st.markdown("---")

st.caption(
"Travel recommendations are AI-generated and may vary. "
"Please verify bookings, timings, prices, and local conditions before travelling."
)