import numpy as np

def swap_rows(matrix, r1, r2):
    """Swaps two rows in a matrix."""
    matrix[[r1, r2]] = matrix[[r2, r1]]
    return matrix

def scale_row(matrix, r, scalar):
    """Scales a row by a non-zero scalar."""
    if scalar == 0:
        raise ValueError("Scalar cannot be zero for scaling.")
    matrix[r] = matrix[r] * scalar
    return matrix

def add_multiple_of_row(matrix, r_target, r_source, scalar):
    """Adds a multiple of one row to another row."""
    matrix[r_target] = matrix[r_target] + matrix[r_source] * scalar
    return matrix

def gauss_jordan_elimination(matrix, complexity_level=1):
    """
    Performs Gauss-Jordan elimination to transform a matrix into Reduced Row-Echelon Form (RREF).

    Args:
        matrix (np.array): The augmented matrix to be reduced.
        complexity_level (int):
            1: Basic RREF using NumPy (conceptual, not direct implementation).
            2: Step-by-step manual Gauss-Jordan elimination.
            3: Advanced analysis including numerical stability and pivot selection strategies.

    Returns:
        np.array: The matrix in RREF.
    """
    if complexity_level == 1:
        print("\n--- Complexity Level 1: Basic RREF (NumPy Conceptual) ---")
        print("Objective: Understand the outcome of Gauss-Jordan without manual steps.")
        print("Real-world application: High-level understanding of matrix reduction in libraries like SciPy or TensorFlow, where the underlying algorithm is abstracted.")
        print("Note: NumPy does not have a direct RREF function. This level conceptually represents using a high-level solver that implicitly performs these operations.")
        # For demonstration, we'll still perform the steps but with less verbose output
        return _manual_gauss_jordan(matrix.copy(), verbose=False)

    elif complexity_level == 2:
        print("\n--- Complexity Level 2: Step-by-Step Gauss-Jordan Elimination ---")
        print("Objective: Manually perform and observe each elementary row operation.")
        print("Real-world application: Developing custom linear algebra routines, debugging numerical algorithms, or understanding the computational cost of each step.")
        return _manual_gauss_jordan(matrix.copy(), verbose=True)

    elif complexity_level == 3:
        print("\n--- Complexity Level 3: Advanced Analysis (Numerical Stability & Pivot Selection) ---")
        print("Objective: Explore the impact of pivot selection and floating-point arithmetic on accuracy.")
        print("Real-world application: High-precision scientific computing, embedded systems with limited floating-point support, or optimizing performance for large sparse matrices.")
        print("Tweaks/Improvements: Implement partial pivoting to improve numerical stability, analyze condition number (as in Module 1.1), or use different data types (e.g., `np.float64`).")
        # For this level, we'll perform manual Gauss-Jordan with added considerations
        return _manual_gauss_jordan(matrix.copy(), verbose=True, advanced_analysis=True)

    else:
        raise ValueError("Invalid complexity level. Choose 1, 2, or 3.")

def _manual_gauss_jordan(matrix, verbose=True, advanced_analysis=False):
    """
    Helper function to perform manual Gauss-Jordan elimination.
    """
    rows, cols = matrix.shape
    lead = 0

    for r in range(rows):
        if lead >= cols:
            break
        i = r
        while i < rows and matrix[i, lead] == 0:
            i += 1
        if i < rows:
            if i != r:
                matrix = swap_rows(matrix, i, r)
                if verbose: print(f"  Swapped R{i+1} with R{r+1}:\n{matrix}")

            pivot = matrix[r, lead]
            if pivot != 0:
                matrix = scale_row(matrix, r, 1 / pivot)
                if verbose: print(f"  Scaled R{r+1} by {1/pivot:.2f}:\n{matrix}")

            for i_row in range(rows):
                if i_row != r:
                    factor = matrix[i_row, lead]
                    matrix = add_multiple_of_row(matrix, i_row, r, -factor)
                    if verbose: print(f"  R{i_row+1} = R{i_row+1} + ({-factor:.2f}) * R{r+1}:\n{matrix}")
            lead += 1
        else:
            lead += 1 # No pivot in this column, move to next column

    if advanced_analysis:
        # Example of a simple numerical stability check (can be expanded)
        if verbose:
            print("\n--- Advanced Analysis Insights ---")
            print("Consideration: Small pivot values can lead to large floating-point errors.")
            print("Strategy: Partial pivoting (swapping rows to get the largest possible pivot) can improve stability.")
            print("Example: If a pivot was very close to zero, scaling by 1/pivot would amplify errors.")

    return matrix


if __name__ == "__main__":
    # Example 1: Unique Solution (from UMD 1.2 Part 2 example)
    print("\n--- Example 1: Unique Solution ---")
    augmented_matrix_1 = np.array([
        [1, 0, 4, 5],
        [0, 5, -13, -1],
        [0, -6, 16, 2]
    ], dtype=float)
    print("Original Matrix:\n", augmented_matrix_1)
    rref_matrix_1 = gauss_jordan_elimination(augmented_matrix_1.copy(), complexity_level=2)
    print("\nFinal RREF:\n", rref_matrix_1)
    print("Solution: x1 = {:.2f}, x2 = {:.2f}, x3 = {:.2f}".format(rref_matrix_1[0, -1], rref_matrix_1[1, -1], rref_matrix_1[2, -1]))

    # Example 2: Inconsistent System (from UMD 1.2 Part 3 example)
    print("\n--- Example 2: Inconsistent System ---")
    augmented_matrix_2 = np.array([
        [1, 1, 4, -5, 2],
        [0, -1, -1, 3, -2],
        [0, 7, 7, -21, 9]
    ], dtype=float)
    print("Original Matrix:\n", augmented_matrix_2)
    rref_matrix_2 = gauss_jordan_elimination(augmented_matrix_2.copy(), complexity_level=2)
    print("\nFinal RREF:\n", rref_matrix_2)
    if np.any(np.all(rref_matrix_2[:, :-1] == 0, axis=1) & (rref_matrix_2[:, -1] != 0)):
        print("Interpretation: Inconsistent system (e.g., 0 = non-zero), no solution.")
    else:
        print("Interpretation: Consistent system.")

    # Example 3: Infinite Solutions (from UMD 1.2 Part 5 example)
    print("\n--- Example 3: Infinite Solutions ---")
    augmented_matrix_3 = np.array([
        [1, -1, 2, 1],
        [0, 1, -1, 2],
        [0, 0, 0, 0]
    ], dtype=float)
    print("Original Matrix:\n", augmented_matrix_3)
    rref_matrix_3 = gauss_jordan_elimination(augmented_matrix_3.copy(), complexity_level=2)
    print("\nFinal RREF:\n", rref_matrix_3)
    if np.all(rref_matrix_3[-1, :-1] == 0) and rref_matrix_3[-1, -1] == 0 and np.sum(np.all(rref_matrix_3[:, :-1] == 0, axis=1)) < rref_matrix_3.shape[0]:
        print("Interpretation: Consistent system with infinite solutions (free variables present).")
        print("Parametric form: x1 = {:.2f} - {:.2f}*x3, x2 = {:.2f} + {:.2f}*x3, x3 is free.".format(rref_matrix_3[0, -1], rref_matrix_3[0, -2], rref_matrix_3[1, -1], -rref_matrix_3[1, -2]))
    else:
        print("Interpretation: Consistent system with unique solution or inconsistent.")

    # Demonstrate Complexity Level 3
    print("\n--- Demonstrating Complexity Level 3 ---")
    # A slightly ill-conditioned matrix for demonstration
    ill_conditioned_matrix = np.array([
        [1, 1, 10],
        [1, 1.0001, 10.0001]
    ], dtype=float)
    print("Original Ill-Conditioned Matrix:\n", ill_conditioned_matrix)
    gauss_jordan_elimination(ill_conditioned_matrix.copy(), complexity_level=3)

    print("\n--- Demonstrating Complexity Level 1 (Conceptual) ---")
    gauss_jordan_elimination(augmented_matrix_1.copy(), complexity_level=1)
