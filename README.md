# 🔒 Ransomware Attack Simulation Dashboard

An educational cybersecurity project that simulates a ransomware attack progression through multiple stages with real-time monitoring and visualization.

## 📋 Overview

This interactive dashboard demonstrates how ransomware attacks evolve from initial access to ransom demand, helping students and cybersecurity professionals understand attack patterns and defense strategies.

## 🎯 Features

- **Real-time Attack Simulation**: Watch as the attack progresses through 5 distinct stages
- **Live Metrics Dashboard**: Track encrypted files, affected systems, and elapsed time
- **Attack Timeline**: Detailed logs showing each step of the attack
- **Visual Progress Indicators**: Color-coded stages for easy monitoring
- **Educational Content**: Learn about ransomware prevention and mitigation

## 🚀 Attack Stages

1. **Dormant** - System is safe, waiting for attack
2. **Initial Access** - Phishing attack and malicious payload delivery
3. **Lateral Movement** - Network scanning and privilege escalation
4. **Data Encryption** - Files and databases get encrypted
5. **Ransom Demand** - Attacker demands payment

## 💻 Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **HTML/CSS** - Custom styling

## 📦 Installation

### Local Setup

1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/ransomware-simulation.git
cd ransomware-simulation
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and go to `http://localhost:8501`

## 🌐 Live Demo

🔗 **[View Live Demo](https://your-app-url.streamlit.app)** *(Add your Streamlit URL here after deployment)*

## 🎮 How to Use

1. Click the **"Start Simulation"** button
2. Watch the attack progress through different stages
3. Observe the metrics updating in real-time
4. View detailed logs in the timeline section
5. Click **"Reset"** to run the simulation again

## 📊 Metrics Tracked

- **Files Encrypted**: Number of files compromised
- **Systems Affected**: Number of systems infected
- **Time Elapsed**: Duration of the attack
- **Current Stage**: Active attack phase

## ⚠️ Educational Purpose

**IMPORTANT**: This is a simulation for educational purposes only. It demonstrates:
- How ransomware attacks progress
- The importance of cybersecurity measures
- Why prevention is critical

## 🛡️ Security Best Practices

Organizations should implement:
- Regular data backups
- Employee cybersecurity training
- Network segmentation
- Incident response plans
- Up-to-date antivirus software
- Multi-factor authentication

## 📝 Project Structure
```
ransomware-simulation/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🤝 Contributing

This is an educational project. Feel free to fork and modify for your learning purposes.

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

Created as a cybersecurity educational project for demonstrating ransomware attack patterns.

## 📧 Contact

For questions or feedback about this project, please open an issue in the repository.

---

**⚠️ Disclaimer**: This simulation is for educational purposes only. Do not use this knowledge for malicious activities. Always practice ethical cybersecurity.
```

---

## **HOW TO ADD THESE FILES TO GITHUB:**

### **Method 1: Create Files Directly on GitHub (Easiest)**

**For requirements.txt:**
1. Go to your repository
2. Click **"Add file"** → **"Create new file"**
3. Name it: `requirements.txt`
4. Copy and paste: `streamlit`
5. Click **"Commit new file"**

**For README.md:**
1. Click **"Add file"** → **"Create new file"**
2. Name it: `README.md`
3. Copy and paste the entire markdown content above
4. Click **"Commit new file"**

---

### **Method 2: Create Files on Your Computer First**

**Step 1: Create requirements.txt**
1. Open Notepad
2. Type: `streamlit`
3. Save as: `requirements.txt` (not .txt.txt!)
   - In Notepad, choose "Save as type" → "All Files"
   - Name: `requirements.txt`

**Step 2: Create README.md**
1. Open Notepad
2. Copy and paste the README content above
3. Save as: `README.md`
   - Choose "Save as type" → "All Files"
   - Name: `README.md`

**Step 3: Upload to GitHub**
1. Go to your repository
2. Click **"Add file"** → **"Upload files"**
3. Drag both files
4. Click **"Commit changes"**

---

## **WHAT EACH FILE DOES:**

### **requirements.txt**
- Tells Streamlit Cloud what Python libraries to install
- Very simple - just lists `streamlit`

### **README.md**
- This is the "homepage" of your GitHub repository
- Shows project description, features, and instructions
- Makes your project look professional
- Helps others understand what your project does
- `.md` stands for Markdown (a simple formatting language)

---

## **AFTER ADDING THESE FILES:**

Your repository should look like this:
```
📁 ransomware-simulation/
   ├── 📄 app.py                (your main code)
   ├── 📄 requirements.txt      (dependencies)
   └── 📄 README.md            (documentation)