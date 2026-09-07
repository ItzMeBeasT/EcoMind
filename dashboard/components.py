"""
EcoMind AI — UI Component Library & Design System
Reusable UI components, CSS design tokens, cards, badges, and chart styling helpers for Streamlit.
"""

import streamlit as st

# Color Palette Definitions
COLOR_BG = "#F7F9F7"
COLOR_CARD = "#FFFFFF"
COLOR_PRIMARY = "#4F8F72"
COLOR_PRIMARY_DARK = "#285943"
COLOR_SOFT_GREEN = "#DDEFE5"
COLOR_SOFT_BLUE = "#DCEAF4"
COLOR_SOFT_YELLOW = "#F7EBC8"
COLOR_SOFT_CORAL = "#F4D9D2"
COLOR_TEXT_MAIN = "#24312B"
COLOR_TEXT_MUTED = "#6B756F"
COLOR_BORDER = "#E4E9E5"

def inject_custom_css():
    """
    Inject professional SaaS CSS design tokens into Streamlit.
    """
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        html, body, [class*="css"], div[data-testid="stAppViewContainer"] {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: {COLOR_BG};
            color: {COLOR_TEXT_MAIN};
        }}

        /* Main Container Padding */
        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }}

        /* Hide default Streamlit header bar decoration */
        header[data-testid="stHeader"] {{
            background-color: {COLOR_BG};
        }}

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {{
            background-color: #FFFFFF;
            border-right: 1px solid {COLOR_BORDER};
            padding-top: 1rem;
        }}

        /* Sidebar Radio Navigation Redesign */
        section[data-testid="stSidebar"] .stRadio label {{
            background-color: transparent;
            color: {COLOR_TEXT_MUTED};
            font-weight: 500;
            font-size: 0.9rem;
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            margin-bottom: 2px;
            transition: all 0.15s ease-in-out;
            cursor: pointer;
            width: 100%;
        }}

        section[data-testid="stSidebar"] .stRadio label:hover {{
            background-color: {COLOR_BG};
            color: {COLOR_TEXT_MAIN};
        }}

        /* Sidebar Section Header Label */
        .nav-category {{
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: #9CA3AF;
            text-transform: uppercase;
            margin-top: 1.25rem;
            margin-bottom: 0.4rem;
            padding-left: 0.5rem;
        }}

        /* Top Header Brand Bar */
        .brand-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #FFFFFF;
            padding: 0.85rem 1.25rem;
            border-radius: 10px;
            border: 1px solid {COLOR_BORDER};
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}
        .brand-left {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .brand-icon {{
            width: 32px;
            height: 32px;
            background-color: {COLOR_SOFT_GREEN};
            color: {COLOR_PRIMARY_DARK};
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.1rem;
        }}
        .brand-title {{
            font-weight: 700;
            font-size: 1.1rem;
            color: {COLOR_TEXT_MAIN};
            margin: 0;
            line-height: 1.2;
        }}
        .brand-subtitle {{
            font-size: 0.78rem;
            color: {COLOR_TEXT_MUTED};
            margin: 0;
        }}
        .brand-right {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        /* Page Headers */
        .page-eyebrow {{
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            color: {COLOR_PRIMARY_DARK};
            text-transform: uppercase;
            margin-bottom: 0.2rem;
        }}
        .page-title {{
            font-size: 1.75rem;
            font-weight: 700;
            color: {COLOR_TEXT_MAIN};
            margin-bottom: 0.35rem;
            line-height: 1.2;
        }}
        .page-description {{
            font-size: 0.92rem;
            color: {COLOR_TEXT_MUTED};
            margin-bottom: 1.25rem;
            max-width: 800px;
        }}

        /* Generic SaaS Card Container */
        .saas-card {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 10px;
            padding: 1.25rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
            transition: border-color 0.2s ease;
        }}
        .saas-card:hover {{
            border-color: #CBD5E1;
        }}

        /* Executive AI Insight Card */
        .ai-insight-card {{
            background-color: #F0F7F4;
            border: 1px solid #C2E2D2;
            border-radius: 10px;
            padding: 1.25rem;
            margin-bottom: 1.5rem;
            position: relative;
        }}
        .ai-insight-title {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.88rem;
            font-weight: 700;
            color: {COLOR_PRIMARY_DARK};
            margin-bottom: 0.5rem;
        }}
        .ai-insight-body {{
            font-size: 0.92rem;
            color: {COLOR_TEXT_MAIN};
            line-height: 1.5;
            margin-bottom: 0.5rem;
        }}

        /* Metric Cards */
        .kpi-card-box {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 10px;
            padding: 1.1rem;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
            height: 100%;
        }}
        .kpi-label {{
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: {COLOR_TEXT_MUTED};
            text-transform: uppercase;
            margin-bottom: 0.4rem;
        }}
        .kpi-val {{
            font-size: 1.6rem;
            font-weight: 700;
            color: {COLOR_TEXT_MAIN};
            line-height: 1.1;
            margin-bottom: 0.3rem;
        }}
        .kpi-sub {{
            font-size: 0.78rem;
            color: {COLOR_TEXT_MUTED};
        }}

        /* Badges */
        .badge-pill {{
            display: inline-block;
            padding: 0.2rem 0.6rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            line-height: 1;
        }}
        .badge-success {{ background-color: {COLOR_SOFT_GREEN}; color: {COLOR_PRIMARY_DARK}; }}
        .badge-info {{ background-color: {COLOR_SOFT_BLUE}; color: #1E40AF; }}
        .badge-warning {{ background-color: {COLOR_SOFT_YELLOW}; color: #92400E; }}
        .badge-danger {{ background-color: {COLOR_SOFT_CORAL}; color: #991B1B; }}
        .badge-neutral {{ background-color: #F1F5F9; color: #475569; }}

        /* Synthetic Data Info Banner */
        .demo-notice-banner {{
            background-color: #FAFAF9;
            border: 1px solid {COLOR_BORDER};
            border-left: 3px solid {COLOR_PRIMARY};
            border-radius: 6px;
            padding: 0.5rem 0.85rem;
            font-size: 0.82rem;
            color: {COLOR_TEXT_MUTED};
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        /* Recommendation Item Card */
        .rec-card-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }}
        .rec-card-title {{
            font-weight: 700;
            font-size: 1rem;
            color: {COLOR_TEXT_MAIN};
        }}
        .rec-card-meta {{
            font-size: 0.8rem;
            color: {COLOR_TEXT_MUTED};
            margin-bottom: 0.5rem;
        }}

        /* Chat UI styling */
        .chat-chip {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 20px;
            padding: 0.4rem 0.85rem;
            font-size: 0.82rem;
            color: {COLOR_TEXT_MAIN};
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .chat-chip:hover {{
            background-color: {COLOR_SOFT_GREEN};
            border-color: {COLOR_PRIMARY};
        }}

        /* Tabs styling customization */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 1.5rem;
            border-bottom: 1px solid {COLOR_BORDER};
        }}

        .stTabs [data-baseweb="tab"] {{
            font-size: 0.9rem;
            font-weight: 600;
            color: {COLOR_TEXT_MUTED};
            padding: 0.5rem 0;
            border-bottom-width: 2px;
        }}

        .stTabs [aria-selected="true"] {{
            color: {COLOR_PRIMARY_DARK} !important;
            border-bottom-color: {COLOR_PRIMARY} !important;
        }}
    </style>
    """, unsafe_allow_html=True)

def render_top_header(dataset_status: str = "Synthetic Demo Dataset", ai_status: str = "AI Engine Online"):
    """
    Render compact top application header bar.
    """
    st.markdown(f"""
    <div class="brand-bar">
        <div class="brand-left">
            <div class="brand-icon">🌿</div>
            <div>
                <p class="brand-title">EcoMind AI</p>
                <p class="brand-subtitle">Campus Energy Intelligence & Sustainability Agent</p>
            </div>
        </div>
        <div class="brand-right">
            <span class="badge-pill badge-neutral">📊 {dataset_status}</span>
            <span class="badge-pill badge-success">✨ {ai_status}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_page_header(title: str, subtitle: str = "", eyebrow: str = "CAMPUS ENERGY INTELLIGENCE"):
    """
    Render page title header with eyebrow tag and crisp typography.
    """
    st.markdown(f"""
    <div>
        <p class="page-eyebrow">{eyebrow}</p>
        <h1 class="page-title">{title}</h1>
        {f'<p class="page-description">{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)

def render_demo_notice_banner():
    """
    Render subtle, non-intrusive synthetic dataset disclosure banner.
    """
    st.markdown("""
    <div class="demo-notice-banner">
        <span>ℹ️</span>
        <span><b>Synthetic Data Notice:</b> This prototype uses synthetic campus energy data for demonstration and evaluation (1M1B Internship / IBM SkillsBuild & AICTE).</span>
    </div>
    """, unsafe_allow_html=True)

def render_metric_card(label: str, value: str, subtitle: str = "", icon: str = "📊"):
    """
    Render clean metric card component.
    """
    st.markdown(f"""
    <div class="kpi-card-box">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="kpi-label">{label}</span>
            <span style="font-size:1rem;">{icon}</span>
        </div>
        <div class="kpi-val">{value}</div>
        <div class="kpi-sub">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def render_executive_ai_insight(title: str, body: str, recommendation: str = ""):
    """
    Render executive AI insight banner.
    """
    st.markdown(f"""
    <div class="ai-insight-card">
        <div class="ai-insight-title">
            <span>✨</span>
            <span>{title}</span>
        </div>
        <div class="ai-insight-body">{body}</div>
        {f'<div style="font-size:0.85rem; font-weight:600; color:{COLOR_PRIMARY_DARK};">💡 Recommended Action: {recommendation}</div>' if recommendation else ''}
    </div>
    """, unsafe_allow_html=True)

def render_trust_card(title: str, description: str, icon: str = "🔒", list_items: list[str] = None):
    """
    Render Responsible AI Trust Center card.
    """
    items_html = ""
    if list_items:
        items_html = "<ul style='margin-top:0.5rem; margin-bottom:0; padding-left:1.2rem; font-size:0.85rem; color:#475569;'>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"

    st.markdown(f"""
    <div class="saas-card">
        <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;">
            <span style="font-size:1.2rem;">{icon}</span>
            <span style="font-weight:700; font-size:1rem; color:{COLOR_TEXT_MAIN};">{title}</span>
        </div>
        <div style="font-size:0.88rem; color:{COLOR_TEXT_MUTED}; line-height:1.4;">{description}</div>
        {items_html}
    </div>
    """, unsafe_allow_html=True)

def render_empty_state(title: str, description: str, icon: str = "🔍"):
    """
    Render clean empty state component.
    """
    st.markdown(f"""
    <div style="text-align:center; padding:2.5rem 1rem; background:#FFFFFF; border:1px dashed {COLOR_BORDER}; border-radius:10px;">
        <div style="font-size:2rem; margin-bottom:0.5rem;">{icon}</div>
        <div style="font-weight:700; font-size:1rem; color:{COLOR_TEXT_MAIN}; margin-bottom:0.25rem;">{title}</div>
        <div style="font-size:0.85rem; color:{COLOR_TEXT_MUTED}; max-width:400px; margin:0 auto;">{description}</div>
    </div>
    """, unsafe_allow_html=True)
