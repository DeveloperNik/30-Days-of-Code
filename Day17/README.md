# Day 17: More Exceptions

# Objective
<p>
Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In today's cahllenge, you're going to practice throwing and propagating an exception. Check out the Tutorial tab for learning materials and an instructional video!
</p>

# Task
<p>
Write a Calculator class with a single method: int power(int,int). The power method takes two integers, <i>n</i> and <i>p</i>, as parameters and returns the integer result of <i>n</i>^<i>p</i>. If either <i>n</i> or <i>p</i> is negative, then the method must throw an exception with the message: <code>n and p should be non-negative</code>.
</p>
<p>
<strong>
Note:
<strong>
Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.
</p>

# Input Format
<p>
Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer, <i>T</i>, the number of test cases. Each of the <i>T</i> subsequent lines describing a test case in 2 space-separated integers denoting <i>n</i> and <i>p</i>, respectively.
</p>

# Constraints
<ul>
<li>No Test Case will result in overflow for correctly written code</li>
</ul>

# Output Format
<p>
Output to stdout is handled for you by the locked stub code in your editor. There are <i>T</i> lines of output, where each line contains the result of <i>n</i>^<i>p</i> as calculated by your Calculator class' power method.
</p>

# Sample Input

~~~~
4
3 5
2 4
-1 -2
-1 3
~~~~

# Sample Output

~~~~
243
16
n and p should be non-negative
n and p should be non-negative
~~~~

# Explanation
<p>
<i>T</i> = 4
</p>
<p>
T0: 3 and 5 are positive, so power returns the result of 3^5, which is 243.
</p>
<p>
T1: 2 and 4 are positive, so power returns the result of 2^4, which is 16.
</p>
<p>
T2: Both inputs (-1 and -2) are negative, so power throws an exception and <code>n and p should be non-negative</code> is printed.
</p>
<p>
T3: One of the inputs (-1) is negative, so power throws an exception and <code>n and p should be non-negative</code> is printed.
</p>