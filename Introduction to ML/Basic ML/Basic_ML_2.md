If you are accidentally here, move to [Basic_ML](https://github.com/Nasim-Ahmed71/Deep-Learning-Easy-Learn/blob/main/Introduction%20to%20ML/Basic_ML.md)

Let's start with an example:<html><br></html>
We have given some values of x (call them features) and some values of y<sub>actual</sub> (call them targets). Our job is to assume the values of y<sub>actual</sub> for unknown values of x. More simply, we need to find a **pattern**
Suppose, 
  >**x = [1, 2, 3, 4, 5, 6]**<br>
and<br>
  >**y<sub>actual</sub> = [1, 4, 9, 16, 25, 36]**

We can easily find a pattern from here, as the values of y<sub>actual</sub> are the square of the values of x. Therefore, by doing this intuition, we can assume the new values of y<sub>actual</sub> for new values of x. For example, the value of y<sub>actual</sub> will be 100, when the value of x is 10.
But, how we can make the machine learn the pattern on its own? This is where we have to use our so-called equation-
>**y<sub>actual</sub> = mx + b**

In this equation, the values for y<sub>actual</sub> and x are given. We just need to find the best values of m, and b, so that the values of y<sub>actual</sub> and x fit well. Initially, we can assign two random values to m and b. Let, m = 0, and b = 0.
<br>For the given scenario,<br>
let us index the arrays from 0.<br>
x<sub>1</sub> = 1 and y<sub>actual<sub>1</sub></sub> = 1
