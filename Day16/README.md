# Day 16: Exceptions - String to Integer

# Objective
<p>
Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error message. Check out the Tutorial tab for learning materials and an instructional video!
</p>

# Task
<p>
Read a string, <i>S</i>, and print its integer value; if <i>S</i> cannot be converted to an integer, print <code>Bad String</code>.
</p>
<p>
<strong>
Note:
</strong>
You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a 0 score.
</p>

# Input Format
<p>A single string, <i>S</i></p>

# Constraints
<ul>
<li>
1 ≤ |<i>S</i>| ≤ 6, where |<i>S</i>| is the length of string <i>S</i>.
</li>
<li>
<i>S</i> is composed of either lowercase letters (<i>a</i> - <i>z</i>) or decimal digits (0 - 9)
</li>
</ul>

# Output Format
<p>
Print the parsed integer value of <i>S</i>, or <code>Bad String</code> if <i>S</i> cannot be converted to an integer.
</p>

# Sample Input 0

~~~~
3
~~~~

# Sample Output 0

~~~~
3
~~~~

# Sample Input 1

~~~~
za
~~~~

# Sample Output 0

~~~~
Bad String
~~~~

# Explanation
<p>
Sample Case 0 contains an integer, so it should not raise an exception when we attempt to convert it to an integer. Thus, we print 3.
</p>
<p>
Sample Case 1 does not contain any integers, so an attempt to convert it to an integer will raise an exception. Thus, our exception handler prints <code>Bad String</code>
</p>