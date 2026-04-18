
import numpy as np

def solve_linear_system(A_matrix, B_vector, complexity_level=1):
    """
    Solves a system of linear equations represented by an augmented matrix [A|B].

    Args:
        A_matrix (np.array): The coefficient matrix (A).
        B_vector (np.array): The constant vector (B).
        complexity_level (int): 
            1: Basic solution using NumPy's built-in solver.
            2: Step-by-step Gaussian Elimination (conceptual, not implemented here for brevity).
            3: Advanced analysis including condition number and error estimation.

    Returns:
        tuple: (solution_vector, message) or (None, error_message)
    """

    if complexity_level == 1:
        print("\n--- Complexity Level 1: Basic Solution (NumPy Solver) ---")
        print("Objective: Quickly find the solution using optimized library functions.")
        print("Real-world application: Rapid prototyping, situations where computational efficiency is paramount and underlying mechanics are abstracted.")
        try:
            solution = np.linalg.solve(A_matrix, B_vector)
            message = f"Solution found using np.linalg.solve: x = {solution}"
            return solution, message
        except np.linalg.LinAlgError:
            message = "The system is singular (inconsistent or infinitely many solutions)."
            return None, message

    elif complexity_level == 2:
        print("\n--- Complexity Level 2: Conceptual Gaussian Elimination ---")
        print("Objective: Understand the step-by-step process of row reduction.")
        print("Real-world application: Developing custom solvers for specific hardware, educational purposes, or when numerical stability requires fine-grained control.")
        print("\nNote: Full Gaussian Elimination implementation is complex and omitted for this example. Conceptually, it involves:")
        print("1. Forward Elimination: Transforming the matrix into an upper triangular form (echelon form) using Elementary Row Operations.")
        print("2. Back Substitution: Solving for variables starting from the last equation and substituting back into previous ones.")
        print("This process is what np.linalg.solve does efficiently under the hood.")
        return None, "Conceptual explanation of Gaussian Elimination provided."

    elif complexity_level == 3:
        print("\n--- Complexity Level 3: Advanced Analysis (Condition Number) ---")
        print("Objective: Assess the sensitivity of the solution to small changes in input data.")
        print("Real-world application: Critical engineering applications (e.g., aerospace, financial modeling) where precision and error propagation are vital. Helps identify ill-conditioned systems.")
        try:
            # Calculate the condition number
            # A high condition number indicates an ill-conditioned system,
            # meaning small changes in A or B can lead to large changes in the solution.
            condition_number = np.linalg.cond(A_matrix)
            print(f"Condition Number of A: {condition_number:.2f}")

            if condition_number > 1000:
                print("Warning: This system is ill-conditioned. Solutions may be highly sensitive to input perturbations.")
            else:
                print("The system is well-conditioned. Solutions are relatively stable.")

            # Attempt to solve the system
            solution = np.linalg.solve(A_matrix, B_vector)
            message = f"Solution found with advanced analysis: x = {solution}"
            return solution, message
        except np.linalg.LinAlgError:
            message = "The system is singular (inconsistent or infinitely many solutions), cannot calculate condition number or solve directly."
            return None, message

    else:
        return None, "Invalid complexity level. Choose 1, 2, or 3."

# --- Example Usage ---
# Define the augmented matrix from the Part 4 (Bonus) example
# System:
# x1 + 2x2 + 2x3 = 4
# x1 + 3x2 + 3x3 = 5
# 2x1 + 6x2 + 5x3 = 6

A_coeff = np.array([
    [1, 2, 2],
    [1, 3, 3],
    [2, 6, 5]
])

B_const = np.array([4, 5, 6])

# Run at different complexity levels
print("\n--- Running Active Lab: Mathematical Foundations for AI Engineering ---")

sol1, msg1 = solve_linear_system(A_coeff, B_const, complexity_level=1)
print(msg1)

sol2, msg2 = solve_linear_system(A_coeff, B_const, complexity_level=2)
print(msg2)

sol3, msg3 = solve_linear_system(A_coeff, B_const, complexity_level=3)
print(msg3)

# Example of an ill-conditioned system (slightly perturbed from original)
print("\n--- Testing an Ill-Conditioned System Example ---")
A_ill = np.array([
    [1.000, 2.000, 2.000],
    [1.001, 3.000, 3.000],
    [2.000, 6.000, 5.000]
])
B_ill = np.array([4.0, 5.0, 6.0])

sol_ill, msg_ill = solve_linear_system(A_ill, B_ill, complexity_level=3)
print(msg_ill)

# Example of a singular system (inconsistent - parallel planes)
print("\n--- Testing a Singular System Example (Inconsistent) ---")
A_singular = np.array([
    [1, 1],
    [1, 1]
])
B_singular = np.array([1, 2]) # x+y=1, x+y=2 (parallel lines)

sol_singular, msg_singular = solve_linear_system(A_singular, B_singular, complexity_level=1)
print(msg_singular)

sol_singular_adv, msg_singular_adv = solve_linear_system(A_singular, B_singular, complexity_level=3)
print(msg_singular_adv)
