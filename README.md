# Instagram Unfollow Automation Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Working-brightgreen.svg)

Automated tool to unfollow users on Instagram using unofficial API.

## ⚠️ Important Warning
**DISCLAIMER**: This project is for educational purposes only. Automation on Instagram may violate Terms of Service and could result in temporary or permanent account restrictions. Use at your own risk.

## 📋 Features
- Batch unfollow users
- Configurable delay between actions
- Automatic retry on failures
- Progress tracking
- Session persistence

## 🛠️ Requirements
- Python 3.8+
- Active Instagram account
- Required Python packages

## ⚙️ Setup
1. Clone the repository:
```bash
git clone https://github.com/vinicezariodev/instagram-unfollow-tool.git
cd Instagram-Unfollow-Tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get your Instagram credentials:

    - Login to Instagram in your browser
    - Go to your user page
    - Open DevTools (F12) → Application → Cookies → instagram.com
    - Copy these cookies: sessionid, ds_user_id, and csrftoken

4. Configure the tool:
```python
# In main.py
SESSIONID = "your_sessionid_here"
DS_USER_ID = "your_ds_user_id"
CSRFTOKEN = "your_csrftoken"
```

## 🚀 Usage

Run the tool with default settings:
```bash
python main.py
```

## 🔧 How It Works
1. Fetches list of accounts you follow

2. For each account:

    - Sends unfollow request
    - Waits random delay between actions
    - Handles errors and rate limits

3. Displays progress and statistics

## 📝 Notes

- Instagram frequently changes its API - this tool may stop working without notice

- The tool includes automatic retries for temporary failures

- For best results, run during normal activity hours
