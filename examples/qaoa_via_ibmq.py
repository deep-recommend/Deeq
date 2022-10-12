from blueqat import pauli, vqe
from qiskit import Aer

def maxcut_qaoa(n_step, edges, minimizer=None, sampler=None, verbose=True):
    """Setup QAOA.

    :param n_step: The number of step of QAOA
    :param n_sample: The number of sampling time of each measurement in VQE.
                     If None, use calculated ideal value.
    :param edges: The edges list of the graph.
    :returns Vqe object
    """
    sampler = sampler or vqe.non_sampling_sampler
    minimizer = minimizer or vqe.get_scipy_minimizer(
        method="Powell",
        options={"ftol": 5.0e-2, "xtol": 5.0e-2, "maxiter": 1000, "disp": True}
    )
    hamiltonian = pauli.I() * 0

    for i, j in edges:
        hamiltonian += pauli.Z(i) * pauli.Z(j)

    return vqe.Vqe(vqe.QaoaAnsatz(hamiltonian, n_step), minimizer, sampler)

if __name__ == "__main__":
    # If you use IBM Q remote backend, use qiskit.register.
    # import qiskit
    # qiskit.register(your token here)
    runner = maxcut_qaoa(1, [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3), (0, 2), (4, 0), (4, 3)],
            sampler=vqe.get_qiskit_sampler(backend=Aer.get_backend('qasm_simulator')))
    result = runner.run(verbose=True)
    print("""
       {4}
      / \\
     {0}---{3}
     | x |
     {1}---{2}
""".format(*result.most_common()[0][0]))
