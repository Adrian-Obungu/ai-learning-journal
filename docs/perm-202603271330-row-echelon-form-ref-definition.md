---
id: 202603271330
title: Permanent Note - Row-Echelon Form (REF) Definition
type: perm
---

# Row-Echelon Form (REF) Definition

## My Understanding
A matrix is said to be in **Row-Echelon Form (REF)** if it satisfies three specific conditions. This form is a crucial intermediate step in the process of solving systems of linear equations using Gaussian elimination. The goal of transforming a matrix into REF is to create a "stair-step" or triangular pattern of non-zero entries, making it easier to solve the corresponding system via back-substitution.

The three conditions for a matrix to be in Row-Echelon Form are:
1.  **Rows of all zeros are at the bottom**: If a matrix contains any rows consisting entirely of zeros, these rows must be grouped together at the very bottom of the matrix.
2.  **Leading entry of each non-zero row is to the left of the leading entry of the row below it**: As you move down the matrix, the first non-zero entry (the "leading entry") of each row must appear further to the right than the leading entry of the row directly above it. This creates the characteristic stair-step pattern.
3.  **All entries in a column below a leading entry are zeros**: For every leading entry, all the numbers directly below it in the same column must be zero. This is achieved through elementary row operations, specifically replacement operations.

Achieving REF allows for a systematic approach to solving linear systems, as it simplifies the equations significantly. It is a less strict form than Reduced Row-Echelon Form (RREF), as leading entries do not necessarily have to be 1, and entries *above* leading entries do not have to be zero.

## Connections
- [[perm-202603271331-leading-entry-and-pivot-position|Leading Entry and Pivot Position]] - Defines the key term used in REF.
- [[perm-202603271316-row-reduction-algorithm-steps|Row Reduction Algorithm Steps]] - REF is the intermediate goal of the forward elimination phase.
- [[perm-202603271318-reduced-row-echelon-form-rref|Reduced Row Echelon Form (RREF)]] - REF is a prerequisite for RREF.

## Source
- [[lit-202603271330-umd-math240-row-echelon-form-part1|Literature Note: UMD Math 240 - Row-Echelon Form Part 1]]
