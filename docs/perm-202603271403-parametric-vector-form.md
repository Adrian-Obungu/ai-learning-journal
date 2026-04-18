---
id: 202603271403
title: Permanent Note - Parametric Vector Form
type: perm
---

# Parametric Vector Form

## My Understanding
**Parametric vector form** is a powerful and concise way to represent the entire solution set of a consistent system of linear equations, especially when the system has infinitely many solutions (i.e., one or more free variables). It expresses the solution vector as a sum of two components:

1.  **A particular solution vector**: This is a constant vector obtained by setting all free variables to zero. It represents one specific point in the solution space.
2.  **A linear combination of vectors**: Each free variable is multiplied by a unique vector, and these products are summed. These vectors represent the directions in which the solution space extends. Each vector corresponds to a free variable and is derived from the coefficients of that free variable in the expressions for the basic variables.

Geometrically, the parametric vector form describes a line (if there's one free variable), a plane (if there are two free variables), or a higher-dimensional hyperplane that passes through the particular solution and is spanned by the direction vectors. This form clearly separates the constant part of the solution from the part that varies with the free parameters.

## Connections
- [[perm-202603271402-basic-and-free-variables|Basic and Free Variables]] - Parametric vector form is used when free variables exist.
- [[perm-202603271233-the-three-possible-solution-states|The Three Possible Solution States]] - This form describes the infinite solution case.
- [[perm-202603271318-reduced-row-echelon-form-rref|Reduced Row Echelon Form (RREF)]] - RREF is necessary to identify basic and free variables and derive the parametric form.

## Example
If a system's solution is $x_1 = 3 - t$, $x_2 = 2 + t$, $x_3 = t$ (where $t$ is a free variable), the parametric vector form would be:

$$\mathbf{x} = \begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$$

Here, $\begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix}$ is the particular solution, and $\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$ is the direction vector associated with the free variable $t$.

## Source
- [[lit-202603271355-umd-math240-free-basic-variables|Literature Note: UMD Math 240 - Free Variables and Basic Variables]]
- [[lit-202603271400-umd-math240-more-complicated-example|Literature Note: UMD Math 240 - More Complicated Example]]
