import streamlit as st
from main import get_weather, get_prayer_times

st.set_page_config(
    page_title="Weather & Prayer Times",
    page_icon="🌙",
    layout="wide",
)

city = st.text_input("Enter your city", value="Lahore")

if st.button("Get Weather & Prayer Times", type="primary"):
    if not city.strip():
        st.warning("Please enter a city name.")
    else:
        try:
            with st.spinner("Fetching live data..."):
                weather_city, temperature = get_weather(city.strip())
                prayer_times = get_prayer_times(city.strip())

            st.session_state["weather_city"] = weather_city
            st.session_state["temperature"] = temperature
            st.session_state["prayer_times"] = prayer_times

        except Exception as error:
            st.error("Could not fetch data. Check the city and internet connection.")
            st.caption(str(error))

temperature = st.session_state.get("temperature")
weather_city = st.session_state.get("weather_city")
prayer_times = st.session_state.get("prayer_times")

if temperature is None:
    theme = "moon"
    title = "Your sky, your salah"
    subtitle = "Discover your weather and daily prayer times."
    weather_icon = "🌙"
    description = "Enter your city to get started."
elif temperature <= 15:
    theme = "moon"
    title = "A calm, moonlit day"
    subtitle = "A little warmth, a moment of peace."
    weather_icon = "🌙"
    description = "Cool weather"
elif temperature >= 30:
    theme = "sun"
    title = "Chasing the sunshine"
    subtitle = "Stay cool, stay grateful, keep your salah."
    weather_icon = "☀️"
    description = "Warm weather"
else:
    theme = "twilight"
    title = "A beautiful day to begin"
    subtitle = "Check the sky. Make time for prayer."
    weather_icon = "🌤️"
    description = "Mild weather"

if theme == "moon":
    background = "linear-gradient(135deg, #06152f, #123c70, #071020)"
    accent = "#62b8ff"
elif theme == "sun":
    background = "linear-gradient(135deg, #321322, #a94b20, #f3a43b)"
    accent = "#ffb45e"
else:
    background = "linear-gradient(135deg, #101b32, #51416b, #a66b54)"
    accent = "#d9b4ff"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {background};
        color: #ffffff;
    }}
    [data-testid="stHeader"] {{
        background: transparent;
    }}
    .block-container {{
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}
    .hero {{
        text-align: center;
        padding: 2rem 1rem;
        border: 1px solid rgba(255,255,255,.2);
        border-radius: 24px;
        background: rgba(5,15,35,.28);
        margin-bottom: 1.5rem;
    }}
    .hero-icon {{
        font-size: 4rem;
    }}
    .hero h1 {{
        color: white;
        font-size: 2.5rem;
    }}
    .hero p {{
        color: #e0e7f5;
        font-size: 1.1rem;
    }}
    .panel {{
        background: rgba(5,15,35,.55);
        border: 1px solid rgba(255,255,255,.2);
        border-radius: 20px;
        padding: 1.4rem;
        min-height: 150px;
        margin-bottom: 1rem;
    }}
    .panel h3 {{
        color: {accent};
    }}
    .prayer {{
        text-align: center;
        background: rgba(5,15,35,.5);
        border: 1px solid rgba(255,255,255,.2);
        border-radius: 16px;
        padding: 1.2rem .4rem;
        margin-bottom: .6rem;
    }}
    .prayer h3 {{
        color: {accent};
        font-size: 1.1rem;
    }}
    .prayer p {{
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
    }}
    div.stButton > button[kind="primary"] {{
        background: {accent};
        color: #101522;
        border: none;
        border-radius: 12px;
        font-weight: 700;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-icon">{weather_icon}</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if weather_city is not None and temperature is not None:
    left, right = st.columns([1, 1])

    with left:
        st.markdown(
            f"""
            <div class="panel">
                <h3>{weather_icon} Current Weather</h3>
                <h1>{temperature:.1f} °C</h1>
                <p>{weather_city} · {description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="panel">
                <h3>🕋 A moment of peace</h3>
                <p>Let your day be guided by faith, gratitude and prayer.</p>
                <p>Make space for what matters.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("## 🕌 Daily Prayer Times")

    if prayer_times:
        columns = st.columns(5)
        for column, (name, time) in zip(columns, prayer_times.items()):
            with column:
                st.markdown(
                    f"""
                    <div class="prayer">
                        <h3>{name}</h3>
                        <p>{time}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
else:
    st.info("Enter a city above and select Get Weather & Prayer Times.")

st.markdown("---")
st.caption("Weather & Prayer Times · Stay grateful. Keep your salah.")
