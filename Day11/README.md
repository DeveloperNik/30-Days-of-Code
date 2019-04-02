# Day 11: Arrays

# Objective
<p>
Today, we're building on our knowledge of Arrays by adding another dimension. Check out teh Tutorial tab for learning materials and an instructional video!
</p>

# Context
<p>Given a 6 x 6 2D Array, <i>A</i>:

~~~~
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
~~~~

<p>
We define an hourlgass in <i>A</i> to be a subset of vlaues with indices falling in this pattern in <i>A</i>'s graphical representation:
</p>

~~~~
a b c
  d
e f g
~~~~

<p>
There are 16 hourglasses in <i>A</i>, and an hourglass sum is the sum of an hourglass' values
</p>

# Task
<p>
Calculate the hourglass sum for every hourglass in <i>A</i>, then print the maximum hourglass sum.
</p>

# Input Format
<p>
There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array <i>A</i>; every value in <i>A</i> will be in the inclusive range of -9 to 9.
</p>

# Constraints
<ul>
<li>-9 ≤ <i>A[i][j]</i> ≤ 9</li>
<li>0 ≤ <i>i, j</i> ≤ 5</li>
</ul>

# Output Format
<p>
Print the largest (maximum) hourglass sum found in <i>A</i>.
</p>

# Sample Input

~~~~
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
~~~~

# Sample Output

~~~~
19
~~~~

# Explanation

<p><i>A</i> contains the following hourglasses:</p>

~~~~
1 1 1  1 1 0  1 0 0  0 0 0
  1      0      0      0
1 1 1  1 1 0  1 0 0  0 0 0

0 1 0  1 0 0  0 0 0  0 0 0 
  1      1      0      0
0 0 2  0 2 4  2 4 4  4 4 0

1 1 1  1 1 0  1 0 0  0 0 0
  0      2      4      4
0 0 0  0 0 2  0 2 0  2 0 0

0 0 2  0 2 4  2 4 4  4 4 0
  0      0      2      0
0 0 1  0 1 2  1 2 4  2 4 0
~~~~

<p>The hourglass with the maximum sum (19) is:</p>

~~~~
2 4 4
  2
1 2 4
~~~~

