import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import date

st.set_page_config(page_title="HonestDay", page_icon="🧠", layout="wide")

# ── GLOBAL STYLES ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap');

* { font-family: 'Space Grotesk', sans-serif !important; }

.stApp {
    background: #0d0d0d !important;
    color: #f0f0f0 !important;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem !important; }

/* Inputs */
.stTextInput input {
    background: #1c1c1c !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 4px !important;
    color: #f0f0f0 !important;
    font-family: 'Space Mono', monospace !important;
}
.stTextInput input:focus {
    border-color: #c0392b !important;
    box-shadow: 0 0 0 1px #c0392b !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: #1c1c1c !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 4px !important;
    color: #f0f0f0 !important;
}
.stSelectbox > div > div:focus-within {
    border-color: #c0392b !important;
}

/* Dropdown options */
[data-baseweb="popover"] {
    background: #1c1c1c !important;
}
[role="option"] {
    background: #1c1c1c !important;
    color: #f0f0f0 !important;
}
[role="option"]:hover {
    background: #c0392b !important;
}

/* Button */
.stButton > button {
    background: #c0392b !important;
    color: white !important;
    border: none !important;
    border-radius: 2px !important;
    padding: 0.7rem 2rem !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    transition: all 0.3s !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: #e74c3c !important;
    box-shadow: 0 0 20px rgba(192,57,43,0.4) !important;
    transform: translateY(-2px) !important;
}

/* Headers */
h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -1px !important;
    color: #f0f0f0 !important;
}
h1 { font-size: 2.5rem !important; font-weight: 700 !important; }
h2 { color: #c0392b !important; font-size: 1.3rem !important; }

/* Metrics */
[data-testid="stMetric"] {
    background: #1c1c1c !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 4px !important;
    padding: 1.2rem !important;
}
[data-testid="stMetricValue"] {
    color: #c0392b !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 2rem !important;
}
[data-testid="stMetricLabel"] {
    color: #888 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* Progress bar */
.stProgress > div > div > div {
    background: #c0392b !important;
}
.stProgress > div > div {
    background: #1c1c1c !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 4px !important;
}

/* Success/Warning/Error */
.stSuccess {
    background: rgba(74,222,128,0.1) !important;
    border: 1px solid #4ade80 !important;
    border-radius: 4px !important;
    color: #4ade80 !important;
}
.stWarning {
    background: rgba(251,191,36,0.1) !important;
    border: 1px solid #fbbf24 !important;
    border-radius: 4px !important;
}
.stError {
    background: rgba(192,57,43,0.1) !important;
    border: 1px solid #c0392b !important;
    border-radius: 4px !important;
}
.stInfo {
    background: rgba(192,57,43,0.08) !important;
    border: 1px solid rgba(192,57,43,0.3) !important;
    border-radius: 4px !important;
    color: #f0f0f0 !important;
}

/* Divider */
hr { border-color: rgba(255,255,255,0.07) !important; }

/* Spinner */
.stSpinner > div { border-top-color: #c0392b !important; }

/* Labels */
label { 
    color: #888 !important; 
    font-family: 'Space Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🧠 HonestDay</h1>
    <p>Stop lying to yourself. Track tasks honestly. Understand your patterns. Beat procrastination with data.</p>
</div>
""", unsafe_allow_html=True)

# ── LOG TASK ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">📝 Log Your Task</div>', unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        task_name = st.text_input("Task Name", placeholder="What was the task?")
        difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    with col2:
        status = st.selectbox("Status", ["Completed", "Partial", "Avoided"])
        reason = st.selectbox("If avoided, why?", [
            "N/A", "Felt too overwhelming", "Too boring",
            "Fear of failure", "Got distracted", "No energy"
        ])
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        save = st.button("Save Task ✅")

    if save:
        if task_name.strip() == "":
            st.warning("Please enter a task name.")
        else:
            new_entry = {
                "Date": str(date.today()),
                "Task": task_name,
                "Difficulty": difficulty,
                "Status": status,
                "Reason": reason
            }
            df_new = pd.DataFrame([new_entry])
            if os.path.exists("tasks.csv"):
                df_new.to_csv("tasks.csv", mode='a', header=False, index=False)
            else:
                df_new.to_csv("tasks.csv", mode='w', header=True, index=False)
            st.success(f"✅ '{task_name}' saved successfully!")

# ── DASHBOARD ──────────────────────────────────────────────────────────────────
if os.path.exists("tasks.csv"):
    df = pd.read_csv("tasks.csv")

    st.markdown("---")
    st.markdown('<div class="section-header">📊 Your Dashboard</div>', unsafe_allow_html=True)

    # Stat cards
    total     = len(df)
    completed = len(df[df["Status"] == "Completed"])
    partial   = len(df[df["Status"] == "Partial"])
    avoided   = len(df[df["Status"] == "Avoided"])
    points    = (completed * 10) + (partial * 4) + (avoided * 2)
    hard_done = len(df[(df["Difficulty"] == "Hard") & (df["Status"] == "Completed")])
    points   += hard_done * 5
    max_pts   = total * 10
    score     = int((points / max_pts) * 100) if max_pts > 0 else 0

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, number, label in zip(
        [c1, c2, c3, c4, c5],
        [total, completed, partial, avoided, f"{score}%"],
        ["Total Tasks", "Completed", "Partial", "Avoided", "Honesty Score"]
    ):
        col.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{number}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.progress(score / 100)

    if score >= 80:
        st.markdown('<div class="score-great">🔥 Outstanding! You\'re crushing it. Keep this momentum going.</div>', unsafe_allow_html=True)
    elif score >= 60:
        st.markdown('<div class="score-good">💪 Good effort. You\'re making progress — push harder on difficult tasks.</div>', unsafe_allow_html=True)
    elif score >= 40:
        st.markdown('<div class="score-warn">⚠️ High avoidance detected. Be honest — what\'s really stopping you?</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="score-warn">🚨 Critical avoidance. You need to confront your patterns today.</div>', unsafe_allow_html=True)

    # Charts
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2, ch3 = st.columns(3)

    with ch1:
        st.markdown('<div class="section-header" style="font-size:1rem">Task Outcomes</div>', unsafe_allow_html=True)
        sc = df["Status"].value_counts().reset_index()
        sc.columns = ["Status", "Count"]
        fig1 = px.pie(sc, names="Status", values="Count",
                      color_discrete_sequence=["#c0392b", "#888888", "#f0f0f0"],
                      hole=0.5)
        fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white",
                           margin=dict(t=10, b=10), showlegend=True,
                           legend=dict(font=dict(color="white")))
        st.plotly_chart(fig1, use_container_width=True)

    with ch2:
        st.markdown('<div class="section-header" style="font-size:1rem">Why Avoided?</div>', unsafe_allow_html=True)
        av = df[df["Reason"] != "N/A"]
        if not av.empty:
            rc = av["Reason"].value_counts().reset_index()
            rc.columns = ["Reason", "Count"]
            fig2 = px.bar(rc, x="Reason", y="Count",
                          color="Count", color_continuous_scale=["#888", "#c0392b"])
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                               font_color="white", margin=dict(t=10, b=10),
                               xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No avoided tasks yet!")

    with ch3:
        st.markdown('<div class="section-header" style="font-size:1rem">Difficulty vs Completion</div>', unsafe_allow_html=True)
        fig3 = px.histogram(df, x="Difficulty", color="Status", barmode="group",
                            color_discrete_sequence=["#c0392b", "#888888", "#f0f0f0"],
                            category_orders={"Difficulty": ["Easy", "Medium", "Hard"]})
        fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="white", margin=dict(t=10, b=10),
                           xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig3, use_container_width=True)

    # Task log table
    st.markdown("---")
    st.markdown('<div class="section-header">📋 Task Log</div>', unsafe_allow_html=True)
    st.dataframe(df.sort_values("Date", ascending=False),
                 use_container_width=True, hide_index=True)

    # AI Insight
    st.markdown("---")
    st.markdown('<div class="section-header">🤖 AI Insight</div>', unsafe_allow_html=True)
    st.markdown("Click below to get a personalized analysis of your procrastination patterns.")

    if st.button("Generate My Insight 🧠"):
        with st.spinner("Analyzing your patterns..."):
            try:
                top_reason = df[df["Reason"] != "N/A"]["Reason"].value_counts().idxmax() \
                    if not df[df["Reason"] != "N/A"].empty else "unknown"
                hard_avoided = len(df[(df["Difficulty"] == "Hard") & (df["Status"] == "Avoided")])
                summary = (
                    f"The user logged {total} tasks, avoided {avoided}. "
                    f"Top avoidance reason: {top_reason}. "
                    f"Hard tasks avoided: {hard_avoided}. "
                    f"Give a short, honest, direct 3-sentence insight about their procrastination pattern. No fluff."
                )
                from groq import Groq
                import os
                from dotenv import load_dotenv

                load_dotenv()

                client = Groq(api_key=os.getenv("GROQ_API_KEY"))
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": summary}],
                    max_tokens=200
                )
                insight = response.choices[0].message.content
                st.markdown(f'<div class="insight-box">💡 {insight}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

else:
    st.markdown("---")
    st.info("👆 Log your first task above to see your dashboard!")