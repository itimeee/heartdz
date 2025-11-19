# Cleveland Heart Disease Dataset - Interactive Visualization

An interactive web-based visualization dashboard for exploring the Cleveland Heart Disease dataset with 303 patient records and 14 clinical features.

## Features

### 📊 Interactive Visualizations

1. **Distribution Analysis**
   - Age distribution histogram with disease status overlay
   - Gender-based disease comparison
   - Chest pain type distribution analysis

2. **Clinical Measurements**
   - Box plots for blood pressure, cholesterol, and heart rate
   - Interactive scatter plot: age vs. max heart rate
   - Correlation heatmap for all numerical features

3. **Disease Indicators**
   - Fasting blood sugar analysis
   - Resting ECG results distribution
   - Exercise-induced angina patterns
   - ST slope analysis
   - Major vessels and thalassemia distribution

4. **Key Insights**
   - Statistical summary cards
   - Feature importance analysis
   - Age group risk analysis
   - Advanced pattern recognition charts
   - Automated key findings

## Dataset Information

**Source:** UCI Machine Learning Repository
**Records:** 303 patients
**Features:** 14 clinical attributes

### Features Description

- **age**: Age in years
- **sex**: Sex (1 = male, 0 = female)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure (mm Hg)
- **chol**: Serum cholesterol (mg/dl)
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (1 = yes, 0 = no)
- **oldpeak**: ST depression induced by exercise
- **slope**: Slope of the peak exercise ST segment (0-2)
- **ca**: Number of major vessels colored by fluoroscopy (0-4)
- **thal**: Thalassemia (0-3)
- **target**: Heart disease presence (1 = yes, 0 = no)

## Usage

### Quick Start

1. **Open the visualization:**
   Simply open `index.html` in a modern web browser (Chrome, Firefox, Safari, or Edge)

2. **Navigate sections:**
   Use the navigation tabs at the top to explore different analyses:
   - Overview
   - Distribution Analysis
   - Clinical Measurements
   - Disease Indicators
   - Key Insights

3. **Interact with charts:**
   - Hover over data points for detailed information
   - Click legend items to show/hide data series
   - Zoom and pan on charts for detailed views
   - Use box selection for focused analysis

### Running the Data Processing Script

If you need to regenerate the processed data:

```bash
python3 process_data.py
```

This will create/update `data/processed_data.json` with:
- Processed patient data
- Statistical summaries
- Feature descriptions

## Technical Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Visualization Library:** Plotly.js 2.27.0
- **Data Processing:** Python 3
- **Styling:** Custom CSS with medical theme

## Project Structure

```
heartdz/
├── index.html              # Main visualization dashboard
├── process_data.py         # Data processing script
├── README.md              # This file
└── data/
    ├── heart_disease.csv      # Raw dataset (303 records)
    └── processed_data.json    # Processed data with statistics
```

## Key Statistics

- **Total Patients:** 303
- **With Heart Disease:** 165 (54.5%)
- **Without Heart Disease:** 138 (45.5%)
- **Average Age:** 54.4 years
- **Male Patients:** 207 (68.3%)
- **Female Patients:** 96 (31.7%)

## Insights Highlighted

The visualization automatically identifies and displays:

1. Gender-specific disease rates
2. High-risk age groups
3. Impact of exercise-induced angina
4. Correlation between clinical measurements
5. Feature importance for disease prediction
6. Patterns in chest pain types
7. ST depression patterns
8. Risk factor combinations

## Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## Notes

- The visualization loads data from `data/processed_data.json`
- All charts are fully interactive with hover tooltips
- The dashboard is responsive and works on tablets and desktops
- No server required - works offline once files are loaded

## Future Enhancements

Possible improvements:
- Add machine learning model predictions
- Include additional statistical tests
- Add data filtering and export capabilities
- Create downloadable reports
- Add more comparative visualizations

## Credits

- **Dataset:** UCI Machine Learning Repository (Cleveland Heart Disease Dataset)
- **Visualization:** Built with Plotly.js
- **Design:** Custom medical-themed interface

## License

This project is for educational and research purposes. The Cleveland Heart Disease dataset is publicly available from the UCI Machine Learning Repository.

---

**Note:** This visualization is for educational purposes only and should not be used for medical diagnosis. Always consult healthcare professionals for medical advice.
