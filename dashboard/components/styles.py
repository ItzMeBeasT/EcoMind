"""
Design tokens, CSS variables, and layout styles for EcoMind AI dashboard.
Replicates the visual reference palette, card structures, hero illustrations, typography, and contrast rules.
"""

import streamlit as st

# Color Palette Tokens
COLOR_BG = "#F4F7F5"
COLOR_SURFACE = "#FFFFFF"
COLOR_PRIMARY = "#4F8F72"
COLOR_PRIMARY_DARK = "#285943"
COLOR_SOFT_GREEN = "#E6F4ED"
COLOR_SOFT_BLUE = "#EBF3FA"
COLOR_SOFT_YELLOW = "#FDF6E2"
COLOR_SOFT_CORAL = "#FCEAE6"
COLOR_TEXT_MAIN = "#1E293B"
COLOR_TEXT_MUTED = "#64748B"
COLOR_TEXT_LIGHT = "#94A3B8"
COLOR_BORDER = "#E2E8F0"

def inject_global_styles():
    """
    Inject custom CSS rules to enforce light SaaS theme, typography, crisp contrast, and centered max-width bounds.
    """
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Caveat:wght@600&display=swap');

        /* App Background & Typography */
        html, body, [class*="css"], div[data-testid="stAppViewContainer"] {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: {COLOR_BG} !important;
            color: {COLOR_TEXT_MAIN} !important;
        }}

        /* Centered Fixed-Width Content Bounds */
        .block-container {{
            max-width: 1240px !important;
            padding-top: 1rem !important;
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
            padding-top: 1.25rem !important;
        }}

        /* High-Contrast Sidebar Section Titles */
        .sidebar-nav-header {{
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: #94A3B8;
            text-transform: uppercase;
            margin-top: 1.25rem;
            margin-bottom: 0.35rem;
            padding-left: 0.5rem;
        }}

        /* Radio Buttons in Sidebar */
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

        section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
            color: {COLOR_TEXT_MAIN} !important;
            font-size: 0.88rem !important;
            font-weight: 600 !important;
            margin: 0 !important;
        }}
        section[data-testid="stSidebar"] div[role="radiogroup"] label[aria-checked="true"] p {{
            color: {COLOR_PRIMARY_DARK} !important;
        }}

        /* Top Utility Header Bar */
        .utility-header-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #FFFFFF;
            padding: 0.6rem 1rem;
            border-radius: 12px;
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
            padding: 0.45rem 0.85rem;
            border-radius: 8px;
            font-size: 0.84rem;
            color: {COLOR_TEXT_MUTED};
            width: 360px;
        }}
        .header-controls {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        /* Hero Banner */
        .hero-banner {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(135deg, #FFFFFF 0%, #F8FAF9 100%);
            border: 1px solid {COLOR_BORDER};
            border-radius: 14px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 1.25rem;
            position: relative;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }}

        /* Synthetic Data Notice Banner */
        .notice-banner {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #EFF6FF;
            border: 1px solid #BFDBFE;
            border-radius: 10px;
            padding: 0.6rem 1rem;
            margin-bottom: 1.25rem;
            font-size: 0.84rem;
            color: #1E40AF;
        }}

        /* Top 4 Metric Cards */
        .kpi-metric-card {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 12px;
            padding: 1.1rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .kpi-icon-box {{
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
        }}
        .kpi-val-text {{
            font-size: 1.65rem;
            font-weight: 800;
            color: {COLOR_TEXT_MAIN};
            line-height: 1.1;
            margin: 0.3rem 0 0.2rem 0;
        }}

        /* Executive AI Insight Banner */
        .ai-insight-banner {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 14px;
            padding: 1.35rem 1.5rem;
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}

        /* Custom SaaS Card Container */
        .saas-card-box {{
            background-color: #FFFFFF;
            border: 1px solid {COLOR_BORDER};
            border-radius: 14px;
            padding: 1.25rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}

        /* Badges & Pills */
        .badge-pill {{
            display: inline-block;
            padding: 0.25rem 0.65rem;
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

        /* Sidebar Bottom Watermark Card */
        .sidebar-leafy-card {{
            background: linear-gradient(180deg, #EDF7F2 0%, #E2F2E9 100%);
            border: 1px solid #CBE5D8;
            border-radius: 12px;
            padding: 1rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            position: relative;
        }}

        /* Custom Streamlit Buttons override */
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
