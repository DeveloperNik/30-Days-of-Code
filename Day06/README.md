# Day 6: Let's Review

# Objective
<p>Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!</p>

# Task
<p>Given a string, <i>S</i>, of length <i>N</i> that is indexed from 0 to <i>N</i> - 1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).</p>
<p><strong>Note: </strong>0 is considered to be an even index.</p>

# Input Format
<p>
The first line contains an integer, <i>T</i> (the number of test cases).
</p>
<p>
Each line <i>i</i> of the <i>T</i> subsequent lines contains a String, <i>S</i>.
</p>

# Constraints
<ul>
<li>
1 ≤ <i>T</i> ≤ 10
</li>
<li>
2 ≤ length of <i>S</i> ≤ 10000
</li>
</ul>

# Output Format
<p>
For each string <i>Sj</i> (where 0 ≤ <i>j</i> ≤ <i>T</i> - 1), print <i>Sj</i>'s even-indexed characters, followed by a space, followed by <i>Sj</i>'s odd-indexed characters.
</p>

# Sample Input

~~~~
2
Hacker
Rank
~~~~

# Sample Output

~~~~
Hce akr
Rn ak
~~~~

# Explanation
<p>
Test Case 0: <i>S</i> = "Hacker"
</p>
<p>
<i>S</i>[0] = "H"
</p>
<p>
<i>S</i>[1] = "a"
</p>
<p>
<i>S</i>[2] = "c"
</p>
<p>
<i>S</i>[3] = "k"
</p>
<p>
<i>S</i>[4] = "e"
</p>
<p>
<i>S</i>[5] = "r"
</p>
<p>
The even indices are 0, 2, and 4, and the odd indices are 1, 3, and 5. We then print a single line of 2 space-separated strings; the first string contains the ordered characters from <i>S</i>'s even indices (<code>Hce</code>), and the second string contains the ordered characters from <i>S</i>'s odd indices (<code>akr</code>)
</p>
<p>
Test Case 1: <i>S</i> = "Rank"
</p>
<p>
<i>S</i>[0] = "R"
</p>
<p>
<i>S</i>[1] = "a"
</p>
<p>
<i>S</i>[2] = "n"
</p>
<p>
<i>S</i>[3] = "k"
</p>
<p>
The even indices are 0 and 2, and the odd indices are 1 and 3. We then print a single line of 2 space-separated strings; the first string contains the ordered characters from <i>S</i>'s even indices (<code>Rn</code>), and the second string contains the ordered characters from <i>S</i>'s odd indices (<code>ak</code>)
</p>