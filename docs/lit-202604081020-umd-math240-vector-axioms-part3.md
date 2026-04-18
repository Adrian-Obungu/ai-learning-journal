---
id: 202604081020
title: Literature Note - UMD Math 240 - Vector Axioms (1.3 Part 3)
author: Dr. Manning (UMD)
source: 1.3 Part 3 Transcript
date: 2026-04-08
type: lit
---

# Literature Note - UMD Math 240 - Vector Axioms (1.3 Part 3)

## Summary
This session delves into the **axioms** that govern vector addition and scalar multiplication in $\mathbb{R}^n$. These eight properties, though derivable from the component-wise definitions, are presented as foundational "facts" that will later serve as axioms for more general **vector spaces**. The session emphasizes the importance of understanding *why* these properties hold, rather than simply accepting them due to familiarity with real number arithmetic.

## Key Concepts
-   **Vector Space $\mathbb{R}^n$**: Re-emphasized as the set of $n$-by-1 column vectors. Visualization beyond $\mathbb{R}^3$ is difficult, but algebraic operations remain consistent.
-   **Geometric Interpretation of Scalar Multiplication (Revisited)**: Scalar multiplication scales a vector along the same line through the origin. Positive scalars maintain direction, negative scalars reverse it. The set of all scalar multiples of a non-zero vector forms a line through the origin.
-   **Zero Vector ($\vec{0}$)**: A special vector with all entries as zero. Its length is context-dependent (e.g., $\begin{bmatrix} 0 \\ 0 \end{bmatrix}$ in $\mathbb{R}^2$, $\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ in $\mathbb{R}^3$). It acts as the additive identity.
-   **Eight Vector Axioms (Properties)**:
    1.  **Commutativity of Addition**: $\vec{u} + \vec{v} = \vec{v} + \vec{u}$
    2.  **Associativity of Addition**: $(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$
    3.  **Additive Identity**: $\vec{u} + \vec{0} = \vec{u}$
    4.  **Additive Inverse**: $\vec{u} + (-1)\vec{u} = \vec{0}$
    5.  **Distributivity (Scalar over Vector Addition)**: $c(\vec{u} + \vec{v}) = c\vec{u} + c\vec{v}$
    6.  **Distributivity (Vector over Scalar Addition)**: $(c + d)\vec{u} = c\vec{u} + d\vec{u}$
    7.  **Associativity of Scalar Multiplication**: $c(d\vec{u}) = (cd)\vec{u}$
    8.  **Multiplicative Identity**: $1\vec{u} = \vec{u}$
-   **Proof by Component-wise Definition**: The session demonstrates how these properties are proven by applying the component-wise definitions of vector addition and scalar multiplication and leveraging the known properties of real numbers.

## Related Notes
- [[perm-202604081004-vector-space-rn|Vector Space $\mathbb{R}^n$]]
- [[perm-202604081021-zero-vector-and-additive-identity|Zero Vector and Additive Identity]]
- [[perm-202604081022-vector-space-axioms|Vector Space Axioms]]

## Raw Excerpts
> "Let $n$ be some integer greater than or equal to one and define the set of $N$ by one column vectors... to be called bold $R$ with a superscript $N$."
> "Scalar multiplication... is scaling vectors... it scales the vector along the same line."
> "The zero vector... is doing the job of the number zero as far as the is concerned. It's some it's being what's called an additive identity."
> "These properties are later going to be used as axioms to define general systems that like behave in the same way that $R^N$ behaves."
> "Just because you believe the addition is commutative in the real numbers isn't enough reason for you to just automatically believe that addition is commutative in the space of $N$ vectors."
