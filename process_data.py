#!/usr/bin/env python3
"""
Process Cleveland Heart Disease dataset for visualization
"""

import csv
import json
from collections import defaultdict

def load_data(file_path):
    """Load CSV data into list of dictionaries"""
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields
            processed_row = {}
            for key, value in row.items():
                try:
                    # Try to convert to float, keep as string if it fails
                    if value == '?':
                        processed_row[key] = None
                    else:
                        processed_row[key] = float(value) if '.' in value else int(value)
                except ValueError:
                    processed_row[key] = value
            data.append(processed_row)
    return data

def calculate_statistics(data):
    """Calculate summary statistics for the dataset"""
    total_patients = len(data)
    with_disease = sum(1 for row in data if row['target'] == 1)
    without_disease = total_patients - with_disease

    males = sum(1 for row in data if row['sex'] == 1)
    females = total_patients - males

    avg_age = sum(row['age'] for row in data) / total_patients
    avg_chol = sum(row['chol'] for row in data if row['chol'] is not None) / sum(1 for row in data if row['chol'] is not None)

    return {
        'total_patients': total_patients,
        'with_disease': with_disease,
        'without_disease': without_disease,
        'disease_percentage': round((with_disease / total_patients) * 100, 1),
        'males': males,
        'females': females,
        'avg_age': round(avg_age, 1),
        'avg_cholesterol': round(avg_chol, 1)
    }

def main():
    # Load the data
    data = load_data('data/heart_disease.csv')

    # Calculate statistics
    stats = calculate_statistics(data)

    # Prepare data structure for JavaScript
    output = {
        'data': data,
        'statistics': stats,
        'feature_names': {
            'age': 'Age',
            'sex': 'Sex (1=male, 0=female)',
            'cp': 'Chest Pain Type',
            'trestbps': 'Resting Blood Pressure',
            'chol': 'Cholesterol',
            'fbs': 'Fasting Blood Sugar > 120 mg/dl',
            'restecg': 'Resting ECG Results',
            'thalach': 'Max Heart Rate',
            'exang': 'Exercise Induced Angina',
            'oldpeak': 'ST Depression',
            'slope': 'Slope of Peak Exercise ST',
            'ca': 'Number of Major Vessels',
            'thal': 'Thalassemia',
            'target': 'Heart Disease (1=yes, 0=no)'
        }
    }

    # Write to JSON file
    with open('data/processed_data.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Processed {len(data)} patient records")
    print(f"Statistics: {stats}")

if __name__ == '__main__':
    main()
