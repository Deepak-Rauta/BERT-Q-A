BERT Question Answering App 🤖
This is a simple Question Answering (Q&A) app built using Hugging Face Transformers and Streamlit. It uses the DistilBERT model to answer questions based on a given text.

🚀 Features
Accepts context and question as input.
Uses DistilBERT to generate an answer.
Runs on Streamlit with a simple UI.

📌 Installation
1️⃣ Clone the Repository
git clone https://github.com/Deepak-Rauta/BERT-Q-A.git
cd BERT-Q-A

2️⃣ Create a Virtual Environment (Optional but Recommended)
For Linux/macOS:
python3 -m venv venv
source venv/bin/activate

For Windows:
python -m venv venv
venv\Scripts\activate

3️⃣ Install Required Packages
pip install -r requirementrs.txt

(If you don’t have requirements.txt, install manually using:)
pip install streamlit transformers torch

🎯 Run the App
streamlit run app.py or python -m streamlit run app.py

📜 How It Works?
1.Enter a context (a passage of text).
2. Enter a question related to the context.
3. Click the "Get Answer" button.
4. The app will use DistilBERT to generate the answer.

📝 Example Usage
Context:
"Apple Inc. is an American multinational technology company headquartered in Cupertino, California. It designs, develops, and sells consumer electronics, computer software, and online services. The company's best-known products include the iPhone, iPad, Mac computers, Apple Watch, and Apple TV. Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976."

Question:
"Who founded Apple Inc?"

Output Answer:
"Steve Jobs, Steve Wozniak, and Ronald Wayne."
