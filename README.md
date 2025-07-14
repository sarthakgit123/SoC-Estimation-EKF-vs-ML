# State of Charge (SoC) Estimation using EKF and Machine Learning

This project explores two different approaches to estimate the **State of Charge (SoC)** of lithium-ion batteries — a critical task in battery management systems for electric vehicles and energy storage.

I’ve implemented and compared:

- **Extended Kalman Filter (EKF)** – a model-based technique using an equivalent circuit to track SoC in real time.
- **Machine Learning models** – including Linear Regression, Decision Tree, Random Forest, Gradient Boosting, and XGBoost — trained on simulated battery data.

Everything was built and tested using **MATLAB Simulink** for EKF and **Python** for the ML models.

---

## Battery Modeling

The battery is modeled using a simple but effective **1-RC Thevenin equivalent circuit**. It includes:

- An open-circuit voltage source (OCV)
- Instantaneous resistance (R₀)
- A single RC branch (R₁, C₁) to model transient behavior

To make the simulation more realistic, I included thermal effects like temperature variation, heat transfer, and real-world current profiles. Parameters like OCV and resistance values change with both **temperature** and **State of Charge**, captured through lookup tables.

---

## Dataset

I generated a synthetic dataset using Simulink that mimics real-world battery behavior. It includes:

**Inputs:**
- Voltage (V)
- Current (A)
- Temperature (K)

**Output:**
- State of Charge (SoC)

These inputs were chosen because they're commonly available in most battery systems and have a strong influence on SoC.

---

## EKF Implementation

The EKF was built in Simulink using a nonlinear state-space model. It predicts SoC in real time by combining:

- A battery model (equivalent circuit)
- Live sensor measurements (voltage, current, temperature)
- Noise modeling (process + measurement noise)

### What Worked Well:
- Good accuracy in dynamic conditions
- Robustness to sensor noise
- Fast convergence when starting from a reasonable initial guess

---

## Machine Learning Models

To compare with EKF, I trained five supervised ML regression models using Python:

- Linear Regression (baseline)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

Before training, I:
- Cleaned and aligned the data
- Analyzed correlations
- Used feature importance plots to understand which inputs mattered most

### Performance Snapshot:

| Model             | MSE    | RMSE   | MAE    | R² Score |
|------------------|--------|--------|--------|----------|
| Linear Regression| 0.0109 | 0.1043 | 0.0836 | 0.6192   |
| Decision Tree    | 0.0009 | 0.0307 | 0.0076 | 0.9669   |
| Random Forest    | 0.0006 | 0.0243 | 0.0079 | 0.9794   |
| Gradient Boosting| 0.0005 | 0.0220 | 0.0093 | 0.9830   |
| XGBoost          | 0.0007 | 0.0262 | 0.0101 | 0.9760   |

Clearly, **XGBoost and Gradient Boosting** performed best, offering high accuracy across different operating conditions.
