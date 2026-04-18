---
id: 202604081011
title: Permanent Note - Linear Combination Definition
type: perm
---

# Linear Combination Definition

## My Understanding
A **linear combination** is a fundamental concept in linear algebra that describes how vectors can be combined using the two basic vector operations: scalar multiplication and vector addition. It is essentially a weighted sum of vectors.

Given a set of vectors $\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k$ (all of the same dimension, say in $\mathbb{R}^n$) and a set of scalars (real numbers) $c_1, c_2, \dots, c_k$, a linear combination of these vectors is expressed as:

$c_1\vec{v}_1 + c_2\vec{v}_2 + \dots + c_k\vec{v}_k$

### Key Aspects:
-   **Weights (Scalars)**: The scalars $c_i$ are often referred to as the "weights" or "coefficients" of the linear combination. They determine how much each vector contributes to the final combined vector.
-   **Resulting Vector**: The result of a linear combination is always another vector within the same vector space $\mathbb{R}^n$. This property is crucial for maintaining consistency within linear systems.
-   **Ubiquity in AI**: Linear combinations are at the heart of many AI algorithms. For example:
    -   **Neural Networks**: The output of a neuron is typically a linear combination of its inputs, followed by an activation function.
    -   **Feature Engineering**: Creating new features by combining existing ones (e.g., $c_1 \cdot \text{feature}_1 + c_2 \cdot \text{feature}_2$).
    -   **Image Processing**: Blending images or applying filters often involves linear combinations of pixel values.

Understanding linear combinations is a prerequisite for grasping more advanced concepts like span, linear independence, basis, and transformations, all of which are critical for a deep understanding of AI.

## Related Notes
- [[lit-202604081010-umd-math240-linear-combinations-parallelograms|Literature Note: UMD Math 240 - Linear Combinations and Parallelograms (1.3 Part 2)]]
- [[perm-202604081002-vector-addition-algebraic|Vector Addition (Algebraic)]]
- [[perm-202604081003-scalar-multiplication-algebraic|Scalar Multiplication (Algebraic)]]
- [[perm-202604081004-vector-space-rn|Vector Space $\mathbb{R}^n$]]

## Daily Review Cues
- [ ] Define a linear combination in your own words.
- [ ] What are the components of a linear combination?
- [ ] How is a linear combination related to vector addition and scalar multiplication?
- [ ] Provide an example of how linear combinations are used in AI. 
