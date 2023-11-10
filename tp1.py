from qiskit import *

# Création du circuit quantique avec 3 qubits et 3 bits classiques
qc = QuantumCircuit(3, 3)

# Hadamard sur le premier et troisième qubit
qc.h([0, 2])

# CX (CNOT) entre le premier et deuxième qubit
qc.cx(0, 1)

# Barrière (utilisée pour séparer visuellement les opérations)
qc.barrier()

# CX (CNOT) entre le troisième et deuxième qubit
qc.cx(2, 1)

# NOT sur le troisième qubit
qc.x(2)

# CX (CNOT) entre le troisième et premier qubit
qc.cx(2, 0)

# NOT sur le troisième qubit
qc.x(2)

# Barrière
qc.barrier()

# SWAP entre le premier et deuxième qubit
qc.swap(0, 1)

# NOT sur le deuxième qubit
qc.x(1)

# CX (CNOT) entre le troisième et deuxième qubit
qc.cx(2, 1)

# NOT sur le premier, deuxième, et troisième qubit
qc.x([0, 1, 2])

# CX (CNOT) entre le troisième et premier qubit
qc.cx(2, 0)

# NOT sur le troisième qubit
qc.x(2)

# Mesures des trois qubits et stockage des résultats dans les bits classiques correspondants
qc.measure([0, 1, 2], [0, 1, 2])

# Dessine le circuit quantique
qc.draw()