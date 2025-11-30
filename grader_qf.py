import datetime
import math

import networkx as nx
import numpy as np
import qiskit
import qiskit.quantum_info

CORRECT_MESSAGE = "Congratulations! 🎉 Your answer is correct."
INCORRECT_MESSAGE = "Sorry, your answer is incorrect. Please try again."

def grade_ex2_qf(max_execution_time_ex2: int) -> str:
    # Check max QPU time specified
    if not isinstance(max_execution_time_ex2, int):
        return "Type error in input parameter"

    if not max_execution_time_ex2 == 900:
        return "Please set the max QPU time to 900 seconds. Please try again."

    return CORRECT_MESSAGE


def grade_ex3_qf(precision: float, estimate_time_only: str) -> str:

    # check types:
    if not isinstance(precision, float) or not isinstance(estimate_time_only, str):
        return "Type error in input parameter"

    # test options
    if precision != 0.02:
        return "Precision is not set to the correct value. Please try again."

    if estimate_time_only != "analytical":
        return 'Analytical time estimation should be used, i.e., estimate_time_only="analytical". Please try again.'

    return CORRECT_MESSAGE

def grade_ex_4_1(circuit: qiskit.QuantumCircuit) -> str:

    if not isinstance(circuit, qiskit.QuantumCircuit):
        return "Circuit should be a QuantumCircuit object. Please try again."

    if circuit.num_qubits != 5:
        return "Circuit should have 5 qubits (n_qubits_ex4 = 5). Please try again."

    expected_2q_layers = 20
    actual_2q_layers = circuit.depth(filter_function=lambda instr: len(instr.qubits) == 2)

    if actual_2q_layers != expected_2q_layers:
        return f"Circuit should have {expected_2q_layers} two-qubit gate layers " f"(10 steps × 2 layers per step). Found {actual_2q_layers}. Please try again."

    expected_barriers = 9
    actual_barriers = sum(1 for instr in circuit.data if instr.operation.name == "barrier")

    if actual_barriers != expected_barriers:
        return f"Circuit should have {expected_barriers} barriers " f"(one between each of the 10 steps). Found {actual_barriers}. Please try again."

    expected_theta_x = math.pi / 6
    expected_theta_zz = math.pi / 3

    for instr in circuit.data:
        if instr.operation.name == "rx":
            if not np.isclose(instr.operation.params[0], expected_theta_x):
                return f"RX gate angles should be π/6 (theta_x_ex4). " f"Found {instr.operation.params[0]}. Please try again."
        elif instr.operation.name == "rzz":
            if not np.isclose(instr.operation.params[0], expected_theta_zz):
                return f"RZZ gate angles should be π/3 (theta_zz_ex4). " f"Found {instr.operation.params[0]}. Please try again."

    return CORRECT_MESSAGE

def grade_ex_4_2_qf(
    precision_ex4_2: float,
    circuit_ex4_2: qiskit.QuantumCircuit,
    observables_ex4_2: list[qiskit.quantum_info.SparsePauliOp],
    backend_ex4_2: str,
    estimate_time_only_ex4_2: str,
) -> str:

    # Expected values for Exercise 4.2
    n_qubits = 5
    n_steps = 10
    theta_x = math.pi / 6
    theta_zz = math.pi / 3

    circ = kicked_ising_1d(n_qubits, theta_x, theta_zz, n_steps)
    observable = qiskit.quantum_info.SparsePauliOp.from_sparse_list([("Z" * n_qubits, range(n_qubits), 1)], n_qubits)  # Global Z measurement

    # Check precision
    if not isinstance(precision_ex4_2, (int, float)):
        return "Precision should be a float. Please try again."

    if precision_ex4_2 <= 0.03:
        return "Precision should be greater than 0.03. Please try again."

    # Check backend name
    if not isinstance(backend_ex4_2, str):
        return "Backend name should be a string. Please try again."

    if not backend_ex4_2.lower().startswith("fake"):
        return "Backend name should be an IBMQ fake backend noisy simulator. Please try again."

    if estimate_time_only_ex4_2 != "empirical":
        return "Empirical time estimation should be used. Please try again."

    # Check pubs format
    if not isinstance(circuit_ex4_2, qiskit.QuantumCircuit):
        return "Circuit should be a QuantumCircuit object. Please try again."

    if not isinstance(observables_ex4_2, list) or not len(observables_ex4_2) == 1 or not isinstance(observables_ex4_2[0], qiskit.quantum_info.SparsePauliOp):
        return "Observables should be a list of a single SparseObservable. Please try again."

    # Check if the circuit matches the expected circ_ex4
    if not qiskit.quantum_info.Operator(circuit_ex4_2).equiv(qiskit.quantum_info.Operator(circ)):
        return "Circuit should be circ_ex4 created with kicked_ising_1D. Please try again."

    # Check if the observable matches the expected observable_ex4
    if not observables_ex4_2[0].simplify() == observable.simplify():
        return "Observable should be the global Z measurement (observable_ex4). Please try again."

    return CORRECT_MESSAGE

def grade_ex_4_3_qf(max_execution_time_ex4_3: int) -> str:

    if 60 <= max_execution_time_ex4_3 <= 600:
        return CORRECT_MESSAGE

    return "max_qpu_time_ex4_3 should be between 1 minute and 10 minutes. Please try again."


def kicked_ising_1d(num_qubits: int, theta_x: float, theta_zz: float, num_steps: int) -> qiskit.QuantumCircuit:
    """
    Parameters:
        num_qubits (int): number of qubits on chain.
        theta_x (float): Angle for RX gates.
        theta_zz (float): Angle for RZZ gates.
        num_steps (int): Number of steps.

    Returns:
        QuantumCircuit: The resulting quantum circuit.
    """
    graph = nx.path_graph(num_qubits)
    qc = qiskit.QuantumCircuit(num_qubits)

    # Precompute edge layers (alternating non-overlapping pairs)
    edges = list(graph.edges())
    even_edges = [(u, v) for (u, v) in edges if u % 2 == 0]
    odd_edges = [(u, v) for (u, v) in edges if u % 2 == 1]

    for step in range(num_steps):
        # RX on all qubits
        for q in range(num_qubits):
            qc.rx(theta_x, q)

        # Apply even and odd layers separately
        for edge_layer in [even_edges, odd_edges]:
            for u, v in edge_layer:
                qc.rzz(theta_zz, u, v)

        if step < num_steps - 1:
            qc.barrier()

    return qc
