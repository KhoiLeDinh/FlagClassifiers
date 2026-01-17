# Flag Classifier Using Color and Aspect Ratio Analysis

A Python-based flag classification project that distinguishes visually similar national flags by analyzing dominant color distributions and image aspect ratios.

---

## Problem Statement

Several national flags appear nearly identical at first glance, making automated classification difficult.  
Examples include:
- Chad vs. Romania
- Monaco vs. Indonesia
- Netherlands vs. Luxembourg

This project explores whether **simple, explainable image features**—rather than deep learning—are sufficient to distinguish such flags.

---

## Approach

The classifier uses two main visual characteristics:

### 1. Color Analysis
- Extracts dominant colors from the flag image
- Compares RGB values and relative color proportions
- Detects subtle hue differences (e.g., Chad blue vs. Romania blue)

### 2. Aspect Ratio Detection
- Computes image width-to-height ratio
- Uses known official flag proportions to differentiate flags
  - Example:
    - Indonesia: 2:3
    - Monaco: 4:5

The final classification decision is based on a combination of these features.

---

## Supported Flag Pairs

Currently supported flag comparisons include:
- Chad vs. Romania
- Monaco vs. Indonesia
- Netherlands vs. Luxembourg

The system is designed to be easily extended to additional flags.

---

## Installation

### Requirements
- Python 3.8+
- NumPy
- Pillow

Install dependencies:
```bash
pip install -r requirements.txt
