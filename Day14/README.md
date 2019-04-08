# Day 14: Scope

# Objective
<p>
Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!
</p>

---

<p>
The absolute difference between two integers, <i>a</i> and <i>b</i>, is written as |<i>a</i> - <i>b</i>|. The maximum absolute difference between two integers in a set of positive integers, <i>elements</i>, is the largest absolute difference between any two integers in <i>elements</i>.
</p>
<p>
The Difference class is started for you in the editor. It has a private integer array (<i>elements</i>) for storing <i>N</i> non-negative integers, and a public integer (<i>maximumDifference</i>) for storing the maximum absolute difference.
</p>

# Task
<p>Complete teh Difference class by writing the following:</p>
<ul>
<li>A class constructor that takes an array of integers as a parameter and saves it to the <i>elements</i> instance variable.</li>
<li>A computeDifference method that finds the maximum absolute difference between any 2 numbers in <i>N</i> and stores it in the <i>maximumDifference</i> instance variable.</li>
</ul>

# Input Format
<p>
You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in 2 lines of input; the first line contains <i>N</i>, and the second line describes the <i>elements</i> arrray.
</p>

# Constraints
<ul>
<li>
1 ≤ <i>N</i> ≤ 10
</li>
<li>
1 ≤ <i>elements</i>[<i>i</i>] ≤ 100, where 0 ≤ <i>i</i> ≤ <i>N</i> - 1
</li>
</ul>

# Output Format
<p>
You are not responsible for printing any output; the Solution class will print the value of the <i>maximumDifference</i> instance variable.
</p>

# Sample Input

~~~~
3
1 2 5
~~~~

# Sample Output

~~~~
4
~~~~

# Explanation
<p>
The scope of the <i>elements</i> array and <i>maximumDifference</i> integer is the entire class instance. The class constructor saves the argument passed to the constructor as the <i>elements</i> instance variable (where the computeDifference method can access it).
</p>
<p>
To find the maximum difference, computeDifference checks each elements in the array and finds the maximum difference between any 2 elements: |1 - 2| = 1
</p>
<p>
|1 - 5| = 4
</p>
<p>
|2 - 5| = 3
</p>
<p>
The maximum of these differences is 4, so it saves the value 4 as the <i>maximumDifference</i> instance variable. THe locked stub code in the editor then prints the value stored as <i>maximumDifference</i>, which is 4.
</p>


