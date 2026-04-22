from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

#Designing oracles of constant and balanced

def constant_oracle(qc, n):
    # Does nothing → constant function
    pass


def balanced_oracle(qc, n):
    for i in range(n-1):
        qc.cx(i, n-1)


#Designing the circuit

def deutsch_jozsa(n, oracle_type):
    qc = QuantumCircuit(n, n-1)

    # Step 1: Initialize output qubit to |1>
    qc.x(n-1)

    # Step 2: Hadamard on all qubits
    qc.h(range(n))

    qc.barrier()

    # Step 3: Oracle
    if oracle_type == "constant":
        constant_oracle(qc, n)
    else:
        balanced_oracle(qc, n)

    qc.barrier()

    # Step 4: Hadamard on input qubits
    qc.h(range(n-1))

    # Step 5: Measure
    qc.measure(range(n-1), range(n-1))

    return qc

#Analyze
def analyze(qc, label):
    sim = AerSimulator()
    compiled = transpile(qc, sim, optimization_level=3)

    result = sim.run(compiled, shots=1024).result()
    counts = result.get_counts()

    print(f"\n--- {label} ---")
    print("Counts:", counts)
    print("Depth:", qc.depth())
    print("Optimized Depth:", compiled.depth())
    print("Gate Count:", qc.count_ops())


#Experimenting
def run_experiment(n):
    print(f"\n DJ Analysis for {n} qubits ")

    qc_const = deutsch_jozsa(n, "constant")
    analyze(qc_const, "Constant Oracle")

    qc_bal = deutsch_jozsa(n, "balanced")
    analyze(qc_bal, "Balanced Oracle")


# Run
for n in [3, 4, 5]:
    run_experiment(n)
