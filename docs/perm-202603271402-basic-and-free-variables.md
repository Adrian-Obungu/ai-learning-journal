---
id: 202603271402
title: Permanent Note - Basic and Free Variables
type: perm
---

# Basic and Free Variables

## My Understanding
When a system of linear equations is transformed into its Reduced Row-Echelon Form (RREF), the variables in the system can be categorized into two types: **basic variables** and **free variables**. This distinction is fundamental for understanding the structure of the solution set, especially in cases with infinitely many solutions.

-   **Basic Variables**:
    *   These are the variables that correspond to **pivot columns** in the RREF of the augmented matrix.
    *   Each basic variable has a unique leading '1' in its column, and all other entries in that column are zero.
    *   Basic variables are *dependent* variables; their values are determined by the values of the free variables and the constant terms.
    *   In the solution set, basic variables are expressed in terms of the free variables.

-   **Free Variables**:
    *   These are the variables that correspond to **non-pivot columns** (excluding the augmented column) in the RREF.
    *   Free variables can take on *any real value* (they are 
