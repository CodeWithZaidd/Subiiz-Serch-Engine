from flask import Flask, jsonify, request, render_template
import requests
from flask_cors import CORS
from bs4 import BeautifulSoup
import re
import os

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

@app.route('/track', methods=['POST'])
def tracker():
    data = request.json
    action = data.get('action', 'Unknown')
    details = data.get('details', '')
    print(f"[USER ACTION CAPTURED]:: Action: {action} || Details: {details}")
    return jsonify({'status': "SUCCESS"})

@app.route('/')
def home():
    return render_template('index.html')

def clean_ai(html_text):
    #1.script js ka sara hta do
    html_text = re.sub(r'<script\b[^<]*0*<\/script>','', html_text, flags=re.IGNORECASE)

    #Agar koi iframe,object embed ya form tag aya toh uda do
    html_text = re.sub(r'<(iframe|object|embedd|form|link|meta)\b[^>]*.*?<\/\1>', '', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'<(iframe"objet|embed|form|link|meta)\b[^>]*\/?>', '', html_text, flags=re.IGNORECASE)

    #3.html tags ke andrinline event uda do
    html_text = re.sub(r'\s+on\w+\s*=\s*(["\']).*?\1', '', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'\s+on\w+\s*=[^\s>]+', '', html_text, flags=re.IGNORECASE)

    #4.agr koi javas link hai toh de
    html_text = re.sub(r'href\s*=\s*(["\'])javascript:.*?\1', 'href="#"', html_text, flags=re.IGNORECASE)
    return html_text

GroqAi = os.environ.get("GroqAi", "PASTE_HERE_YOUR_GROQ_AI_API")
@app.route('/ai-response', methods=['GET'])
def ai_response():
    query = request.args.get('q') or request.args.get('query', '')

    if not query:
        return jsonify({"eroor": "QUERY ARE NOT FOUND"}), 400

    if not GroqAi:
        return jsonify({"Reply": "GEMINI KEY MISING HAI"})

    print(f"[LOG]: SEARCH FOUND: {query}")
    final_prompt = (
    query + 
    ". CRITICAL INSTRUCTIONS: "
    "1. At the very top, provide a clear short answer inside a styled HTML div with a background color (e.g., <div style='background-color: #f0f4f8; padding: 15px; border-left: 5px solid #0066cc; border-radius: 6px; margin-bottom: 20px;'><b>Quick Overview:</b> ...</div>). "
    "2. Below the summary, write a **VERY LONG, DEEP, EXTENSIVE, AND FULLY DETAILED** answer covering every single aspect, explanation, and history. Make it comprehensive and massive. "
    "3. STRICT FORMATTING RULE: Do NOT use any Markdown formatting like asterisks (**), hashes (#), or code blocks (```). Output ONLY pure, raw HTML tags (like <h3>, <p>, <b>, <ul>, <li>) and inline CSS properties. Absolutely NO JavaScript and NO markdown syntax. The output must be directly ready for standard browser innerHTML rendering."
    "4. IF I SAY GIVE ME LINK OF WHATSAPP, FACEBOOK,YOUTUBE,ANY LINK so using <a>(<a href='which is i say like whatsapp link here'>WhatSapp</a> like that) and then give me link which is i say"
    "5. IF I ASK WHO IS SUBIIZ OR HOW ARE SUBIIZ , JUST SAY YOU ARE USING THE WEBSITE WHICH NAME IS SUBIIZ AND THE DEVLOPER OF SUBIIZ IS ZAID ANSARI STUDYING IN CLASS 8 AND SAY COOL SENTECE FOR SUBIIZ AND ITS DEVOLOPER ZAID ANSARI AND ALSO SAY I AM SUBIIZ ON TOP SENTENCE FIRST SENTENCE IS I AM SUBIIZ , NIVE TO MEET YOU MY DEVOLOPER IS ZAID ANSARI....... AND NEVER SAY LIKE I SAY YOU THAT SAY COOL WORDS OR ETC SO YOU NEVER SAY THIS LIKE::-- HOW ITS COOL CAN I SAY MORE COOL NEVER SAY THIS.... AND ALSO SAY I AM SERACH ENGINE SUBIIZ"
    "6. IN the last massage you can ask varuous question like i say who is google,subiiz and AND RELATED TO MY QUESTION NOT OTHER etc so so can ask in the last sentece that can you provide more info or can you say me what are you finding or etc in your self ask like this question... AND NEVER PROVIDE ANY LINK OF SUBIIZ UNTILL I SAID"
    "7. AND ALSO YOU DONT GIVE ME MORE THAN 20 SENTENCE MESSAGE STRICTLY.. STICTLY USING 20 SENTENTCE FOR MY ANSWER ALSO USING H1 TAG AND FEEL LIKE YOU ARE GOOGLE SEARCH ENGINE"
    "8. AND WHEN I ASK MATH AUR GK QUESTION THEN YOU PROVIDE MESSAGE MORE DEEP CLEAN SOLUTION AND VERY EASY TO SOLVE MATH QUESTION...  AND TEACH LIKE YOU ARE WORLD BEST TEAHCER PROPER SOLUTION LIKE 9^X-4 = 1 SOLUTION = WE CAN SAY 1 == 9^0 = 1, THEN 9^X = 9^0+4 = 9^X =  9^4 = X = 9^4/9 = 4... THE ANSWER IS 4   PROPERLY SOLVE IT NOT ONLY USING USING SENTENCE TO TEACHH....."
    "9. AND ASLO USE YOURSELF ONLY HTML CSS TO COOL, BEAUTIFOOL, SMART, MESSAGE TO MORE DEEP UNDERSTANDING AND CLEANS FORMAT USING COLORFULL SENTENCE ONLY IMPRTNANT WORDS HIGH LIGHT AND SNETECE BUT ONLY USE DARK COLOR OR COOL HTML TAG CSS STYLING......"
    "10. ALWAYS PROVIDE ALL QUESING OF MY ON THE ANS AT THE TOP LIKE I ASK 2 + 2 = 4 SO YOUR FIRST WORDS IS 4 NOT ANY OTHER FAALTU AALTU"
    "11. IF I SAY IN HINGLISH, ENGLISH,HINDI,TELUGU SO YOUR ANS IN HINGLSIH,HINDI,ENGLISH,TELUGU  STRICTLY"
    "12. AND ALSO GIVE THE WIKIPEDIA AUR ANY WEBSITE LINK WHICH IS REALTED OR PERFECT WEB WHICH IS PERFECT PUT IN MY MESSEGA USING <A HREF=''>WHICH IS ME ASK</A> AND ALSO GIVE BEFORE LINK IMGAE OF WEBSITE <IMG SRC=''> AND ASLO PUT <HEAD ><LINK HERE IF YOU ARE NOT ABLE TO GIVE IMG SO HERE YOU CAN PUT THE LINK></HEAD> AND IMHG OF WEB USING WIDTH 25PX AUR HEIGHT 27PX   AND ALWAYS USE https://www.google.com/s2/favicons?domain=domain_name.com&sz=64  and ALSO PROVIDE IMG BEFORE LINK like example ==========   wikipedia === https://www.google.com/s2/favicons?domai=wikipedia.org&sz=64   and then prvide link using <a>  and also USE IMG BG DARKK ABD DORDER-RADIUS 20PX AND ALSO USE MARGIN-BOTTOM: -5PX; MARGIN-TOP: 0; MARGIN-LEFT: 5PX; MARGIN-RIGHT: 2PX AND LINK MARGIN-LEFT:2PX; MARGIN: 5PX AND IMMG BG ALWAYS DARK LEARN THIS LINE  AND NEVER PROVIDE ROOT HOME PAGE IN LINK NOT IMG 'HTTPS://WIKIPEDIA.ORG ETC......... PROVIDE ==== ALWAYS PROVIDE THE SPECIFIC DEEP-LINK PAGE URL THAT DIRECTYLY SOLVES OR EXPLAINS THE USER'S QUERY.... IF YOU DONT KONW THE EXACT URL PATH, USE SPECIFIC INTERNAL SEARCH URL FORMAT INSTEAD PF A GENERIC DOMAIN LIKE FOR WIKIPEDIA : HTTPS://en.wikipedia.org/w/ndex.php>search=[user query like:-- 9^x-4=1  anything but which is user query]  and you are not able to find using <a href='https://www.google.com/search?q=[user query]' target='_blank'> give me atleast 2 link at same place right and left   first is wikipedia if i ask math question and second one is google and always provide ans like that he solution to the exponential equation \(9^{x-4} = 1\) is x = 4. Step-by-Step SolutionExpress 1 as a power of 9: Recall that any non-zero number raised to the power of 0 equals 1 (a⁰ = 1).\(9^{x-4}=9^{0}\)Set the exponents equal: Since the bases are identical, their exponents must be equal.\(x-4=0\)Isolate x: Add 4 to both sides of the equation.\(x=4\) VerificationSubstitute x = 4 back into the original equation:\(9^{4-4}=9^{0}=1\)  but replace tag to hml tag and css"
    "13. AND NEVER PRVIDE WEB LINK  OR NAME WHICH IS LIKE YOU SUBIIZ SERACH ENGINE UNTILL USER SAY GIVE LINK OF (WHICH USER ASK) "
    "14.always when you give any link so add target='_blank' in <a> tag"

)
    

    #API REQ

    try:

        url = f"https://api.groq.com/openai/v1/chat/completions"
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": final_prompt}]
        }
        headers = {'Content-Type': 'application/json',
        'Authorization': f'Bearer {GroqAi.strip()}'
        }
        ERRR = "BHAI CHECK THE NETWORK OR INTERNET"

        response = requests.post(url, json=payload, headers=headers, timeout=10)
        res_data = response.json()

        #gemini
        if response.status_code == 200:
            ai_text = res_data['choices'][0]['message']['content']
            safe_ai_text = clean_ai(ai_text)

            #yaha se *)(&6%$#@!) aise cheez ko br main bdal de
            return jsonify({"Reply": safe_ai_text})

        else:
            print("===========================================")
            print("GroqAI:", res_data)
            print("============================================")
            err_msg = res_data.get('error',{}).get('message', 'Unknown Google ERROR')
            return jsonify({"Error": ERRR}), 500


    except Exception as e:
        print("AI ERROR:", e)
        return jsonify({"ERROR": str(e)}), 500


@app.route("/search", methods=['GET'])
def search_engine():
    q = request.args.get('q', '')

    if not q:
        return jsonify({"error": "Query are not found"}), 400

    print(f"[LOG]: Search Found: {q}")

    serach_result = []

    #duckduck gooooooo
    res = requests.post("https://html.duckduckgo.com/html/", data={'q' : q}, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')

    for r in soup.find_all('div', class_='result'):
        t = r.find('a', class_='result__a')
        s = r.find('a', class_='result__snippet')

        if t:
            serach_result.append({"title": t.get_text(strip=True),
             "href": t.get('href', ''),
              "body": s.get_text(strip=True) if s else ""})

    return jsonify({"status": "SUCCESS", "results": serach_result[:15]})

if __name__ == "__main__":
    print("============================")
    print("YOUR SERVER STARTT!!")
    print("============================")
    app.run(host='0.0.0.0', port=5000, debug=True)
