import numpy as np

def vector_add(v1, v2):
    """Performs vector addition."""
    return v1 + v2

def scalar_multiply(scalar, v):
    """Performs scalar multiplication."""
    return scalar * v

def linear_combination(vectors, scalars):
    """Calculates a linear combination of vectors."""
    if len(vectors) != len(scalars):
        raise ValueError("Number of vectors and scalars must be equal.")
    
    if not vectors:
        return np.array([])

    result = np.zeros_like(vectors[0])
    for i in range(len(vectors)):
        result += scalar_multiply(scalars[i], vectors[i])
    return result

def is_in_span(vectors, target_vector, complexity_level=1):
    """
    Determines if a target_vector is in the span of a set of vectors.

    Args:
        vectors (list of np.array): A list of vectors that define the span.
        target_vector (np.array): The vector to check if it's in the span.
        complexity_level (int):
            1: Basic check using NumPy's linear solver.
            2: Conceptual explanation of forming and solving the augmented matrix.
            3: Advanced analysis including rank and null space considerations.

    Returns:
        tuple: (bool, message) indicating if the vector is in the span and an explanation.
    """
    num_vectors = len(vectors)
    if num_vectors == 0:
        return np.all(target_vector == 0), "No vectors to span. Only zero vector is in span."

    # Form the coefficient matrix A from the input vectors
    # Each vector becomes a column in A
    A = np.array(vectors).T # Transpose to make vectors columns

    # Check if the target vector has the same dimension as the vectors in the set
    if A.shape[0] != target_vector.shape[0]:
        return False, "Dimension mismatch between spanning vectors and target vector."

    if complexity_level == 1:
        print("\n--- Complexity Level 1: Basic Span Check (NumPy Solver) ---")
        print("Objective: Quickly determine if a vector is in the span using optimized library functions.")
        print("Real-world application: Rapid prototyping, quick checks in data preprocessing, or when computational efficiency is prioritized over understanding the underlying mechanics.")
        try:
            # Solve Ax = b for x (the scalars for the linear combination)
            # If a solution exists, b is in the span of the columns of A
            coefficients = np.linalg.solve(A, target_vector)
            # Verify the linear combination
            reconstructed_vector = linear_combination(vectors, coefficients)
            if np.allclose(reconstructed_vector, target_vector):
                return True, f"Vector is in the span. Coefficients: {coefficients}"
            else:
                return False, "Vector is not in the span (numerical instability or no exact solution)."
        except np.linalg.LinAlgError as e:
            if "Singular matrix" in str(e) or "coefficients are not unique" in str(e):
                # This means the columns of A are linearly dependent, or system is inconsistent
                # We need a more robust check for consistency in this case
                # For complexity 1, we simplify to 'not directly solvable by simple inverse'
                return False, "Vector is not in the span (or spanning vectors are linearly dependent, leading to no unique solution for coefficients)."
            return False, f"An error occurred: {e}"

    elif complexity_level == 2:
        print("\n--- Complexity Level 2: Conceptual Span Check (Augmented Matrix) ---")
        print("Objective: Understand the equivalence between a vector equation and an augmented matrix, and interpret consistency.")
        print("Real-world application: Debugging linear algebra problems, understanding the theoretical basis of feature engineering, or explaining model interpretability.")
        
        # Form the augmented matrix [A | b]
        augmented_matrix = np.hstack((A, target_vector.reshape(-1, 1)))
        print(f"Augmented Matrix [A | b]:\n{augmented_matrix}")

        # Conceptually, we would perform row reduction here.
        # For simplicity in this conceptual level, we'll use NumPy's rank function
        # A vector b is in the span of the columns of A if and only if
        # rank(A) == rank([A | b])
        rank_A = np.linalg.matrix_rank(A)
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)

        if rank_A == rank_augmented:
            message = "Vector is in the span. The system Ax=b is consistent (rank(A) == rank([A|b]))."
            if rank_A == A.shape[1]: # If rank equals number of columns, unique solution
                try:
                    coefficients = np.linalg.solve(A, target_vector)
                    message += f" Unique coefficients: {coefficients}"
                except np.linalg.LinAlgError:
                    message += " (Unique solution, but direct solve failed due to numerical issues)"
            else:
                message += " (Infinitely many solutions for coefficients, as spanning vectors are linearly dependent)."
            return True, message
        else:
            return False, "Vector is not in the span. The system Ax=b is inconsistent (rank(A) != rank([A|b]))."

    elif complexity_level == 3:
        print("\n--- Complexity Level 3: Advanced Span Analysis (Rank, Null Space, and Geometric Interpretation) ---")
        print("Objective: Deeply analyze the properties of the spanning set, including linear independence, basis, and the dimension of the subspace.")
        print("Real-world application: Dimensionality reduction (PCA), understanding model capacity, feature selection in high-dimensional data, or anomaly detection in cybersecurity.")

        rank_A = np.linalg.matrix_rank(A)
        num_cols = A.shape[1]
        dimension_of_space = A.shape[0]

        message_parts = []

        # Linear Independence
        if rank_A == num_cols:
            message_parts.append(f"Spanning vectors are linearly independent. They form a basis for their span (dimension {rank_A}).")
        else:
            message_parts.append(f"Spanning vectors are linearly dependent. The dimension of their span is {rank_A} (less than the number of vectors). There are {num_cols - rank_A} free variables.")

        # Check if target vector is in span (consistency)
        augmented_matrix = np.hstack((A, target_vector.reshape(-1, 1)))
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)

        if rank_A == rank_augmented:
            message_parts.append("Target vector IS in the span (system is consistent).")
            if rank_A == num_cols:
                message_parts.append("  - Unique combination of spanning vectors exists.")
            else:
                message_parts.append("  - Infinitely many combinations of spanning vectors exist.")
            
            # Null Space (for deeper understanding of infinite solutions)
            if rank_A < num_cols:
                # Find a basis for the null space of A
                # This is more complex to implement directly without symbolic math libraries
                # Conceptually, if Ax=0 has non-trivial solutions, then there's a null space
                message_parts.append("  - The null space of the coefficient matrix is non-trivial, indicating redundancy in the spanning vectors.")

            # Geometric Interpretation (simplified for text output)
            if rank_A == 1:
                message_parts.append("  - Geometrically, the span is a line through the origin.")
            elif rank_A == 2 and dimension_of_space >= 2:
                message_parts.append("  - Geometrically, the span is a plane through the origin.")
            elif rank_A == dimension_of_space:
                message_parts.append(f"  - Geometrically, the span is the entire space R^{dimension_of_space}.")
            else:
                message_parts.append(f"  - Geometrically, the span is a {rank_A}-dimensional subspace of R^{dimension_of_space}.")

            return True, "\n".join(message_parts)
        else:
            message_parts.append("Target vector IS NOT in the span (system is inconsistent).")
            message_parts.append("  - Geometrically, the target vector lies outside the subspace formed by the spanning vectors.")
            return False, "\n".join(message_parts)

    else:
        return False, "Invalid complexity level. Choose 1, 2, or 3."


if __name__ == "__main__":
    print("\n--- Module 1.3: Vector Operations & Span Active Lab ---")

    # Example Vectors
    v1 = np.array([1, 2])
    v2 = np.array([3, 4])
    v3 = np.array([5, 6])
    v4 = np.array([2, 4]) # Linearly dependent with v1

    # --- Part 1: Basic Vector Operations ---
    print("\n### Part 1: Basic Vector Operations")
    print(f"Vector v1: {v1}")
    print(f"Vector v2: {v2}")

    # Vector Addition
    sum_v1_v2 = vector_add(v1, v2)
    print(f"v1 + v2 = {sum_v1_v2}")

    # Scalar Multiplication
    scaled_v1 = scalar_multiply(2, v1)
    print(f"2 * v1 = {scaled_v1}")

    # Linear Combination
    lc_result = linear_combination([v1, v2], [2, -1])
    print(f"2*v1 - 1*v2 = {lc_result}")

    # --- Part 2: Is a Vector in the Span? ---
    print("\n### Part 2: Is a Vector in the Span?")

    # Example 1: Target vector IS in the span (unique solution)
    print("\n--- Example 1: Target vector IS in the span (unique solution) ---")
    span_vectors_1 = [np.array([1, 0]), np.array([0, 1])]
    target_1 = np.array([5, 7])
    print(f"Spanning vectors: {span_vectors_1}")
    print(f"Target vector: {target_1}")

    in_span, msg = is_in_span(span_vectors_1, target_1, complexity_level=1)
    print(f"Complexity Level 1: {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_1, target_1, complexity_level=2)
    print(f"Complexity Level 2: {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_1, target_1, complexity_level=3)
    print(f"Complexity Level 3: {in_span}. {msg}")

    # Example 2: Target vector IS NOT in the span (inconsistent system)
    print("\n--- Example 2: Target vector IS NOT in the span (inconsistent system) ---")
    span_vectors_2 = [np.array([1, 1, 0]), np.array([0, 1, 0])]
    target_2 = np.array([1, 1, 1]) # Cannot be formed by these vectors
    print(f"Spanning vectors: {span_vectors_2}")
    print(f"Target vector: {target_2}")

    in_span, msg = is_in_span(span_vectors_2, target_2, complexity_level=1)
    print(f"Complexity Level 1: {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_2, target_2, complexity_level=2)
    print(f"Complexity Level 2: {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_2, target_2, complexity_level=3)
    print(f"Complexity Level 3: {in_span}. {msg}")

    # Example 3: Target vector IS in the span (infinitely many solutions - linearly dependent spanning vectors)
    print("\n--- Example 3: Target vector IS in the span (infinitely many solutions) ---")
    span_vectors_3 = [np.array([1, 2]), np.array([2, 4])]
    target_3 = np.array([3, 6]) # This is 3 * [1, 2]
    print(f"Spanning vectors: {span_vectors_3}")
    print(f"Target vector: {target_3}")

    in_span, msg = is_in_span(span_vectors_3, target_3, complexity_level=1)
    print(f"Complexity Level 1: {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_3, target_3, complexity_level=2)
    print(f"Complexity Level 2: {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_3, target_3, complexity_level=3)
    print(f"Complexity Level 3: {in_span}. {msg}")

    # Example 4: Span of two vectors in R^3 (forms a plane)
    print("\n--- Example 4: Span of two vectors in R^3 (forms a plane) ---")
    span_vectors_4 = [np.array([1, 0, 0]), np.array([0, 1, 0])]
    target_4_in = np.array([2, 3, 0]) # In the xy-plane
    target_4_out = np.array([2, 3, 1]) # Not in the xy-plane
    print(f"Spanning vectors: {span_vectors_4}")
    print(f"Target vector (in plane): {target_4_in}")
    print(f"Target vector (out of plane): {target_4_out}")

    in_span, msg = is_in_span(span_vectors_4, target_4_in, complexity_level=3)
    print(f"Complexity Level 3 (in plane): {in_span}. {msg}")
    in_span, msg = is_in_span(span_vectors_4, target_4_out, complexity_level=3)
    print(f"Complexity Level 3 (out of plane): {in_span}. {msg}")

    # --- Part 3: Geometric Visualization (Conceptual) ---
    print("\n### Part 3: Geometric Visualization (Conceptual)")
    print("For 2D vectors, you can visualize span as:")
    print("  - Single non-zero vector: A line through the origin.")
    print("  - Two non-collinear vectors: A plane (the entire 2D space if in R^2, or a plane in R^3).")
    print("  - Two collinear vectors: Still a line through the origin.")
    print("In higher dimensions, these concepts extend algebraically, even if direct visualization is not possible.")
    print("Real-world application: Understanding feature spaces in machine learning, where each feature is a dimension. Span helps define the 'reach' of your data.")
