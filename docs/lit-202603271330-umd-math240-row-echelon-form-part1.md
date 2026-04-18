---
id: 202603271330
title: Literature Note - UMD Math 240 - Row-Echelon Form (1.2 Part 1)
author: Dr. Manning (UMD)
source: 1.2 Part 1 Transcript
date: 2026-03-27
type: lit
---

# Literature Note - UMD Math 240 - Row-Echelon Form (1.2 Part 1)

## Summary
This session formally defines **Row-Echelon Form (REF)** and **Reduced Row-Echelon Form (RREF)**, which are the target states for matrices undergoing Gaussian and Gauss-Jordan elimination. It introduces the concept of **row equivalence** and the critical notion of a **leading entry**, laying the groundwork for understanding how to systematically solve systems of linear equations and interpret their solution sets.

## Key Concepts
-   **Row Equivalence**: Two matrices are row equivalent if one can be transformed into the other through a sequence of Elementary Row Operations. Row equivalent matrices correspond to systems of linear equations with the same solution space.
-   **Leading Entry**: The leftmost non-zero entry in a non-zero row of a matrix.
-   **Row-Echelon Form (REF)**: A matrix is in REF if it satisfies three conditions:
    1.  All non-zero rows are above any rows of all zeros.
    2.  Each leading entry of a non-zero row is in a column to the right of the leading entry of the row above it.
    3.  All entries in a column below a leading entry are zeros.
-   **Reduced Row-Echelon Form (RREF)**: A matrix is in RREF if it satisfies the three REF conditions, plus two additional conditions:
    4.  The leading entry in each non-zero row is 1 (a "leading one" or "pivot").
    5.  Each column containing a leading 1 has zeros everywhere else (above and below the leading 1).
-   **Uniqueness of RREF**: Every matrix is row equivalent to exactly one matrix in reduced row-echelon form.

## Related Notes
- [[perm-202603271330-row-echelon-form-ref-definition|Row-Echelon Form (REF) Definition]]
- [[perm-202603271331-leading-entry-and-pivot-position|Leading Entry and Pivot Position]]
- [[perm-202603271318-reduced-row-echelon-form-rref|Reduced Row Echelon Form (RREF)]]
- [[perm-202603271247-elementary-row-operations-explained|Elementary Row Operations Explained]]

## Raw Excerpts
> "...row echelon form of a matrix, which is kind of the goal of all the RO operations we were doing..."
> "Any two matrices are really equivalent provided that there's a sequence of RO operations you can do that will get you from one to the other."
> "The leading entry of a row... is the leftmost nonzero entry."
> "A matrix is in Row Echelon Form... provided that the following three things are all true."
> "If in addition, you get two more things, four and five... Then we said that our matrix is in reduced row echelon form."
> "Every matrix... is row equivalent to exactly one matrix in reduced row, echelon form."
