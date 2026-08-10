# SUBIIZ Search Engine 🚀

**SUBIIZ** is a lightweight, custom-built full-stack AI-powered search engine web application. This application uses a Python (Flask) backend and a pure HTML/CSS/JavaScript frontend to provide a Google-style clean UI and a fast AI search summary experience.

---

## 🌟 Key Features

* **AI Search Summaries:** Generates detailed and formatted answers in instant, rich-text HTML format for queries using the Groq API (`llama-3.3-70b-versatile`).
* **Live Web Results Scraping:** Scrapes and lists real-time top web search links and summaries using DuckDuckGo Web Scraping (`BeautifulSoup4`).
* **Clean UI/UX:** Fully responsive Google-inspired user interface including a dynamic typing placeholder effect, dark elements, and dynamic CSS formatting.
* **Custom Shortcuts Manager:** Provides the functionality to add and remove custom bookmark shortcuts using client-side `localStorage` in the browser.
* **Text-to-Speech (TTS):** Built-in Web Speech API integration, allowing users to listen to AI responses in Hindi and English.
* **User Analytics & Tracking:** Captures user actions inside the app (pages, clicked links, created shortcuts) at the `/track` tracking endpoint.
* **XSS & Script Cleaning:** Uses regular expressions (regex) in the backend to filter and clean malicious scripts, event handlers, and unwanted links from raw AI HTML responses.

---

## 🛠️ Tech Stack

### Backend
* **Python 3.x**
* **Flask** (Web Framework)
* **Flask-CORS** (Cross-Origin Resource Sharing)
* **Requests** (HTTP client for Groq API & DuckDuckGo)
* **BeautifulSoup4** (HTML Parsing & Web Scraping)

### Frontend
* **HTML5 & CSS3** (Custom styling, Flexbox, Animations)
* **JavaScript (Vanilla ES6)** (DOM manipulation, Async Fetch API, LocalStorage, Speech Synthesis)
* **FontAwesome** (Icons)

---

## 📁 Project Structure

```text
SUBIIZ-Search-Engine/
│
├── app.py                    # Main Flask backend application server
├── static/
│   └── SUBIIZ_LOGO.png       # Application favicon & logo assets
└── templates/
    └── index.html            # Main frontend interface file



```




### 🚀 Installation & Setup
1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

2. Clone the Repository

```bash
git clone [https://github.com/your-username/subiiz-search-engine.git](https://github.com/your-username/subiiz-search-engine.git)
cd subiiz-search-engine
```


### 3. Install Dependencies

``` bash
pip install flask flask-cors requests beautifulsoup4
```

### 4. Configure Groq AI Key
Set your Groq API Key inside the GroqAi variable in the app.py file
```bash
GroqAi = "YOUR_GROQ_API_KEY_HERE"
```

### 5. Run the Application

``` bash
python app.py
```

### Important: Open in your browser after the server starts:

```plain text
http://localhost:5000
```

### 📡 API Routes Summary

```
Method	Endpoint	Description
GET	/	
Renders the primary search interface (index.html)

GET	/search?q=<query>	
Scrapes DuckDuckGo and returns structured JSON web search results

GET	/ai-response?q=<query>	
Calls Groq LLM API to return rich styled HTML overview responses

POST	/track	
Logs user interaction events on the backend terminal
```


###  Developer Info

Developed by Zaid Ansari
