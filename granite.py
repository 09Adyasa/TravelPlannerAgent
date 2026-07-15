import os
from dotenv import load_dotenv
import streamlit as st
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

if "IBM_API_KEY" in st.secrets:

    API_KEY = st.secrets["IBM_API_KEY"]
    PROJECT_ID = st.secrets["IBM_PROJECT_ID"]
    URL = st.secrets["IBM_URL"]
    MODEL_ID = st.secrets["MODEL_ID"]

else:

    API_KEY = os.getenv("IBM_API_KEY")
    PROJECT_ID = os.getenv("IBM_PROJECT_ID")
    URL = os.getenv("IBM_URL")
    MODEL_ID = os.getenv("MODEL_ID")

# -----------------------------------
# Credentials
# -----------------------------------

credentials = Credentials(
    url=URL,
    api_key=API_KEY
)

# -----------------------------------
# Load Model
# -----------------------------------

model = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=PROJECT_ID
)

# -----------------------------------
# AI Travel Planner
# -----------------------------------

def generate_itinerary(
    source,
    destination,
    days,
    traveller,
    budget,
    weather
):

    prompt = f"""
You are an expert AI Travel Planner.

Generate a COMPLETE travel plan.

IMPORTANT RULES

- Never ask the user for more information.
- Never ask follow-up questions.
- Assume reasonable information wherever required.
- Return only the travel plan.
- Format everything beautifully in Markdown.

Travel Details

Source: {source}

Destination: {destination}

Duration: {days} days

Traveller Type : {traveller}

Budget : {budget}


Weather : {weather}

The itinerary should be optimized according to BOTH the selected travel style and weather.

If the user selected Beach + Sunny,
prefer beaches, islands, sunset viewpoints and water activities.

If the user selected Nature + Rainy,
recommend waterfalls, forests and backwaters.

If the user selected Mountains + Cold,
recommend snow viewpoints, ropeways and bonfire experiences.

Avoid suggesting activities that do not suit the selected weather.

# 🌍 Trip Overview

Write 2 paragraphs describing the destination.

# 📅 Day-wise Itinerary

Generate a UNIQUE itinerary for every day.

For every day include:

Morning

Breakfast

Afternoon

Lunch

Evening

Dinner

Night

Mention famous attractions.

Mention local experiences.

Mention shopping areas.

Mention hidden gems.

Do NOT repeat activities.

# 🍽 Local Food Recommendations

Give

• 6 famous dishes

• 3 street foods

• 2 desserts

• 3 cafes

• 3 restaurants

# 🚖 Recommended Transport

Suggest the best transportation options.

Include:

• Best way to reach the destination from the source

• Local transport options

• Budget-friendly transport

• Comfortable transport

• Estimated travel time within the destination

• Any useful travel tips regarding transport

# 🏨 Accommodation Recommendations

Recommend accommodation according to the user's budget.

Include:

Budget Hotels (3)

Mid-range Hotels (3)

Luxury Hotels (3)

For each hotel mention:

• Suitable traveller type

• Approximate price range per night

• Why it is recommended

Mention hotels that are popular and highly rated in the destination.

# 💰 Budget Suggestions

Suggest

Accommodation

Food

Transport

Activities

Shopping

# 🎒 Packing Checklist

According to the weather.

# 🛡 Safety Tips

Give practical safety tips.

# 🚑 Emergency Advice

Mention emergency precautions.

# ⭐ Travel Tips

Give useful travel hacks.

Return ONLY the travel plan.

The response must contain ALL sections in this exact order:

1. Trip Overview

2. Day Wise Itinerary

3. Must Try Foods

4. Recommended Transport

5. Accommodation Recommendations

6. Estimated Budget

7. Packing Checklist

8. Safety Tips

9. Emergency Advice

10. Extra Travel Tips

Do not skip any section.

Use Markdown headings for every section.
"""

    params = {
        "decoding_method": "sample",
        "temperature": 0.7,
        "top_p": 0.9,
        "max_new_tokens": 1200
    }

    try:

        response = model.generate_text(
            prompt=prompt,
            params=params
        )

        if isinstance(response, str):
            return response

        if isinstance(response, dict):

            if "results" in response:
                return response["results"][0]["generated_text"]

            if "generated_text" in response:
                return response["generated_text"]

        return str(response)

    except Exception as e:

        return f"""
# ❌ Watsonx Error

{str(e)}

Please check:

• IBM API Key

• Project ID

• Region

• Model ID
"""
