---
id: 202604081050
title: Literature Note - UMD Math 240 - Span (1.3 Part 6)
author: Dr. Manning (UMD)
source: 1.3 Part 6 Transcript
date: 2026-04-08
type: lit
---

# Literature Note - UMD Math 240 - Span (1.3 Part 6)

## Summary
This session introduces the crucial concept of the **span** of a set of vectors. The span is defined as the set of all possible linear combinations that can be formed from a given set of vectors. It explores how to determine if a vector is in the span of others and provides geometric interpretations of span in $\mathbb{R}^2$ and $\mathbb{R}^3$, illustrating that the span can be a line, a plane, or the entire space.

## Key Concepts
-   **Span of a Set of Vectors**: Denoted as $\text{Span}\{\vec{v}_1, \dots, \vec{v}_k\}$, it is the set of all vectors $\vec{b}$ that can be written as a linear combination of $\vec{v}_1, \dots, \vec{v}_k$. Algebraically, $\text{Span}\{\vec{v}_1, \dots, \vec{v}_k\} = \{c_1\vec{v}_1 + \dots + c_k\vec{v}_k \mid c_1, \dots, c_k \in \mathbb{R}\}$.
-   **Determining if a Vector is in the Span**: To check if a vector $\vec{b}$ is in the span of $\{\vec{v}_1, \dots, \vec{v}_k\}$, one must determine if the vector equation $x_1\vec{v}_1 + \dots + x_k\vec{v}_k = \vec{b}$ has a solution. This is done by forming the augmented matrix $[\vec{v}_1 \dots \vec{v}_k | \vec{b}]$ and checking its consistency through row reduction.
-   **Geometric Interpretation of Span**:
    -   **Span of one non-zero vector**: A line passing through the origin in the direction of the vector.
    -   **Span of two non-collinear vectors in $\mathbb{R}^2$**: The entire $\mathbb{R}^2$ plane.
    -   **Span of two non-collinear vectors in $\mathbb{R}^3$**: A plane passing through the origin. It cannot span all of $\mathbb{R}^3$.
    -   **Span of vectors in higher dimensions**: Extends these geometric ideas, though visualization becomes impossible.
-   **Trivial Linear Combination**: The zero vector is always in the span of any non-empty set of vectors, as it can be formed by setting all weights to zero ($0\vec{v}_1 + \dots + 0\vec{v}_k = \vec{0}$). This is called the trivial linear combination.

## Related Notes
- [[perm-202604081011-linear-combination-definition|Linear Combination Definition]]
- [[perm-202604081031-vector-equation-to-augmented-matrix|Vector Equation to Augmented Matrix]]
- [[perm-202604081032-solving-for-linear-combination-weights|Solving for Linear Combination Weights]]
- [[perm-202604081051-span-of-vectors-definition|Span of Vectors Definition]]
- [[perm-202604081052-geometric-interpretation-of-span|Geometric Interpretation of Span]]

## Raw Excerpts
> "If I have a set of actors $V_1$ through $V_K$ living in $R^N$ and I have some other vector $B$ also living in $R^N$. Can I tell whether $B$ is some linear combination of $V_1$ through $V_K$?"
> "This is the same as the system of equations... with Augmented Matrix... $V_1$ through $V_K$ augmented with $B$."
> "I want to make a definition for now. We'll make a definition. I'm going to say... this set... is the same as the set of all possible linear combinations."
> "Call that set of all possible linear combinations of $X V_1$ through $V_K$ Call that set the span of $V_1$ through $V_K$."
> "If instead I had some... $R^3$ here... and I just take a pair of vectors... These things only span a subset of all of $R^3$. They don't span everything."
