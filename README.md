# 📈 Big Tech Stock Explorer

A professional, interactive stock market web app built with Python and Streamlit. Explore the historical price performance of major Big Tech companies, compare growth, and simulate investments — all in your browser.

**🔗 Live App:** https://big-tech-stocks-hq5dwkokv7hxmger5sbljs.streamlit.app/

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A["📊 Plotly Built-in\nStock Data\n(px.data.stocks)"]
    B["🐍 Streamlit App\n(app.py)"]
    C["🐙 GitHub Repo\n(Big-tech-stocks)"]
    D["☁️ Streamlit Cloud\n(share.streamlit.io)"]
    E["🌐 User Browser"]

    A -->|"loaded via px.data.stocks()"| B
    B -->|"git push"| C
    C -->|"auto-deploy on push"| D
    D -->|"serves live app via HTTPS"| E

    style A fill:#4CAF50,color:#fff,stroke:#388E3C
    style B fill:#FF4B4B,color:#fff,stroke:#C62828
    style C fill:#24292e,color:#fff,stroke:#000
    style D fill:#1565C0,color:#fff,stroke:#0D47A1
    style E fill:#F57C00,color:#fff,stroke:#E65100
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏆 **Best Performer** | Instantly see which selected stock grew the most in the chosen period |
| 💰 **Investment Calculator** | Enter any amount and see what it would be worth today |
| 📅 **Date-Range Slider** | Zoom into any time window from Jan 2018 to Dec 2019 |
| 📊 **Growth Bar Chart** | Color-coded bar chart comparing total growth % per stock |
| ⚡ **Most Volatile** | Identifies the stock with the highest daily return standard deviation |

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open your browser at **http://localhost:8501**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web app framework — turns Python scripts into interactive UIs |
| **Plotly** | Interactive line and bar charts |
| **Pandas** | Data manipulation and date handling |

---

## 💡 Did You Know?

The original Apple I computer was sold for **$666.66** — not for any sinister reason, but simply because Steve Wozniak liked repeating digits. He later said he had no idea the number had any other connotations.
