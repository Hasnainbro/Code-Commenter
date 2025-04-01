# **Code Commenting Tool Using OpenRouter API**
An interactive web application that uses OpenRouter's AI to dynamically add, remove, and fix comments in Python code. This tool streamlines code understanding and debugging.

---

## 🚀 **Features**
- **Add Comments:** Generates beginner-friendly, detailed comments for your Python code.  
- **Remove Comments:** Removes all comments from your code, preserving the format and indentation.  
- **Fix Code:** Detects errors in your code and provides a corrected version.  
- **Responsive UI:** Intuitive, user-friendly interface with instant results.  
- **Copy Button:** Easily copy output code with a single click.  

---

## 🛠️ **Project Structure**
```
📂 code-commenting-tool
├── 📜 app.py                 # Flask backend with OpenRouter API integration
├── 📜 requirements.txt       # Python dependencies
├── 📜 .env                   # Environment variables (API key configuration)
├── 📜 README.md              # Project documentation
│
├── 📂 static                 # Static files for frontend
│   ├── 📜 styles.css         # Styling for the frontend
│
└── 📂 templates              # HTML templates for the frontend
    ├── 📜 index.html         # Main HTML page with input/output boxes

```
---

## 📜 **Prerequisites**
Ensure you have the following installed:
- Python 3.8 or higher
- Flask
- requests
- dotenv (for environment variable management)
- OpenRouter API key

---

## ⚙️ **Environment Setup**

### Step 1: Clone the Repository
```bash
git clone https://github.com/Hasnainbro/Code-Commenter.git
cd code-commenter
```

### Step 2: Create and Configure .env File

```bash
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
To Create your OpenRouter API key follow the steps:
- Go to [OpenRouter](https://openrouter.ai/) Website
- Create your account
- Hover on your profile
- Tap on Keys
- Tap Create Key Button, name your key
- Copy Your Key (Save key, as you wont be able to copy again after leaving the page)

### Step 3: Install Requirements 

```
pip install Flask requests python-dotenv
```

### Step 4 : Run the Program

```
Python app.py
```
