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
# How should we update the values of m and b?
If you cannot hold anymore, let's see some weird things...
> <p align = 'center'><b>m<sub>new</sub> = m<sub>old</sub> - α d/<sub>dm</sub>MSE</b></p>
and
> <p align = 'center'><b>b<sub>new</sub> = b<sub>old</sub> - α d/<sub>db</sub>MSE</b></p>
Ohhhooooo!!! What is MSE or α and why they are here?<br>
Before answering the question, let us see apples...<br>
![Apples](https://github.com/Nasim-Ahmed71/Deep-Learning-Easy-Learn/blob/main/Introduction%20to%20ML/Images/Apples.png)
