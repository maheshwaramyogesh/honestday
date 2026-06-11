# 🧠 HonestDay — Behavioral Intelligence System

> *You don't have a time problem. You have an avoidance problem.*

**HonestDay** is not a productivity app. It is a behavioral mirror — revealing the avoidance patterns, emotional triggers, and blind spots that keep you stuck. It tracks your tasks honestly, scores your self-awareness, and uses AI to confront you with what is actually happening.

---

## 🔗 Live Links

| | Link |
|---|---|
| 🖥️ **Landing Page** | [honestdayy.netlify.app](https://honestdayy.netlify.app) |
| ⚡ **Live App** | [honestdayy.streamlit.app](https://honestdayy.streamlit.app) |

---

## 🎯 The Core Insight

Most tools measure output. HonestDay measures the **gap between intent and action** — the avoidance window, the emotional patterns, the blind spots that cost you weeks.

Every task you didn't do was a choice. You chose something else — comfort, distraction, fear of being judged. HonestDay makes that choice **visible as data.**

---

## 🧩 The Problem — Why You Procrastinate

| Trigger | What It Means |
|---|---|
| 🌊 **Overwhelm** | The task looks too big before you start. So you don't start. |
| 😴 **Boredom** | Your brain craves dopamine. If the task doesn't offer it, your mind finds something that does. |
| 😰 **Fear of Failure** | Overthinking kills more tasks than laziness ever did. |
| 🎯 **Perfectionism** | "Not perfect yet" is the most sophisticated form of procrastination. |
| ❓ **Ambiguity** | Your brain is waiting for clarity that will never arrive until you start. |

---

## ✨ Features

### 🔁 Behavioral Loader
Before entering the app, users are asked to think of something they've been putting off. This behavioral priming creates immediate personal relevance — the app confronts you before you even begin.

### 📊 Avoidance Clock
A canvas-drawn radial chart showing the breakdown of avoidance triggers across all logged sessions:
- Fear of Failure — 28%
- Overwhelm — 22%
- Low Dopamine — 17%
- Uncertainty — 11%
- Completed Honestly — 22%

### 📜 Scroll Story
A sticky 4-panel scroll narrative that takes the user through:
1. **The Pattern** — You don't have a time problem
2. **The Diagnosis** — You have an avoidance problem
3. **The Evidence** — We can prove it with data
4. **The Change** — Your first honest day starts now

### 🪞 Mirror Moment
A fixed behavioral observer widget in the bottom-right corner that watches the user's actual behavior on the page — time spent, scroll depth, clicks made — and confronts them with what they actually did vs what they intended to do. Escalates every 30 seconds.

### 🧪 Live Behavioral Diagnosis
An interactive participation section where users pick their avoidance trigger from a real scenario — and receive an immediate personalized behavioral diagnosis based on their selection.

### 🤖 AI Live Typewriter Analysis
A simulated live AI analysis card powered by **Groq / Llama-3.1** that reads behavioral data and types out a personalized confrontation in real time — not motivational advice, but a direct pattern identification.

> *"You consistently avoid tasks that require external judgment or expose uncertainty. This isn't about difficulty — your completion rate on hard tasks with clear outcomes is actually high. The pattern is specific: tasks where success depends on someone else's reaction are systematically delayed."*

### 🏆 Honesty Score System
A points system that rewards truthful self-reporting over performance:

| Action | Points | Why |
|---|---|---|
| ✅ Task Completed | +10 | You did the work |
| 💪 Hard Task Bonus | +5 | Difficult completions earn extra |
| ⚡ Partial Completion | +4 | Starting matters more than nothing |
| 🤝 Avoided — But Honest | +2 | Honesty earns more than pretending |

**The core philosophy:** A person who completes 5 tasks and honestly logs 3 avoidances scores higher than someone who completes 7 tasks but never admitted any struggle.

### 📈 Live Data Dashboard
Three real-time Plotly charts built from your actual CSV data:
- **Task Outcomes** — completed vs partial vs avoided
- **Avoidance Reasons** — what triggers your procrastination most
- **Difficulty vs Completion** — do you avoid hard tasks more?

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| App Framework | Python + Streamlit |
| Data Processing | Pandas |
| Data Visualization | Plotly |
| AI Inference | Groq API / Llama-3.1-8b-instant |
| Data Storage | CSV (flat file, auto-generated) |
| Landing Page | HTML + CSS + WebGL (GLSL shaders) + GSAP + ScrollTrigger |
| Fonts | Instrument Serif + Inter (Google Fonts) |
| Deployment | Streamlit Cloud + Netlify |

---

## 🌐 Landing Page — Technical Details

The landing page (`index.html`) is a single self-contained file with:

- **WebGL Particle System** — 180 particles representing tasks. Red particles (avoided tasks) drift outward from center. Green particles (completed tasks) orbit inward toward accountability. Mouse cursor repels all particles — avoidance behavior visualized physically.
- **GSAP + ScrollTrigger** — smooth scroll-based animations throughout every section
- **Magnetic Buttons** — buttons physically follow the cursor using GSAP elastic easing
- **Custom Dual Cursor** — red dot + lagging ring replaces the default cursor
- **Mirror Moment Widget** — fixed behavioral observer tracking real user behavior on page
- **Behavioral Loader** — GSAP timeline primes the user before entering the page
- **Scroll Story** — 4-panel sticky scroll narrative with pinned animations
- **AI Typewriter** — character-by-character typing effect with simulated thinking delay
- **Responsive Design** — mobile breakpoints at 980px and 580px

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Free [Groq API key](https://console.groq.com)

### Installation

```bash
# Clone the repo
git clone https://code.swecha.org/yogesh_0908/honestday.git
cd honestday

# Install dependencies
python -m pip install streamlit pandas plotly groq

# Run the app
python -m streamlit run app.py
```

### Configure Your API Key
In `app.py`, find and replace:
```python
client = Groq(api_key="YOUR_GROQ_KEY_HERE")
```

---

## 📁 Project Structure

```
honestday/
│
├── app.py                  # Streamlit application (main)
├── index.html              # Landing page (WebGL + GSAP + CSS)
├── tasks.csv               # Auto-generated on first task log
└── README.md               # This file
```

---

## 🧠 Score Formula

```
Score (%) = (completed × 10 + partial × 4 + avoided × 2 + hard_done × 5)
            ──────────────────────────────────────────────────────────────
                                total_tasks × 10
```

---

## 🤖 How The AI Insight Works

When "Generate My Insight" is clicked, the app builds a behavioral summary from your CSV data:

```python
summary = f"""
The user logged {total} tasks, avoided {avoided}.
Top avoidance reason: {top_reason}.
Hard tasks avoided: {hard_avoided}.
Give a short, honest, direct 3-sentence insight about their
procrastination pattern. No fluff.
"""
```

This is sent to **Groq's Llama-3.1-8b-instant** model which returns a personalized analysis in under 2 seconds.

---

## 📊 Behavioral Data — What The Research Shows

Based on patterns tracked in HonestDay sessions:
- **68%** of avoidance is driven by fear of failure or external judgment
- **54%** by cognitive overwhelm — the task feels larger than it is
- **41%** by low dopamine — the task feels unrewarding
- Most avoidance windows **open after 10am** — your highest performance is in the morning

---

## 🏆 Built At

**Hackathon 2026** — Built solo in under 8 hours from zero to deployed.

---

## 👤 Author

**Yogesh** — [@yogesh_0908](https://code.swecha.org/yogesh_0908)

---

## 📄 License

MIT — free to use, modify, and build on.

---

*"Every task you didn't do was a choice. HonestDay makes that choice visible."*