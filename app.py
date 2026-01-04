import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="The Silent Struggle",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- DESIGN SYSTEM & CSS INJECTION ---
# We inject "Digital Craftsmanship" design: Noise texture, Serif fonts, and broken grid.
def load_css():
    st.markdown("""
        <style>
        /* IMPORT FONTS */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

        /* RESET & BACKGROUND */
        .stApp {
            background-color: #0F0F11; /* Noise Void */
            color: #F4F1DE; /* Off-White Parchment */
            font-family: 'Inter', sans-serif;
        }

        /* HIDE DEFAULT STREAMLIT ELEMENTS */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* TYPOGRAPHY */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            font-weight: 400;
            color: #F4F1DE;
        }
        
        h1 {
            font-size: 4.5rem !important;
            line-height: 1.1;
            margin-bottom: 0.2em;
            letter-spacing: -0.02em;
        }
        
        .hero-subtext {
            font-family: 'Space Mono', monospace;
            color: #8D99AE; /* Muted Ash */
            text-transform: uppercase;
            letter-spacing: 0.15em;
            font-size: 0.8rem;
            margin-top: 1rem;
        }

        .highlight-text {
            color: #E07A5F; /* Electric Clay */
            font-style: italic;
        }

        /* CARDS & CONTAINERS - BROKEN GRID */
        .glass-card {
            background: rgba(26, 26, 28, 0.6); /* Frosted Graphite */
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 0px; /* Brutalist corners */
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .glass-card:hover {
            transform: translateY(-5px) scale(1.01);
            border-color: rgba(224, 122, 95, 0.3); /* Electric Clay hint */
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        }

        /* MATPLOTLIB/CHART OVERRIDES IN CSS (If SVG) */
        /* Note: Matplotlib renders as image, so we just style the container */
        
        /* SCROLLBAR */
        ::-webkit-scrollbar {
            width: 8px;
            background: #0F0F11;
        }
        ::-webkit-scrollbar-thumb {
            background: #2D2D30;
            border-radius: 4px;
        }

        </style>
    """, unsafe_allow_html=True)

load_css()

# --- DATA LOADING ---
@st.cache_data
def load_data():
    df = pd.read_csv("Mental Health Dataset.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset not found. Please ensure 'Mental Health Dataset.csv' is in the root directory.")
    st.stop()

# --- HERO SECTION (BROKEN GRID LAYOUT) ---
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("""
        <div style='margin-top: 4rem; margin-bottom: 4rem;'>
            <h1>The Silent <br> <span class='highlight-text'>Struggle.</span></h1>
            <p class='hero-subtext'>DATA SOURCE: 2014-2015 GLOBAL MENTAL HEALTH SURVEY • N=292,366</p>
            <p style='font-size: 1.2rem; margin-top: 2rem; max-width: 600px; line-height: 1.6; color: #D6D6D6;'>
                We often ask "Just wondering" or "How's work?", but rarely 
                "How does your mind feel today?". This is an exploration of the 
                invisible weight carried by professionals across the globe.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Intentionally empty or strictly for a "floaty" impact card later
    # This creates the "Whitespace" described in the vision.
    st.markdown("""
        <div class='glass-card' style='margin-top: 8rem;'>
            <h3 style='font-size: 1.5rem; margin-bottom: 1rem;'>Snapshot</h3>
            <div style='display: flex; justify-content: space-between; align-items: baseline;'>
                <span style='font-family: Space Mono; color: #8D99AE;'>GROWING STRESS</span>
                <span style='font-size: 3rem; font-family: Playfair Display; color: #E07A5F;'>
                    {:.1f}%
                </span>
            </div>
            <p style='font-size: 0.9rem; color: #8D99AE; margin-top: 0.5rem;'>
                of respondents reported noticeable increase in stress levels.
            </p>
        </div>
    """.format(len(df[df['Growing_Stress'] == 'Yes']) / len(df) * 100), unsafe_allow_html=True)

# --- VISUALIZATION FUNCTIONS ---

def setup_chart_style():
    """Configures Matplotlib to match the 'Digital Craftsmanship' aesthetic."""
    plt.style.use('dark_background')
    
    # Colors
    bg_color = '#1A1A1C' # Frosted Graphite match (or transparent)
    text_color = '#F4F1DE' # Off-White Parchment
    accent_color = '#D6D6D6' # Muted Grid

    plt.rcParams.update({
        'figure.facecolor': bg_color,
        'axes.facecolor': bg_color,
        'axes.edgecolor': bg_color, # Hide spines by making them same color
        'text.color': text_color,
        'axes.labelcolor': text_color,
        'xtick.color': text_color,
        'ytick.color': text_color,
        'font.family': 'monospace', # Fallback to monospace for nice tech feel
        # 'font.monospace': ['Space Mono', 'Consolas'], # Try to use system fonts if available
        'grid.color': accent_color,
        'grid.linestyle': ':',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.3,
    })

def plot_stress_gap(df):
    """
    Visualization 1: The Weight of Work.
    Horizontal Bar Chart comparing Growing Stress across Occupations.
    """
    setup_chart_style()
    
    # Data Prep
    # We want % of "Yes" for Growing_Stress per Occupation
    occ_stress = df[df['Growing_Stress'] == 'Yes']['Occupation'].value_counts()
    occ_total = df['Occupation'].value_counts()
    stress_ratio = (occ_stress / occ_total * 100).sort_values(ascending=True)
    
    # Filter for cleaner viz (optional, keeping all for now)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Background transparent for glass effect
    fig.patch.set_alpha(0.0) 
    ax.patch.set_alpha(0.0)
    
    # The Plot - Using "Electric Clay" (#E07A5F) for bars
    bars = ax.barh(stress_ratio.index, stress_ratio.values, color='#E07A5F', height=0.6)
    
    # "Digital Craftsmanship" Styling
    # 1. Remove Spines
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    # 2. No Axis Labels, just Data Labels
    ax.set_xticks([]) # Hide x-axis numbers
    ax.tick_params(axis='y', length=0, labelsize=12, pad=10) # Clean Y labels
    
    # 3. Direct Labeling (The "Architectural" Look)
    for bar in bars:
        width = bar.get_width()
        # Add value text end of bar
        ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                f'{width:.1f}%', 
                ha='left', va='center', 
                fontsize=11, fontfamily='monospace', color='#E07A5F', fontweight='bold')
        
    # Title (handled in H1/H2 in HTML, but here for context if exported)
    # ax.set_title("GROWING STRESS BY OCCUPATION", loc='left', fontsize=10, pad=20, color='#8D99AE')

    return fig

# --- THE "STREAM" (Main Content) ---

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True) # Spacer

# Section 1: Occupation vs Stress
st.markdown("## 01. The Weight of Work")

row1_col1, row1_col2 = st.columns([2, 1])

with row1_col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    fig_stress = plot_stress_gap(df)
    st.pyplot(fig_stress)
    st.markdown("</div>", unsafe_allow_html=True)


def plot_age_dist(df):
    """
    Visualization 2 (New): The Age of Anxiety.
    Violin Plot: Age Distribution by Growing Stress (Yes/No).
    """
    setup_chart_style()
    
    # Data Prep
    # Filter out NaNs if any
    df_clean = df.dropna(subset=['Age', 'Growing_Stress'])
    
    age_yes = df_clean[df_clean['Growing_Stress'] == 'Yes']['Age'].values
    age_no = df_clean[df_clean['Growing_Stress'] == 'No']['Age'].values
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    # Violin Plot
    # positions: 1 for Yes, 2 for No
    parts = ax.violinplot([age_yes, age_no], positions=[1, 2], showmeans=False, showmedians=True, showextrema=False)
    
    # Styling the Violins
    # Body
    for i, pc in enumerate(parts['bodies']):
        pc.set_facecolor('#E07A5F' if i == 0 else '#8D99AE')
        pc.set_edgecolor('#F4F1DE')
        pc.set_alpha(0.7)
    
    # Median Lines
    if 'cmedians' in parts:
        parts['cmedians'].set_color('#F4F1DE')
        parts['cmedians'].set_linewidth(1.5)

    # Custom styling
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Growing Stress:\nYES', 'Growing Stress:\nNO'], fontsize=12, fontfamily='monospace')
    ax.tick_params(axis='y', colors='#8D99AE', labelsize=10)
    ax.set_ylabel('Age', color='#8D99AE', fontfamily='monospace')

    # Add descriptive text/stats
    mean_yes = age_yes.mean()
    mean_no = age_no.mean()
    
    ax.text(1, 72, f'Mean: {mean_yes:.1f}y', ha='center', color='#E07A5F', fontsize=10, fontfamily='monospace')
    ax.text(2, 72, f'Mean: {mean_no:.1f}y', ha='center', color='#8D99AE', fontsize=10, fontfamily='monospace')
    
    return fig

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

# Section 02: The Age of Anxiety
st.markdown("## 02. The Age of Anxiety")
st.markdown("<p style='max-width: 600px; margin-bottom: 2rem; color: #8D99AE;'>Does age correlate with the perceived rise in stress?</p>", unsafe_allow_html=True)

col_age_text, col_age_plot = st.columns([1, 2])

with col_age_text:
     st.markdown("""
        <div class='glass-card' style='margin-top: 2rem;'>
            <h4 style='color: #F4F1DE; margin-bottom: 0.5rem; font-family: Playfair Display;'>Generational Weight.</h4>
            <p>
                Visualizing the age distribution reveals if stress is a burden of the young or the weary.
                <br><br>
                <span style='color: #E07A5F;'><b>Orange</b></span> indicates those reporting <b>Growing Stress</b>.
                <br>
                <span style='color: #8D99AE;'><b>Grey</b></span> indicates those who differ.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_age_plot:
    st.pyplot(plot_age_dist(df))


def plot_global_headspace(df):
    """
    Visualization 2: Global Headspace.
    Lollipop Chart: % of people with Mental Health History by Country.
    """
    setup_chart_style()
    
    # Data Prep
    # Filter countries with significant entries to avoid noise (e.g. > 20 respondents)
    country_counts = df['Country'].value_counts()
    significant_countries = country_counts[country_counts > 20].index
    
    df_sig = df[df['Country'].isin(significant_countries)]
    
    # % Yes for Mental_Health_History
    mh_history = df_sig[df_sig['Mental_Health_History'] == 'Yes']['Country'].value_counts()
    total_counts = df_sig['Country'].value_counts()
    
    mh_ratio = (mh_history / total_counts * 100).sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    # Lollipop Plot
    # 1. The Lines (Stems)
    ax.hlines(y=mh_ratio.index, xmin=0, xmax=mh_ratio.values, color='#8D99AE', alpha=0.4, linewidth=1)
    
    # 2. The Dots (Heads)
    # Using "Acid Sage" (#81B29A) for specific positive/neutral look or just distinct from the red
    ax.scatter(mh_ratio.values, mh_ratio.index, color='#81B29A', s=100, alpha=1, zorder=3)
    
    # Styling
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.set_xticks([])
    ax.tick_params(axis='y', length=0, labelsize=11, pad=15)
    
    # Annotate dots
    for i, (country, val) in enumerate(zip(mh_ratio.index, mh_ratio.values)):
        ax.text(val + 1.5, i, f'{val:.1f}%', va='center', fontsize=9, color='#81B29A', fontfamily='monospace')

    return fig

def plot_habit_loop(df):
    """
    Visualization 3: Habit Loop.
    Heatmap of Days Indoors vs Mood Swings.
    """
    setup_chart_style()
    
    # Data Prep
    # Cross tabulation
    mood_order = ['Low', 'Medium', 'High']
    indoors_order = ['1-14 days', '15-30 days', '31-60 days', 'More than 2 months', 'Go out Every day']
    
    # Ensure ordered categorical data for correct sorting
    df['Mood_Swings'] = pd.Categorical(df['Mood_Swings'], categories=mood_order, ordered=True)
    df['Days_Indoors'] = pd.Categorical(df['Days_Indoors'], categories=indoors_order, ordered=True)
    
    heatmap_data = pd.crosstab(df['Days_Indoors'], df['Mood_Swings'], normalize='columns') * 100
    
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    # Heatmap
    # We construct a custom heatmap using scatter or imshow
    # Imshow is easier but standard seaborn is better (no seaborn allowd per user prompt? "pandas, matplotlib").
    # We will use imshow with matplotlib
    
    im = ax.imshow(heatmap_data.values, cmap='bone', aspect='auto') # 'bone' is dark/greyscale/blueish
    
    # Custom loop for text annotations
    for i in range(len(indoors_order)):
        for j in range(len(mood_order)):
            try:
                val = heatmap_data.loc[indoors_order[i], mood_order[j]]
                color = 'black' if val > 50 else '#F4F1DE'
                ax.text(j, i, f'{val:.0f}%', ha='center', va='center', color=color, fontsize=10)
            except KeyError:
                continue

    # Axis Labels
    ax.set_xticks(range(len(mood_order)))
    ax.set_xticklabels(mood_order, fontsize=10)
    ax.xaxis.tick_top() # Put Mood on top
    
    ax.set_yticks(range(len(indoors_order)))
    ax.set_yticklabels(indoors_order, fontsize=10)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.tick_params(axis='both', length=0, pad=10)
    
    return fig

# --- RENDER REMAINING SECTIONS ---

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

# Section 2: Global Headspace
st.markdown("## 03. The Geography of Pain")
st.markdown("<p style='max-width: 600px; margin-bottom: 2rem; color: #8D99AE;'>Reported family history of mental health issues across nations with significant respondent data.</p>", unsafe_allow_html=True)

col_map, col_text = st.columns([2, 1])
with col_map:
    st.pyplot(plot_global_headspace(df))

with col_text:
    st.markdown("""
        <div class='glass-card' style='margin-top: 4rem;'>
            <h4 style='color: #81B29A; margin-bottom: 0.5rem; font-family: Space Mono;'>SENSITIVITY ANALYSIS</h4>
            <p>
                Cultural openness to discussing mental health varies wildly. 
                Higher percentages in Western nations may reflect <i>diagnosis availability</i> 
                rather than higher incidence rates.
                <br><br>
                <b>Key Design Note:</b> The "Acid Sage" dots represent confirmed history.
            </p>
        </div>
    """, unsafe_allow_html=True)


st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

# Section 3: Habit Loop
st.markdown("## 04. The Habit Loop")
st.markdown("<p style='max-width: 600px; margin-bottom: 2rem; color: #8D99AE;'>Correlation between isolation (Days Indoors) and emotional volatility (Mood Swings).</p>", unsafe_allow_html=True)

col_heat, col_desc = st.columns([1.5, 1])

with col_desc:
     st.markdown("""
        <div style='border-left: 2px solid #E07A5F; padding-left: 1.5rem; margin-top: 2rem;'>
            <h3 style='font-size: 2rem; margin-bottom: 0.5rem;'>Isolation Amplifies.</h3>
            <p>
                The data shows a clear darkening of the heatmap as days indoors increase. 
                Those staying inside for 2+ months show distinct volatility patterns compared 
                to the "Go out Every day" cohort.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_heat:
    st.pyplot(plot_habit_loop(df))

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)


def plot_coping_donut(df):
    """
    Visualization 4: The Circle of Control.
    Donut Chart for Coping Struggles.
    """
    setup_chart_style()
    
    # Data Prep
    counts = df['Coping_Struggles'].value_counts()
    
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    # Donut Chart
    # Colors: "Electric Clay" for Yes, "Muted Ash" for No
    colors = ['#E07A5F', '#2D2D30'] 
    
    # Wedgeprops for the "Donut" hole and spacing
    wedges, texts, autotexts = ax.pie(
        counts, 
        labels=counts.index,
        colors=colors,
        startangle=90,
        wedgeprops=dict(width=0.4, edgecolor='#1A1A1C', linewidth=2),
        textprops=dict(color='#F4F1DE', fontfamily='monospace'),
        autopct='%1.1f%%',
        pctdistance=0.75
    )
    
    # Styling text
    for text in texts:
        text.set_fontsize(12)
        text.set_fontweight('bold')
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color('#1A1A1C') # Dark text on the bright wedge
        autotext.set_fontweight('bold')
        
    # Center Circle Text
    ax.text(0, 0, 'COPING\nSTRUGGLES', ha='center', va='center', fontsize=14, color='#8D99AE', fontfamily='monospace', fontweight='bold')
    
    return fig

def plot_gender_treatment(df):
    """
    Visualization 5: The Gender Divide.
    Stacked Bar: Gender vs Seeking Treatment.
    """
    setup_chart_style()
    
    # Data Prep
    # Normalize Gender (Basic cleanup for top 2 + Other)
    top_genders = ['Male', 'Female']
    df['Gender_Group'] = df['Gender'].apply(lambda x: x if x in top_genders else 'Non-Binary/Other')
    
    cross_tab = pd.crosstab(df['Gender_Group'], df['treatment'], normalize='index') * 100
    
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    # Stacked Bar
    # Yes = Electric Clay, No = Muted Ash
    cross_tab.plot(kind='barh', stacked=True, color=['#2D2D30', '#E07A5F'], ax=ax, edgecolor='#1A1A1C')
    
    # Styling
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.set_xticks([])
    ax.tick_params(axis='y', length=0, labelsize=12, pad=10)
    ax.set_ylabel('')
    
    # Annotations
    for c in ax.containers:
        ax.bar_label(c, fmt='%.0f%%', label_type='center', color='#F4F1DE', fontsize=10, fontfamily='monospace')
        
    # Legend
    ax.legend(['No Treatment', 'Sought Treatment'], loc='upper center', bbox_to_anchor=(0.5, 1.1), 
              frameon=False, ncol=2, fontsize=10)
    
    return fig

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

# Section 4: Hidden Battles (New Coverage)
st.markdown("## 05. Hidden Battles")
st.markdown("<p style='max-width: 600px; margin-bottom: 2rem; color: #8D99AE;'>Examining how different groups cope and seek help (Coping Struggles, Gender, Treatment).</p>", unsafe_allow_html=True)

col_donut, col_stack = st.columns([1, 1.5])

with col_donut:
    st.markdown("<h4 style='text-align: center; font-family: Space Mono; color: #8D99AE;'>THE COPING MECHANISM</h4>", unsafe_allow_html=True)
    st.pyplot(plot_coping_donut(df))

with col_stack:
    st.markdown("<h4 style='text-align: center; font-family: Space Mono; color: #8D99AE;'>SEEKING HELP BY GENDER</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.pyplot(plot_gender_treatment(df))
    
    st.markdown("""
        <div class='glass-card' style='margin-top: 1rem;'>
            <p style='font-size: 0.9rem;'>
                <b>Note:</b> While 'Coping Struggles' are nearly evenly split, there is a distinct gap in 
                treatment seek-rates between genders, highlighting potential societal barriers or stigma differences.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)


def plot_symptom_cluster(df):
    """
    Visualization 6: The Symptom Cluster.
    Grouped Bar Chart for Habits, Work Interest, and Social Weakness.
    """
    setup_chart_style()
    
    # Data Prep
    # We want % of "Yes", "No", "Maybe" for each category
    cols = ['Changes_Habits', 'Work_Interest', 'Social_Weakness']
    data = {}
    
    for c in cols:
        counts = df[c].value_counts(normalize=True) * 100
        data[c] = counts
        
    symptom_df = pd.DataFrame(data).fillna(0).T 
    # Reorder columns if needed usually Yes/No/Maybe/Not sure
    # Let's ensure consistent scale
    
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    # Plot
    # Using specific colors: Yes=Electric Clay, No=Muted Ash, Other=Darker
    symptom_df.plot(kind='bar', color=['#E07A5F', '#8D99AE', '#2D2D30', '#4A4A4F'], ax=ax, edgecolor='#1A1A1C')

    # Styling
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.set_xticklabels(['Habit\nChanges', 'Work\nInterest', 'Social\nWeakness'], rotation=0, fontsize=11, fontfamily='monospace')
    ax.tick_params(axis='y', length=0, labelsize=10, pad=10)
    ax.legend(title='Response', frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4)
    
    return fig

def plot_systemic_factors(df):
    """
    Visualization 7: Systemic Factors.
    Small multiples for Care Options, Family History, Interview.
    """
    setup_chart_style()
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    fig.patch.set_alpha(0.0)
    
    factors = [
        ('care_options', 'Care Options'),
        ('family_history', 'Family History'),
        ('mental_health_interview', 'Open to Interview')
    ]
    
    colors = ['#E07A5F', '#8D99AE', '#2D2D30', '#81B29A']

    for i, (col, title) in enumerate(factors):
        ax = axes[i]
        ax.patch.set_alpha(0.0)
        
        counts = df[col].value_counts(normalize=True) * 100
        counts.plot(kind='pie', ax=ax, colors=colors, 
                   autopct='%1.0f%%', startangle=90,
                   wedgeprops=dict(width=0.6, edgecolor='#1A1A1C'),
                   textprops=dict(color='#F4F1DE', fontsize=9, fontfamily='monospace'))
        
        ax.set_ylabel('')
        ax.text(0, 0, title.replace(' ', '\n'), ha='center', va='center', fontsize=10, fontweight='bold', color='#8D99AE')

    return fig

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

# Section 5: The Holistic View
st.markdown("## 06. The Holistic View")
st.markdown("<p style='max-width: 600px; margin-bottom: 2rem; color: #8D99AE;'>A final deep dive into behavioral symptoms and systemic responsiveness.</p>", unsafe_allow_html=True)

# 5.1 Stats Row (Self Employed)
se_count = df[df['self_employed'] == 'Yes'].shape[0]
se_pct = (se_count / df.shape[0]) * 100

st.markdown(f"""
    <div style='border-top: 1px solid #2D2D30; border-bottom: 1px solid #2D2D30; padding: 1rem 0; margin-bottom: 2rem; display: flex; align-items: center; justify-content: space-between;'>
        <span style='font-family: Space Mono; color: #8D99AE;'>DEMOGRAPHIC CONTEXT</span>
        <span style='font-family: Playfair Display; font-size: 1.2rem;'>
            <span style='color: #E07A5F;'>{se_pct:.1f}%</span> of respondents are Self-Employed.
        </span>
    </div>
""", unsafe_allow_html=True)

col_symptoms, col_system = st.columns([1, 1])

with col_symptoms:
    st.markdown("<h4 style='text-align: center; font-family: Space Mono; color: #8D99AE;'>SYMPTOM TRIAD</h4>", unsafe_allow_html=True)
    st.pyplot(plot_symptom_cluster(df))
    st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #666;'>Changes in Habits, Work Interest, and Social Weakness.</p>", unsafe_allow_html=True)

with col_system:
    st.markdown("<h4 style='text-align: center; font-family: Space Mono; color: #8D99AE;'>SYSTEMIC & HISTORY</h4>", unsafe_allow_html=True)
    st.pyplot(plot_systemic_factors(df))
    st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #666;'>Care Options, Family History, and Interview Openness.</p>", unsafe_allow_html=True)

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)



