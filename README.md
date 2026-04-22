# Quantum Circuit Optimization using Qiskit

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

| Qubits | Oracle Type | Output | Depth | Optimized Depth | CNOT Gates | Hadamard Gates |
|--------|------------|--------|-------|-----------------|------------|----------------|
| 3      | Constant   | 00     | 4     | 3               | 0          | 5              |
| 3      | Balanced   | 11     | 6     | 5               | 2          | 5              |
| 4      | Constant   | 000    | 4     | 3               | 0          | 7              |
| 4      | Balanced   | 111    | 7     | 6               | 3          | 7              |
| 5      | Constant   | 0000   | 4     | 3               | 0          | 9              |
| 5      | Balanced   | 1111   | 8     | 7               | 4          | 9              |

### QFT Analysis

| Qubits | Version            | Depth | Optimized Depth | Hadamard (H) | Phase (CP) | SWAP |
|--------|-------------------|-------|-----------------|--------------|------------|------|
| 3      | Standard QFT      | 7     | 5               | 6            | 3          | 1    |
| 3      | No-SWAP QFT       | 6     | 5               | 6            | 3          | 0    |
| 3      | Approximate QFT   | 6     | 5               | 6            | 3          | 0    |
| 4      | Standard QFT      | 9     | 7               | 8            | 6          | 2    |
| 4      | No-SWAP QFT       | 8     | 7               | 8            | 6          | 0    |
| 4      | Approximate QFT   | 8     | 7               | 8            | 5          | 0    |
| 5      | Standard QFT      | 11    | 9               | 10           | 10         | 2    |
| 5      | No-SWAP QFT       | 10    | 9               | 10           | 10         | 0    |
| 5      | Approximate QFT   | 10    | 9               | 10           | 7          | 0    |

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
