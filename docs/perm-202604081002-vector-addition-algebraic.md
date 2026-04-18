---
id: 202604081002
title: Permanent Note - Vector Addition (Algebraic)
type: perm
---

# Vector Addition (Algebraic)

## My Understanding
Vector addition is a fundamental operation that combines two vectors of the same dimension (length) to produce a new vector. Algebraically, this operation is defined as **component-wise addition**. This means that to add two vectors, you simply add their corresponding entries.

Given two $n$-vectors $\vec{v}$ and $\vec{w}$:
$\vec{v} = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix}$ and $\vec{w} = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}$

Their sum is defined as:
$\vec{v} + \vec{w} = \begin{bmatrix} a_1 + b_1 \\ a_2 + b_2 \\ \vdots \\ a_n + b_n \end{bmatrix}$

### Key Characteristics:
-   **Dimension Preservation**: The sum of two $n$-vectors is always another $n$-vector. This ensures that the operation remains within the same vector space (e.g., adding two 2D vectors results in another 2D vector).
-   **New Operation**: It is crucial to recognize that vector addition, while using the familiar `+` symbol, is a *new mathematical operation* distinct from the addition of real numbers. Its properties (like commutativity and associativity) must be proven based on this component-wise definition, even if they seem intuitively obvious from real number arithmetic.
-   **Prerequisite**: Both vectors must have the same number of components (i.e., be of the same length or dimension) for addition to be defined. Attempting to add vectors of different lengths is an undefined operation.

In the context of AI, vector addition is ubiquitous. For example, when combining feature vectors from different sources or accumulating gradients during neural network training, this component-wise addition is the underlying mechanism.

## Related Notes
- [[lit-202604081000-umd-math240-vector-addition-part1|Literature Note: UMD Math 240 - Vector Addition (1.3 Part 1)]]
- [[perm-202604081001-vector-definition-and-notation|Vector Definition and Notation]]
- [[perm-202604081004-vector-space-rn|Vector Space $\mathbb{R}^n$]]

## Daily Review Cues
- [ ] How is vector addition defined algebraically?
- [ ] What is the primary condition for two vectors to be added?
- [ ] Why is vector addition considered a "new" operation despite using the `+` symbol?
- [ ] What is the dimension of the resulting vector when two $n$-vectors are added?
