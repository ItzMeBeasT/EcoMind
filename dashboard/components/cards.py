"""
Card and container components for EcoMind AI dashboard matching exact reference design.
4 Top Metric Cards with sparklines, Executive AI Insight banner with quote, Building Share Progress bars,
Peak Usage badge, Occupancy Correlation badge, Quick Actions list, and Trust Center cards.
"""

import streamlit as st

def render_top_4_kpis(summary: dict, top_bld: dict, anom_count: int, anom_pct: float):
    """
    Render 4 top metric cards matching reference image layout and colors.
    """
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-metric-card">
            <div class="kpi-card-header">
                <span class="kpi-card-title">Total Consumption</span>
                <div class="kpi-icon-box" style="background-color:#E6F4ED; color:#285943;">⚡</div>
            </div>
            <div class="kpi-val-text">{summary['total_energy_kwh']:,.0f} kWh</div>
            <div style="font-size:0.78rem; color:#64748B; margin-bottom:0.5rem;">Across selected period</div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="badge-pill badge-success">↑ +12%</span>
                <svg width="70" height="22" viewBox="0 0 70 22" fill="none">
                    <path d="M2 18L15 14L28 16L42 8L55 12L68 3" stroke="#22C55E" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-metric-card">
            <div class="kpi-card-header">
                <span class="kpi-card-title">Average Hourly Load</span>
                <div class="kpi-icon-box" style="background-color:#EBF3FA; color:#1E40AF;">📊</div>
            </div>
            <div class="kpi-val-text">{summary['avg_energy_kwh']:.2f} kWh</div>
            <div style="font-size:0.78rem; color:#64748B; margin-bottom:0.5rem;">Typical hourly consumption</div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="badge-pill badge-info">↑ +5%</span>
                <svg width="70" height="22" viewBox="0 0 70 22" fill="none">
                    <path d="M2 16L15 18L28 12L42 14L55 6L68 4" stroke="#3B82F6" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-metric-card">
            <div class="kpi-card-header">
                <span class="kpi-card-title">Top Consumer</span>
                <div class="kpi-icon-box" style="background-color:#FDF6E2; color:#92400E;">🏢</div>
            </div>
            <div class="kpi-val-text">{top_bld['building']}</div>
            <div style="font-size:0.78rem; color:#64748B; margin-bottom:0.5rem;">{top_bld['share_percent']:.1f}% of total consumption</div>
            <div style="display:flex; justify-content:flex-end;">
                <svg width="60" height="20" viewBox="0 0 60 20" fill="none">
                    <rect x="2" y="10" width="8" height="10" rx="1" fill="#FDE047"/>
                    <rect x="14" y="6" width="8" height="14" rx="1" fill="#FACC15"/>
                    <rect x="26" y="12" width="8" height="8" rx="1" fill="#FDE047"/>
                    <rect x="38" y="2" width="8" height="18" rx="1" fill="#EAB308"/>
                    <rect x="50" y="8" width="8" height="12" rx="1" fill="#FACC15"/>
                </svg>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-metric-card">
            <div class="kpi-card-header">
                <span class="kpi-card-title">Anomalies Detected</span>
                <div class="kpi-icon-box" style="background-color:#FCEAE6; color:#991B1B;">⚠️</div>
            </div>
            <div class="kpi-val-text">{anom_count}</div>
            <div style="font-size:0.78rem; color:#64748B; margin-bottom:0.5rem;">{anom_pct:.1f}% rate in active subset</div>
            <div style="display:flex; justify-content:flex-end;">
                <svg width="70" height="22" viewBox="0 0 70 22" fill="none">
                    <path d="M2 14L15 15L28 10L42 18L55 5L68 12" stroke="#EF4444" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_executive_ai_insight(top_bld: dict):
    """
    Render EcoMind AI Insight Banner matching exact reference layout.
    """
    st.markdown(f"""
    <div class="ai-insight-banner">
        <div style="display:flex; gap:1.25rem; align-items:flex-start; flex:1;">
            <div style="width:48px; height:48px; min-width:48px; background-color:#E6F4ED; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.5rem; color:#285943;">
                💡
            </div>
            <div>
                <div style="font-weight:700; font-size:1.05rem; color:#285943; margin-bottom:0.4rem;">EcoMind Insight</div>
                <div style="font-size:0.92rem; color:#1E293B; line-height:1.5; margin-bottom:0.75rem;">
                    <b>{top_bld['building']}</b> accounts for <b>{top_bld['share_percent']:.1f}%</b> of total campus electricity usage with an average hourly consumption of <b>{top_bld['avg_energy_kwh']:.2f} kWh</b>.<br>
                    Multivariate analysis indicates elevated AC usage and device load during peak operational hours.
                </div>
            </div>
        </div>
        <div style="width:1px; height:70px; background-color:#E2E8F0; margin:0 0.5rem;"></div>
        <div style="max-width:240px; padding-left:0.5rem;">
            <div style="font-size:2rem; color:#CBD5E1; line-height:1; font-family:serif;">“</div>
            <div style="font-size:0.82rem; font-style:italic; color:#64748B; line-height:1.4; margin-top:-0.5rem;">
                Small changes today, a more sustainable campus tomorrow.
            </div>
            <div style="font-size:0.75rem; font-weight:700; color:#94A3B8; text-align:right; margin-top:0.3rem;">— EcoMind AI</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_energy_by_building_card(bld_stats):
    """
    Render Energy by Building card matching exact reference bar colors and shares.
    """
    st.markdown("""
    <div class="saas-card-box">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.15rem;">
            <div style="font-weight:700; font-size:1.05rem; color:#1E293B;">📊 Energy by Building</div>
        </div>
        <div style="font-size:0.8rem; color:#64748B; margin-bottom:1rem;">Total and average consumption</div>
    """, unsafe_allow_html=True)

    colors = ["#22C55E", "#3B82F6", "#F59E0B", "#EF4444"]
    
    for idx, row in bld_stats.iterrows():
        b_name = row["building"]
        b_kwh = row["total_energy_kwh"]
        b_share = row["share_percent"]
        bar_color = colors[idx % len(colors)]

        st.markdown(f"""
        <div style="margin-bottom:0.85rem;">
            <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.25rem;">
                <span style="font-weight:600; color:#1E293B;">{b_name}</span>
                <span><b style="color:#1E293B;">{b_kwh:,.0f} kWh</b> <span style="color:#64748B; font-size:0.8rem;">{b_share:.1f}%</span></span>
            </div>
            <div style="width:100%; height:12px; background-color:#F1F5F9; border-radius:999px; overflow:hidden;">
                <div style="width:{min(100, max(5, b_share))}%; height:100%; background-color:{bar_color}; border-radius:999px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
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
    <div class="saas-card-box">
        <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;">
            <span style="font-size:1.2rem;">{icon}</span>
            <span style="font-weight:700; font-size:1rem; color:#1E293B;">{title}</span>
        </div>
        <div style="font-size:0.88rem; color:#64748B; line-height:1.4;">{description}</div>
        {items_html}
    </div>
    """, unsafe_allow_html=True)

def render_empty_state(title: str, description: str, icon: str = "🔍"):
    """
    Render empty state placeholder.
    """
    st.markdown(f"""
    <div style="text-align:center; padding:2.5rem 1rem; background:#FFFFFF; border:1px dashed #E2E8F0; border-radius:12px;">
        <div style="font-size:2rem; margin-bottom:0.5rem;">{icon}</div>
        <div style="font-weight:700; font-size:1rem; color:#1E293B; margin-bottom:0.25rem;">{title}</div>
        <div style="font-size:0.85rem; color:#64748B; max-width:400px; margin:0 auto;">{description}</div>
    </div>
    """, unsafe_allow_html=True)
