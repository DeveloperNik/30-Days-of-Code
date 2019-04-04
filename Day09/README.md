# Day 9: Recursion 3

# Objective
<p>
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!
</p>

# Recursive Method for Calculating Factorial
<p>
<i>factorial(N)</i> = 1 if <i>N</i> ≤ 1
</p>
<p>
<i>factorial(N)</i> = <i>N</i> x <i>factorial</i>(<i>N</i> - 1) otherwise
</p>

# Task
<p>
Write a factorial function taht takes a positive integer, <i>N</i>, as a parameter and prints the result of <i>N</i>! (<i>N</i>) factorial).
</p>
<p><strong>Note:</strong> if you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.</p>

# Input Format
<p>
A single integer, <i>N</i> (the argument to pass to factorial).
</p>

# Constraints
<ul>
<li>2 ≤ <i>N</i> ≤ 12</li>
<li>Your submission must contain a recursive function named factorial</li>
</ul>

# Output Format
<p>
Print a single integer denoting <i>N</i>!.
</p>

# Sample Input
<p>
<code>3</code>
</p>

# Sample Output
<p>
<code>6</code>
</p>

# Explanation
<p>
Consider the following steps:
</p>
<ol>
<li><i>factorial</i>(3) = 3 x <i>factorial</i>(2)</li>
<li><i>factorial</i>(2) = 2 x <i>factorial</i>(1)</li>
<li><i>factorial</i>(1) = 1</li>
</ol>
<p>
From steps 2 and 3, we can say <i>factorial</i>(2) = 2 x 1 = 2; then when we apply the value from <i>factorial</i>(2) to step 1, we get <i>factorial</i>(3) = 3 x 2 x 1 = 6. Thus, we print 6 as our answer.
</p>