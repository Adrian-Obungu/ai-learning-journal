---
id: 202604081031
title: Permanent Note - Vector Equation to Augmented Matrix
type: perm
---

# Vector Equation to Augmented Matrix

## My Understanding
A crucial connection in linear algebra is the equivalence between a **vector equation** and a **system of linear equations**, which can then be represented as an **augmented matrix**. This translation is fundamental for solving problems involving linear combinations and determining if a vector lies within the span of a set of other vectors.

### The Equivalence:
Consider a vector equation of the form:
$x_1\vec{v}_1 + x_2\vec{v}_2 + \dots + x_k\vec{v}_k = \vec{b}$

Where:
-   $\vec{v}_1, \dots, \vec{v}_k$ are known column vectors (each in $\mathbb{R}^n$).
-   $\vec{b}$ is a known column vector (also in $\mathbb{R}^n$).
-   $x_1, \dots, x_k$ are the unknown scalar weights we are trying to find.

This vector equation is precisely equivalent to a system of linear equations. If we write out each vector component-wise, we get a system where each row represents an equation. For example, if $\vec{v}_1 = \begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{n1} \end{bmatrix}$ and $\vec{b} = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}$, the first row of the system would be $x_1 a_{11} + x_2 a_{12} + \dots + x_k a_{1k} = b_1$.

### Translation to Augmented Matrix:
This system of linear equations can then be directly represented by an augmented matrix:

$[\vec{v}_1 \quad \vec{v}_2 \quad \dots \quad \vec{v}_k \quad | \quad \vec{b}]$

In this augmented matrix:
-   Each column to the left of the augmentation bar is one of the vectors $\vec{v}_i$.
-   The column to the right of the augmentation bar is the vector $\vec{b}$.
-   The unknowns $x_1, \dots, x_k$ correspond to the weights that would be found by solving this system using row reduction (e.g., Gauss-Jordan elimination).

### Significance:
This equivalence is powerful because it allows us to use the well-established techniques of matrix manipulation (like row reduction) to answer questions about vector combinations. It forms the computational backbone for determining consistency, finding unique solutions, or describing infinite solution sets for vector equations.

## Related Notes
- [[lit-202604081030-umd-math240-linear-combinations-part4|Literature Note: UMD Math 240 - Linear Combinations (1.3 Part 4)]]
- [[perm-202604081011-linear-combination-definition|Linear Combination Definition]]
- [[perm-202604081032-solving-for-linear-combination-weights|Solving for Linear Combination Weights]]
- [[perm-202603271246-augmented-matrix-construction|Augmented Matrix Construction]]

## Daily Review Cues
- [ ] How can a vector equation be rewritten as a system of linear equations?
- [ ] How do the vectors $\vec{v}_i$ and $\vec{b}$ map to an augmented matrix?
- [ ] What do the unknowns $x_i$ represent in the context of the augmented matrix?
- [ ] Why is this translation important for solving problems in linear algebra?
