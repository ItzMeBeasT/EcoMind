"""
Layout components for EcoMind AI dashboard matching exact reference image design.
Top utility header bar, hero banner graphic, synthetic notice banner, sidebar watermark card, and bottom SDG 7 banner.
"""

import streamlit as st

def render_top_utility_bar(dataset_status: str = "Synthetic Demo Dataset", ai_status: str = "AI Online"):
    """
    Render top utility header bar matching reference image layout.
    """
    st.markdown("""
    <div class="utility-header-bar">
        <div class="search-placeholder">
            <span>🔍</span>
            <span>Search insights, buildings, or ask EcoMind...</span>
        </div>
        <div class="header-controls">
            <div style="background:#FFFFFF; border:1px solid #E2E8F0; padding:0.4rem 0.85rem; border-radius:8px; font-size:0.82rem; color:#475569; display:flex; align-items:center; gap:0.4rem;">
                <span>📅</span>
                <span>Jan 01, 2026 – Mar 31, 2026</span>
                <span style="font-size:0.7rem; color:#94A3B8;">▼</span>
            </div>
            <span class="badge-pill badge-success" style="display:flex; align-items:center; gap:0.3rem;">
                <span style="font-size:0.6rem; color:#10B981;">●</span> AI Online
            </span>
            <div style="width:32px; height:32px; background-color:#334155; color:#FFFFFF; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.85rem;">
                R
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_hero_header():
    """
    Render hero banner matching exact reference image layout and graphic illustration.
    """
    st.markdown("""
    <div class="hero-banner">
        <div style="max-width: 680px;">
            <p class="hero-eyebrow">CAMPUS ENERGY INTELLIGENCE</p>
            <h1 class="hero-title">Campus Energy Overview</h1>
            <p class="hero-description">
                Understand consumption patterns, detect anomalies, and identify opportunities to reduce energy waste with the power of AI.
            </p>
        </div>
        <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end;">
            <svg width="220" height="90" viewBox="0 0 220 90" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Sun -->
                <circle cx="165" cy="25" r="14" fill="#FDE047" opacity="0.9"/>
                <!-- Hills -->
                <path d="M70 75C100 55 140 55 170 75" stroke="#86EFAC" stroke-width="20" stroke-linecap="round"/>
                <path d="M110 75C140 50 180 50 210 75" stroke="#BBF7D0" stroke-width="16" stroke-linecap="round"/>
                <!-- Modern Campus Buildings -->
                <rect x="85" y="45" width="22" height="30" rx="2" fill="#38BDF8" opacity="0.8"/>
                <rect x="112" y="35" width="28" height="40" rx="2" fill="#4F8F72"/>
                <rect x="145" y="40" width="24" height="35" rx="2" fill="#285943"/>
                <!-- Trees -->
                <circle cx="78" cy="65" r="8" fill="#22C55E"/>
                <circle cx="174" cy="62" r="9" fill="#16A34A"/>
                <circle cx="190" cy="66" r="7" fill="#4ADE80"/>
            </svg>
            <div style="font-family: 'Caveat', cursive, sans-serif; font-size: 1.1rem; color: #4F8F72; font-weight: 600; margin-top: -5px; transform: rotate(-3deg);">
                Sustainable Campuses Brighter Futures.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_synthetic_notice():
    """
    Render notice banner matching exact reference image layout.
    """
    st.markdown("""
    <div class="notice-banner">
        <div style="display:flex; align-items:center; gap:0.6rem;">
            <span style="font-size:1.1rem; color:#3B82F6;">ℹ️</span>
            <div>
                <b>Synthetic Data Notice</b><br>
                <span style="font-size:0.8rem; color:#475569;">This prototype uses synthetic campus energy data for demonstration and evaluation (1M1B Internship / IBM SkillsBuild & AICTE). All values are estimates.</span>
            </div>
        </div>
        <div style="background:#FFFFFF; border:1px solid #93C5FD; color:#1E40AF; padding:0.35rem 0.75rem; border-radius:6px; font-weight:600; font-size:0.78rem;">
            Demo Mode
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar_card_and_footer():
    """
    Render sidebar leafy watermark card and bottom branding logo.
    """
    st.markdown("""
    <div class="sidebar-leafy-card">
        <div style="font-size: 0.95rem; font-weight: 700; color: #285943; line-height: 1.3; margin-bottom: 1.5rem;">
            A Greener<br>Tomorrow<br>Starts with<br>Smarter Decisions.
        </div>
        <div style="width: 40%; height: 5px; background-color: #4F8F72; border-radius: 999px;"></div>
    </div>

    <div style="display:flex; align-items:center; gap:0.5rem; margin-top:1.5rem; font-size:0.82rem;">
        <div style="width:20px; height:20px; background-color:#DDEFE5; color:#285943; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.75rem;">✓</div>
        <div>
            <div style="font-weight:700; color:#24312B;">EcoMind AI</div>
            <div style="font-size:0.72rem; color:#64748B;">AI for a Sustainable Campus</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sdg_footer():
    """
    Render bottom SDG 7 sustainability banner matching exact reference screenshot.
    """
    st.markdown("""
    <div style="margin-top: 2rem; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 1rem 1.25rem; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="width: 42px; height: 42px; background-color: #DDEFE5; color: #285943; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">
                🌱
            </div>
            <div>
                <div style="font-weight: 700; font-size: 0.95rem; color: #285943;">Reducing Energy. Enabling Change.</div>
                <div style="font-size: 0.82rem; color: #64748B;">EcoMind AI supports SDG 7 (Affordable and Clean Energy) through data-driven insights and responsible AI.</div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="text-align: right; font-size: 0.78rem; color: #64748B;">
                <b style="color: #D97706;">SDG 7</b><br>
                Affordable and<br>Clean Energy
            </div>
            <div style="font-size: 1.6rem; color: #F59E0B;">☀️</div>
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; color: #334155; padding: 0.45rem 0.85rem; border-radius: 8px; font-weight: 600; font-size: 0.82rem;">
                Learn More
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
