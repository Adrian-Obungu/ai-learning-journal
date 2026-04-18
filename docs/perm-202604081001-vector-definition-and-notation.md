---
id: 202604081001
title: Permanent Note - Vector Definition and Notation
type: perm
---

# Vector Definition and Notation

## My Understanding
A **vector** is fundamentally an ordered list of real numbers. This definition is crucial because it moves beyond the intuitive geometric arrow to a precise algebraic structure. The "ordered" aspect is paramount, as the position of each number within the list carries specific meaning. For instance, in a 2D vector `[x, y]`, `x` represents movement along one axis and `y` along another; swapping them changes the vector entirely.

In linear algebra, vectors are conventionally represented as **column vectors**, enclosed in square brackets. This choice is not arbitrary; it facilitates seamless integration with matrix operations, particularly matrix-vector multiplication, which forms the bedrock of many AI algorithms.

### Key Notational Conventions:
-   **Column Format**: `[a1, a2, ..., an]` where `a_i` are real numbers.
-   **Length/Dimension**: An `n`-vector has `n` entries. The set of all such `n`-vectors is denoted as $\mathbb{R}^n$.
-   **Symbolic Representation**: Vectors are typically denoted by lowercase letters with an arrow above them (e.g., $\vec{v}$, $\vec{u}$). This distinguishes them from scalars (single real numbers), which are represented by plain lowercase letters (e.g., `c`, `d`).

This algebraic definition allows us to extend vector concepts beyond the visualizable 2D or 3D spaces into higher dimensions ($\mathbb{R}^n$, where $n > 3$), which are commonplace in machine learning (e.g., feature vectors with hundreds or thousands of dimensions).

## Related Notes
- [[lit-202604081000-umd-math240-vector-addition-part1|Literature Note: UMD Math 240 - Vector Addition (1.3 Part 1)]]
- [[perm-202604081004-vector-space-rn|Vector Space $\mathbb{R}^n$]]

## Daily Review Cues
- [ ] How is a vector defined algebraically?
- [ ] Why is the order of numbers in a vector important?
- [ ] What is the standard notation for a vector in linear algebra?
- [ ] How do you distinguish a vector from a scalar in notation?
- [ ] What is the significance of representing vectors as column vectors?
