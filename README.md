# The Silent Struggle: Mental Health Data Visualization

## Overview
**The Silent Struggle** is a bespoke data visualization application built with Python and Streamlit. It explores a large mental health dataset (N=292,366) to uncover the invisible weight carried by professionals worldwide.

Unlike standard dashboards, this project adheres to a strict "Digital Craftsmanship" design philosophy—rejecting generic templates in favor of a textured, editorial, and human-centric aesthetic.

## 🎨 Design Philosophy
*   **Aesthetic**: "Organic Modernism Meets Clinical Clarity."
*   **Palette**:
    *   **Noise Void** (`#0F0F11`): A textured, deep charcoal background.
    *   **Electric Clay** (`#E07A5F`): High-contrast accent for primary data.
    *   **Acid Sage** (`#81B29A`): Soft accent for positive/neutral trends.
    *   **Typography**: *Playfair Display* (Headlines) & *Space Mono* (Data/Labels).
*   **Interaction**: Zero-spine charts, direct labeling, and glassmorphism cards.

## 🛠️ Technology Stack
*   **Core**: Python 3.x
*   **Framework**: Streamlit
*   **Data Processing**: Pandas
*   **Visualization**: Matplotlib (Customized for CSS consistency)

## 🚀 Installation & Setup

1.  **Clone/Download** this repository.
2.  Open your terminal in the project folder.
3.  **Run the Setup Command** (Windows Powershell):
    ```powershell
    # 1. Create and Activate Virtual Environment
    python -m venv venv
    .\venv\Scripts\activate

    # 2. Install Dependencies
    pip install streamlit pandas matplotlib
    ```

4.  **Run the Application**:
    ```powershell
    streamlit run app.py
    ```

## 📊 Visualizations & Logic

The dashboard is divided into 5 "Story Sections", covering every column in the dataset:

### 1. The Weight of Work
*   **Chart**: Horizontal Bar (Spine-less)
*   **Metric**: `Growing_Stress` vs `Occupation`
*   **Insight**: Identifying which professions are reporting higher perceived stress increases.

### 2. The Geography of Pain
*   **Chart**: Lollipop Chart
*   **Metric**: `Mental_Health_History` vs `Country`
*   **Insight**: A cleaner alternative to choropleth maps, showing the % of reported history by nation.

### 3. The Habit Loop
*   **Chart**: Monochromatic Heatmap (`Bone` colormap)
*   **Metric**: `Days_Indoors` vs `Mood_Swings`
*   **Insight**: Visually proves the correlation between isolation (days indoors) and emotional volatility.

### 4. Hidden Battles
*   **Charts**: Donut Chart & Stacked Bar
*   **Metrics**:
    *   `Coping_Struggles`: The "Circle of Control" showing the split in coping mechanisms.
    *   `Gender` vs `Treatment`: Highlighting the disparity in help-seeking behavior between genders.

### 5. The Holistic View
*   **Charts**: Grouped Bar & Small Multiples
*   **Metrics**:
    *   **Symptom Triad**: `Changes_Habits`, `Work_Interest`, `Social_Weakness`.
    *   **Systemic Factors**: `Care_Options`, `Family_History`, `Interview_Openness`.
    *   **Demographics**: `Self_Employed` context.

## 📁 File Structure
*   `app.py`: The main application entry point including all CSS injection and Python logic.
*   `Mental Health Dataset.csv`: The source data file.
*   `README.md`: This documentation.


