# quantum-algorithm-analysis

## Overview
This repository explores the implementation and analysis of key quantum algorithms, including the Deutsch–Jozsa algorithm and the Quantum Fourier Transform (QFT), using Qiskit.

The focus is on circuit-level efficiency, including depth, gate count, and optimization techniques for scalable quantum computation.

---

## Motivation
Near-term quantum devices are limited by noise and short coherence times. Efficient circuit design is essential for practical quantum computing. This project investigates how algorithmic structures affect circuit performance.

---

## Algorithms Implemented

### 1. Deutsch–Jozsa Algorithm
- Distinguishes constant vs balanced Boolean functions
- Demonstrates quantum advantage using a single oracle query

### 2. Quantum Fourier Transform (QFT)
- Implemented from first principles
- Includes:
  - Standard QFT
  - QFT without SWAP gates
  - Approximate QFT

---

## Key Features
- Circuit depth analysis
- Gate count comparison
- Transpiler optimization (optimization level 3)
- Multi-qubit scalability analysis (3–5 qubits)
- Comparison of optimized vs unoptimized circuits

---

## Results & Observations

### Deutsch–Jozsa
- Constant oracle → always returns all zeros
- Balanced oracle → returns non-zero states
- Demonstrates exponential speedup over classical methods

### QFT
- Removing SWAP gates reduces circuit depth significantly
- Approximate QFT reduces gate count with minimal loss in accuracy
- Circuit depth increases with number of qubits

---

## Sample Outputs

### Deutsch–Jozsa Results
![DJ Results](deutsch_jozsa/dj_results.png)

### QFT Analysis
![QFT Results](qft/qft_results.png)

### Circuit Depth Comparison
![Depth](results/depth_comparison.png)

---

## Technologies Used
- Python
- Qiskit
- NumPy

---

## Future Work
- Noise-aware circuit optimization
- Execution on real quantum hardware
- Error mitigation techniques
- Application to phase estimation and Shor’s algorithm

---

## Author
Tanush Mohan Poola
