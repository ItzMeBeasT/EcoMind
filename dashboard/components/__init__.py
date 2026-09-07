"""
Design tokens and custom CSS styling rules for EcoMind AI.
Strict contrast safeguards, typography rules, and responsive SaaS layout bounds.
"""

import streamlit as st

# Color Palette Tokens
COLOR_BG = "#F7F9F7"
COLOR_SURFACE = "#FFFFFF"
COLOR_PRIMARY = "#4F8F72"
COLOR_PRIMARY_DARK = "#285943"
COLOR_SOFT_GREEN = "#DDEFE5"
COLOR_SOFT_BLUE = "#DCEAF4"
COLOR_SOFT_YELLOW = "#F7EBC8"
COLOR_SOFT_CORAL = "#F4D9D2"
COLOR_TEXT_MAIN = "#24312B"
COLOR_TEXT_MUTED = "#68736D"
COLOR_TEXT_LIGHT = "#8A948E"
COLOR_BORDER = "#E3E9E5"

def inject_global_styles():
    """
    Inject custom CSS rules to enforce light SaaS theme, typography, crisp contrast, and centered max-width bounds.
    """
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* App Background & Typography */
        html, body, [class*="css"], div[data-testid="stAppViewContainer"] {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: {COLOR_BG} !important;
            color: {COLOR_TEXT_MAIN} !important;
        }}

        /* Centered Fixed-Width Content Bounds */
        .block-container {{
            max-width: 1200px !important;
            padding-top: 1.25rem !important;
            padding-bottom: 3.5rem !important;
            margin: 0 auto !important;
        }}

        /* Streamlit Top Header Styling */
        header[data-testid="stHeader"] {{
            background-color: {COLOR_BG} !important;
        }}

        /* Sidebar Container Styling */
        section[data-testid="stSidebar"] {{
            background-color: #FFFFFF !important;
            border-right: 1px solid {COLOR_BORDER} !important;
            padding-top: 1rem !important;
        }}

        /* High-Contrast Sidebar Section Titles */
        .sidebar-nav-header {{
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: {COLOR_PRIMARY};
            text-transform: uppercase;
            margin-top: 1.25rem;
            margin-bottom: 0.35rem;
            padding-left: 0.5rem;
        }}

        /* Radio Buttons in Sidebar (Fixing contrast and selection) */
        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
            background-color: transparent !important;
            color: {COLOR_TEXT_MAIN} !important;
            font-weight: 500 !important;
            font-size: 0.88rem !important;
            padding: 0.5rem 0.75rem !important;
            border-radius: 8px !important;
            margin-bottom: 3px !important;
            transition: all 0.15s ease-in-out !important;
            cursor: pointer !important;
            border: 1px solid transparent !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
            background-color: {COLOR_BG} !important;
            color: {COLOR_PRIMARY_DARK} !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label[aria-checked="true"] {{
            background-color: {COLOR_SOFT_GREEN} !important;
            color: {COLOR_PRIMARY_DARK} !important;
            font-weight: 700 !important;
            border: 1px solid #C2E2D2 !important;
        }}

        /* Ensure Radio text remains crisp & readable */
        section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
            color: {COLOR_TEXT_MAIN} !important;
            font-size: 0.88rem !important;
            font-weight: 600 !important;
            margin: 0 !important;
        }}
        section[data-testid="stSidebar"] div[role="radiogroup"] label[aria-checked="true"] p {{
            color: {COLOR_PRIMARY_DARK} !important;
        }}

        /* SaaS Top Utility Header Bar */
        .utility-header-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #FFFFFF;
            padding: 0.75rem 1.25rem;
            border-radius: 10px;
            border: 1px solid {COLOR_BORDER};
            margin-bottom: 1.25rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}
        .search-placeholder {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background-color: {COLOR_BG};
            border: 1px solid {COLOR_BORDER};
            padding: 0.4rem 0.85rem;
            border-radius: 6px;
            font-size: 0.82rem;
            color: {COLOR_TEXT_MUTED};
            width: 320px;
        }}
        .header-badges {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        /* Hero / Page Banner Styling */
        .hero-eyebrow {{
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            color: {COLOR_PRIMARY_DARK};
            text-transform: uppercase;
            margin-bottom: 0.25rem;
        }}
        .hero-title {{
            font-size: 1.85rem;
            font-weight: 700;
            color: {COLOR_TEXT_MAIN};
            margin-bottom: 0.35rem;
            line-height: 1.2;
        }}
        .hero-description {{
            font-size: 0.94rem;
            color: {COLOR_TEXT_MUTED};
            margin-bottom: 1.25rem;
            max-width: 850px;
            line-height: 1.5;
        }}

        /* Synthetic Data Notice Banner */
        .synthetic-notice-box {{
            background-color: #FAFAF9;
            border: 1px solid {COLOR_BORDER};
            border-left: 3px solid {COLOR_PRIMARY};
            border-radius: 6px;
            padding: 0.55rem 0.85rem;
            font-size: 0.82rem;
            color: {COLOR_TEXT_MUTED};
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        /* Metric / KPI Card Styling */
        .kpi-card {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 10px;
            padding: 1.1rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
            height: 100%;
        }}
        .kpi-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.4rem;
        }}
        .kpi-card-title {{
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            color: {COLOR_TEXT_MUTED};
            text-transform: uppercase;
        }}
        .kpi-card-value {{
            font-size: 1.65rem;
            font-weight: 700;
            color: {COLOR_TEXT_MAIN};
            line-height: 1.1;
            margin-bottom: 0.3rem;
        }}
        .kpi-card-sub {{
            font-size: 0.78rem;
            color: {COLOR_TEXT_MUTED};
        }}

        /* Executive AI Insight Card */
        .ai-insight-box {{
            background-color: #F0F7F4;
            border: 1px solid #C2E2D2;
            border-radius: 10px;
            padding: 1.25rem;
            margin-bottom: 1.5rem;
        }}
        .ai-insight-head {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
            font-weight: 700;
            color: {COLOR_PRIMARY_DARK};
            margin-bottom: 0.5rem;
        }}
        .ai-insight-text {{
            font-size: 0.92rem;
            color: {COLOR_TEXT_MAIN};
            line-height: 1.5;
            margin-bottom: 0.5rem;
        }}
        .ai-insight-action {{
            font-size: 0.86rem;
            font-weight: 600;
            color: {COLOR_PRIMARY_DARK};
            background-color: #FFFFFF;
            border: 1px solid #C2E2D2;
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            display: inline-block;
        }}

        /* Custom SaaS Card Container */
        .saas-container {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 10px;
            padding: 1.25rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}
        .saas-container-title {{
            font-weight: 700;
            font-size: 1rem;
            color: {COLOR_TEXT_MAIN};
            margin-bottom: 0.85rem;
        }}

        /* Badges & Pills */
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

        /* Sidebar Footer Message */
        .sidebar-footer {{
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid {COLOR_BORDER};
            font-size: 0.75rem;
            color: {COLOR_TEXT_MUTED};
            line-height: 1.4;
            font-style: italic;
        }}

        /* Custom Button Tweaks */
        .stButton>button {{
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            border: 1px solid {COLOR_BORDER} !important;
            background-color: #FFFFFF !important;
            color: {COLOR_TEXT_MAIN} !important;
            transition: all 0.15s ease !important;
        }}
        .stButton>button:hover {{
            background-color: {COLOR_SOFT_GREEN} !important;
            color: {COLOR_PRIMARY_DARK} !important;
            border-color: {COLOR_PRIMARY} !important;
        }}
    </style>
    """, unsafe_allow_html=True)
