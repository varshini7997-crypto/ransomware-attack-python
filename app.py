import streamlit as st
import time
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Ransomware Attack Simulation",
    page_icon="🔒",
    layout="wide"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
    }
    .stButton>button {
        background-color: #dc2626;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 30px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #b91c1c;
    }
    .metric-card {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #404040;
    }
    .log-entry {
        background-color: #2d2d2d;
        padding: 10px;
        margin: 5px 0;
        border-left: 4px solid #dc2626;
        border-radius: 5px;
        font-family: monospace;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    .warning-box {
        background-color: #1e3a8a;
        border: 2px solid #3b82f6;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'attack_stage' not in st.session_state:
    st.session_state.attack_stage = 0
    st.session_state.is_running = False
    st.session_state.files_encrypted = 0
    st.session_state.systems_affected = 0
    st.session_state.detection_time = 0
    st.session_state.logs = []
    st.session_state.start_time = None

# Attack stages
stages = [
    {"name": "Dormant", "color": "#6b7280"},
    {"name": "Initial Access", "color": "#eab308"},
    {"name": "Lateral Movement", "color": "#f97316"},
    {"name": "Data Encryption", "color": "#dc2626"},
    {"name": "Ransom Demand", "color": "#9333ea"}
]

# Attack timeline
attack_logs = [
    {"stage": 1, "message": "Phishing email opened by user", "time": 0},
    {"stage": 1, "message": "Malicious payload downloaded", "time": 2},
    {"stage": 1, "message": "Backdoor installed on system", "time": 4},
    {"stage": 2, "message": "Scanning network for vulnerabilities", "time": 6},
    {"stage": 2, "message": "Privilege escalation attempted", "time": 8},
    {"stage": 2, "message": "Admin credentials compromised", "time": 10},
    {"stage": 3, "message": "Beginning file encryption process", "time": 12},
    {"stage": 3, "message": "Documents folder encrypted", "time": 14},
    {"stage": 3, "message": "Database files encrypted", "time": 16},
    {"stage": 3, "message": "Backup systems targeted", "time": 18},
    {"stage": 4, "message": "Ransom note deployed", "time": 20},
    {"stage": 4, "message": "Payment deadline set: 48 hours", "time": 22}
]

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🔒 Ransomware Attack Simulation")
    st.markdown("**Educational Demo - Cybersecurity Training**")

with col2:
    if st.button("🚀 Start Simulation", disabled=st.session_state.is_running):
        st.session_state.is_running = True
        st.session_state.attack_stage = 0
        st.session_state.files_encrypted = 0
        st.session_state.systems_affected = 0
        st.session_state.detection_time = 0
        st.session_state.logs = []
        st.session_state.start_time = time.time()
        st.rerun()
    
    if st.button("🔄 Reset"):
        st.session_state.is_running = False
        st.session_state.attack_stage = 0
        st.session_state.files_encrypted = 0
        st.session_state.systems_affected = 0
        st.session_state.detection_time = 0
        st.session_state.logs = []
        st.session_state.start_time = None
        st.rerun()

st.markdown("---")

# Progress Bar
st.subheader("⚡ Attack Progress")
progress_cols = st.columns(5)
for idx, stage in enumerate(stages):
    with progress_cols[idx]:
        if idx <= st.session_state.attack_stage:
            st.markdown(f"""
            <div style='background-color: {stage["color"]}; height: 12px; 
            border-radius: 6px; margin-bottom: 10px;'></div>
            <p style='text-align: center; font-size: 12px; font-weight: bold;'>
            {stage["name"]}</p>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='background-color: #404040; height: 12px; 
            border-radius: 6px; margin-bottom: 10px;'></div>
            <p style='text-align: center; font-size: 12px; color: #6b7280;'>
            {stage["name"]}</p>
            """, unsafe_allow_html=True)

st.markdown("---")

# Metrics
st.subheader("📊 Real-Time Metrics")
metric_cols = st.columns(4)

with metric_cols[0]:
    st.markdown(f"""
    <div class='metric-card'>
        <h2 style='color: #dc2626; font-size: 36px; margin: 0;'>
        {st.session_state.files_encrypted}</h2>
        <p style='color: #9ca3af; margin: 5px 0 0 0;'>Files Encrypted</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[1]:
    st.markdown(f"""
    <div class='metric-card'>
        <h2 style='color: #f97316; font-size: 36px; margin: 0;'>
        {st.session_state.systems_affected}</h2>
        <p style='color: #9ca3af; margin: 5px 0 0 0;'>Systems Affected</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[2]:
    st.markdown(f"""
    <div class='metric-card'>
        <h2 style='color: #eab308; font-size: 36px; margin: 0;'>
        {st.session_state.detection_time}s</h2>
        <p style='color: #9ca3af; margin: 5px 0 0 0;'>Time Elapsed</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[3]:
    st.markdown(f"""
    <div class='metric-card'>
        <h2 style='color: #9333ea; font-size: 36px; margin: 0;'>
        {st.session_state.attack_stage}</h2>
        <p style='color: #9ca3af; margin: 5px 0 0 0;'>Current Stage</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Live Logs
st.subheader("📝 Attack Timeline & Logs")
log_container = st.container()

with log_container:
    if len(st.session_state.logs) == 0:
        st.info("⏳ Waiting for simulation to start...")
    else:
        for log in st.session_state.logs:
            st.markdown(f"""
            <div class='log-entry'>
                <span style='color: #dc2626;'>[{log['time']}s]</span>
                <span style='color: #eab308;'>[Stage {log['stage']}]</span>
                <span style='color: #d1d5db;'>{log['message']}</span>
            </div>
            """, unsafe_allow_html=True)

# Educational Note
st.markdown("""
<div class='warning-box'>
    <strong style='color: #93c5fd;'>⚠️ Educational Purpose:</strong>
    <p style='color: #bfdbfe; margin: 10px 0 0 0;'>
    This simulation demonstrates how ransomware attacks progress through different stages. 
    Real attacks involve malware encryption, data exfiltration, and ransom demands. 
    Organizations should implement proper cybersecurity measures including regular backups, 
    employee training, network segmentation, and incident response plans.
    </p>
</div>
""", unsafe_allow_html=True)

# Simulation Logic
if st.session_state.is_running:
    if st.session_state.start_time:
        elapsed = int(time.time() - st.session_state.start_time)
        st.session_state.detection_time = elapsed
        
        # Check for new logs
        for log in attack_logs:
            if log['time'] == elapsed and log not in st.session_state.logs:
                st.session_state.logs.insert(0, log)
                st.session_state.attack_stage = log['stage']
        
        # Update metrics
        if st.session_state.attack_stage >= 2:
            st.session_state.files_encrypted = min(
                st.session_state.files_encrypted + random.randint(50, 150), 
                5000
            )
            st.session_state.systems_affected = min(
                st.session_state.systems_affected + random.randint(1, 3), 
                50
            )
        
        # Stop simulation
        if elapsed >= 22:
            st.session_state.is_running = False
        
        # Auto-refresh every second
        time.sleep(1)
        st.rerun()