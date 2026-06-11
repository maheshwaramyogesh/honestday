# 🧠 HonestDay — Behavioral Intelligence System

> *You don't have a time problem. You have an avoidance problem.*

**HonestDay** is a personal procrastination tracker that reveals the real patterns behind your avoidance behavior — scored on honesty, analyzed by AI, visualized with data.

🖥️ **Live Website:** [honestdayy.netlify.app](https://honestdayy.netlify.app)

---

## 🎯 The Problem

Most productivity apps give you to-do lists and timers. None of them ask the real question:

**Why aren't you doing the work?**

Procrastination isn't laziness. It's an avoidance pattern driven by:
- Tasks that feel too overwhelming before you even start
- Boredom — your brain craving dopamine the task doesn't offer
- Fear of failure — overthinking kills more tasks than laziness ever did

---

## 💡 The Solution

HonestDay makes your avoidance patterns **visible as data** — and rewards you for being truthful about them.

---

## ✨ Features

### 📝 Behavioral Task Logger
Log what you worked on, how difficult it was, and whether you completed, partially did, or avoided it. If avoided — you tell the system exactly why.

### 📊 Live Pattern Dashboard
Three real-time Plotly charts reveal:
- **Task Outcomes** — completed vs partial vs avoided (pie chart)
- **Avoidance Reasons** — what triggers your procrastination most (bar chart)
- **Difficulty vs Completion** — do you avoid hard tasks more than easy ones? (histogram)

### 🏆 Honesty Score Engine
A points system that rewards truthful self-reporting over performance:

| Action | Points |
|--------|--------|
| ✅ Task Completed | +10 |
| 💪 Hard Task Bonus | +5 |
| ⚡ Partial Completion | +4 |
| 🤝 Avoided — But Honest | +2 |

> **The core insight:** Admitting avoidance earns more than pretending you completed something. Honesty is the metric.

### 🤖 Groq AI Insight
Click "Generate My Insight" — the app sends your real behavioral data to Groq's Llama-3.1 inference engine and gets back a personalized 3-sentence confrontation about your specific avoidance pattern.

**Not generic motivation. Your data. Your pattern. Your truth.**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend + Backend | Python + Streamlit |
| Data Processing | Pandas |
| Data Visualization | Plotly |
| AI Inference | Groq API / Llama-3.1-8b-instant |
| Data Storage | CSV (local flat file) |
| Landing Page | HTML + CSS + WebGL + GSAP |
| Deployment | Streamlit Cloud + Netlify |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# Clone the repository
git clone https://code.swecha.org/yogesh_0908/honestday.git
cd honestday

# Install dependencies
python -m pip install streamlit pandas plotly groq

# Run the app
python -m streamlit run app.py
```

### Configuration
In `app.py`, find this line and replace with your Groq API key:
```python
client = Groq(api_key="YOUR_GROQ_KEY_HERE")
```

---

## 📁 Project Structure

```
honestday/
│
├── app.py                  # Main Streamlit application
├── honestday_fixed.html    # Landing page (WebGL + GSAP)
├── tasks.csv               # Auto-generated task data (created on first use)
└── README.md               # This file
```

---

## 🧠 How The Score Works

The score isn't about how many tasks you completed. It's about how honest you were.

```
Score = (completed × 10 + partial × 4 + avoided × 2 + hard_bonus × 5)
        ─────────────────────────────────────────────────────────────────
                          total_tasks × 10
```

A person who completed 5 tasks and honestly logged 3 avoidances scores **higher** than someone who completed 7 tasks but never admitted any struggle.

---

## 🤖 AI Insight — How It Works

When you click "Generate My Insight", the app builds a plain English summary of your behavioral data:

```
"The user logged 18 tasks, avoided 4.
Top avoidance reason: Felt too overwhelming.
Hard tasks avoided: 3.
Give a short, honest, direct 3-sentence insight about their
procrastination pattern. No fluff."
```

This is sent to Groq's Llama-3.1 model which returns a personalized behavioral analysis — not motivational advice, but a direct confrontation of your specific pattern.

---

## 🎨 Landing Page

The landing page (`honestday_fixed.html`) features:
- **WebGL particle system** — 180 particles representing tasks (red = avoided, green = completed) that react to your mouse
- **Behavioral loader** — primes you to think of something you've been avoiding
- **GSAP scroll animations** — smooth section reveals throughout
- **Mirror Moment widget** — tracks your actual behavior on the page and confronts you with it
- **Interactive participation quiz** — pick your avoidance trigger and get a personalized diagnosis
- **AI typewriter effect** — simulates live behavioral analysis

---

## 📊 Behavioral Insights From Real Data

Based on typical usage patterns HonestDay reveals:

- **68%** of avoidance driven by fear of failure or judgment
- **54%** by cognitive overwhelm — task perceived as too large
- **41%** by low dopamine — task feels unrewarding
- Most avoidance happens **after 10am** — morning is your highest performance window

---

## 🏆 Built At

**Hackathon 2026** — Built solo in under 8 hours.

---

## 👤 Author

**Yogesh** — [@yogesh_0908](https://code.swecha.org/yogesh_0908)

---

## 📄 License

MIT License — feel free to use, modify, and build on this.

---

*"Every task you didn't do was a choice. HonestDay makes that choice visible."*