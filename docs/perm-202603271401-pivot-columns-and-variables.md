---
id: 202603271401
title: Permanent Note - Pivot Columns and Variables
type: perm
---

# Pivot Columns and Variables

## My Understanding
A **pivot column** is a column in a matrix that contains a **pivot position** (a leading one) when the matrix is in its Reduced Row-Echelon Form (RREF). The identification of pivot columns is crucial because it directly determines the nature of the variables in the corresponding system of linear equations.

-   **Identification**: To find pivot columns, one must first transform the matrix into its RREF. Any column in the original matrix that corresponds to a column containing a leading '1' in the RREF is a pivot column.
-   **Significance**: Variables associated with pivot columns are called **basic variables**. These variables are constrained and their values are determined by the free variables and the constant terms in the system. They are the variables we "solve for" when expressing the general solution.
-   **Non-Pivot Columns**: Columns that do not contain a pivot in the RREF (excluding the augmented column) correspond to **free variables**.

## Connections
- [[perm-202603271331-leading-entry-and-pivot-position|Leading Entry and Pivot Position]] - Defines what a pivot is.
- [[perm-202603271402-basic-and-free-variables|Basic and Free Variables]] - Explains the types of variables derived from pivot and non-pivot columns.
- [[perm-202603271318-reduced-row-echelon-form-rref|Reduced Row Echelon Form (RREF)]] - The form required to identify pivot columns.

## Source
- [[lit-202603271350-umd-math240-row-echelon-example2|Literature Note: UMD Math 240 - Row-Echelon Form Example 2]]
- [[lit-202603271355-umd-math240-free-basic-variables|Literature Note: UMD Math 240 - Free Variables and Basic Variables]]
