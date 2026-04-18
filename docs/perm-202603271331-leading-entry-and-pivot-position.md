---
id: 202603271331
title: Permanent Note - Leading Entry and Pivot Position
type: perm
---

# Leading Entry and Pivot Position

## My Understanding
In the context of matrices and row reduction, the concepts of **leading entry** and **pivot position** are fundamental for understanding the structure of a matrix in Row-Echelon Form (REF) and Reduced Row-Echelon Form (RREF).

-   **Leading Entry**: The leftmost non-zero entry in a non-zero row of a matrix. Every non-zero row has exactly one leading entry. Rows of all zeros do not have a leading entry.

-   **Pivot Position**: A location in a matrix that corresponds to a leading entry in the row-echelon form of the matrix. Once a matrix is transformed into REF or RREF, the positions of these leading entries are called pivot positions. The column containing a pivot position is called a **pivot column**.

These concepts are crucial because they dictate the structure of the solution set for a system of linear equations. Variables corresponding to pivot columns are typically **basic variables**, while variables corresponding to non-pivot columns (excluding the augmented column) are **free variables**.

## Connections
- [[perm-202603271330-row-echelon-form-ref-definition|Row-Echelon Form (REF) Definition]] - Leading entries define the structure of REF.
- [[perm-202603271318-reduced-row-echelon-form-rref|Reduced Row Echelon Form (RREF)]] - Pivot positions are key to RREF.
- [[perm-202603271401-pivot-columns-and-variables|Pivot Columns and Variables]] - Explains the significance of columns containing pivots.

## Example
Consider a matrix in REF:
$$\begin{pmatrix}
\mathbf{2} & 1 & 3 & 4 \\
0 & \mathbf{5} & 6 & 7 \\
0 & 0 & 0 & \mathbf{1}
\end{pmatrix}$$
Here, the leading entries are 2, 5, and 1 (bolded). Their positions are pivot positions.

## Source
- [[lit-202603271330-umd-math240-row-echelon-form-part1|Literature Note: UMD Math 240 - Row-Echelon Form Part 1]]
