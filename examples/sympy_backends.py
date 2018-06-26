# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.
"""
Example use of the symbolic simulator backends, which keep precise forms of
amplitudes.
"""

from qiskit_addon_sympy import SympyProvider
# The following import will be replaced by an import of register
# once register is written
from qiskit.wrapper._wrapper import _DEFAULT_PROVIDER
from qiskit import execute, load_qasm_file


def use_sympy_backends():
    """ Usage examples for the Sympy simulators """

    # The following lines will be replaced by a usage of register
    provider = SympyProvider()
    _DEFAULT_PROVIDER.add_provider(provider)
    q_circuit = load_qasm_file('simple.qasm')

    # sympy statevector simulator
    result = execute(q_circuit, backend='local_statevector_simulator_sympy').result()
    print("final quantum amplitude vector: ")
    print(result.get_statevector(q_circuit))

    # sympy unitary simulator
    result = execute([q_circuit], backend='local_unitary_simulator_sympy').result()
    print("\nunitary matrix of the circuit: ")
    print(result.get_unitary(q_circuit))

if __name__ == "__main__":
    use_sympy_backends()
