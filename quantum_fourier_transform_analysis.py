from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

#Quantum Fourier Transform Functions

def qft(circuit, qubits):
    n = len(qubits)
    for i in range(n):
        circuit.h(qubits[i])
        for j in range(i+1, n):
            angle = np.pi / (2**(j-i))
            circuit.cp(angle, qubits[j], qubits[i])
    # SWAPs
    for i in range(n//2):
        circuit.swap(qubits[i], qubits[n-i-1])
    return circuit


def qft_no_swap(circuit, qubits):
    n = len(qubits)
    for i in range(n):
        circuit.h(qubits[i])
        for j in range(i+1, n):
            angle = np.pi / (2**(j-i))
            circuit.cp(angle, qubits[j], qubits[i])
    return circuit


def approx_qft(circuit, qubits, threshold=np.pi/8):
    n = len(qubits)
    for i in range(n):
        circuit.h(qubits[i])
        for j in range(i+1, n):
            angle = np.pi / (2**(j-i))
            if angle > threshold:
                circuit.cp(angle, qubits[j], qubits[i])
    return circuit


#Analyzing the circuit
def analyze_circuit(qc, label):
    sim = AerSimulator()

    compiled = transpile(qc, sim, optimization_level=3)

    print(f"\n--- {label} ---")
    print("Original Depth:", qc.depth())
    print("Optimized Depth:", compiled.depth())
    print("Gate Count:", qc.count_ops())

    return compiled

#Experimenting with different Quantum Fourier Transform functions
def run_experiment(n):
    print(f"\n QFT Analysis for {n} Qubits ")

    # Standard QFT
    qc1 = QuantumCircuit(n)
    qc1.h(range(n))
    qft(qc1, list(range(n)))
    analyze_circuit(qc1, "Standard QFT")

    # No SWAP QFT
    qc2 = QuantumCircuit(n)
    qc2.h(range(n))
    qft_no_swap(qc2, list(range(n)))
    analyze_circuit(qc2, "QFT without SWAP")

    # Approximate QFT
    qc3 = QuantumCircuit(n)
    qc3.h(range(n))
    approx_qft(qc3, list(range(n)))
    analyze_circuit(qc3, "Approximate QFT")


#Run for different number of qubits
for n in [3, 4, 5]:
    run_experiment(n)
