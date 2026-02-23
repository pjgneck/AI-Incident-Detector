---
marp: true
theme: default
size: 16:9
paginate: true
title: AI System Health Monitor
---

# AI System Health Monitor  
### Automated Metric Analysis & Real-Time Detection  
**by Parker Groneck**

---

#  The Problem

- **Accessibility:**  
  Monitoring data is fragmented and hard to understand  

- **Complexity:**  
  No clear "birds-eye view" without manual oversight  

- **High Financial Risk:**  
  Failures detected after crashes → revenue loss  

---

#  The Solution

- **Automated Pulling:**  
  AI pulls data from metric sources (e.g., DataDog)  

- **Instant Detection:**  
  Neural network identifies issues in real-time  

- **Unified Interface:**  
  Java-based engine for training + monitoring  

---

#  Key Features

## PY Log Generator
- Simulates high-contrast system behavior  
- Uses **"Jump" Function** for clear classification  

---

## AI Cleaner Script
- Cleans and normalizes raw logs  
- Scales data to **(0.0 → 1.0)**  

---

## JS API (Mock Data)
- Node.js / Express server  
- Serves metrics via HTTP  
- Simulates real-world API interaction  

---

# Proof of Concept (PoC)

- **DecisionPlotter:**  
  Visualizes system behavior clusters in 2D  

- **Goal:**  
  Ensure data is separable  

- **Target:**  
  Validate >70% classification accuracy  

---

# Java-Based AI & CMD Interface

## The Brain
- Custom Multi-Layer Perceptron (MLP)  
- Built from scratch in Java  
- No external libraries  

---

## CMD Interface
- **Hosting:** Real-time monitoring  
- **Training:** Live Backpropagation updates  

---

# Requirements

- Real-time system health classification  
- Immediate issue detection  
- Reduced financial risk  
- Lightweight, production-ready monitoring  
- Detection Accuracy > 70% 