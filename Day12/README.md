# Day 12: Inheritance

# Objective
<p>
Today, we're delving into inheritance. Check out teh attached tutorial for learning materials and an instructional video!
</p>

# Task
<p>
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for student are provided for you in the editor. Observe that Student inherits all the properties of Person.
</p>
<p>
Complete the Student class by writing the following:
</p>
<ul>
<li>A Student class constructor, which ahs 4 parameters:</li>
<ol>
<li>A string, <i>firstName</i>.</li>
<li>A string, <i>lastName</i>.</li>
<li>An integer, <i>id</i>.</li>
<li>An integer array (or vector) of test scores, <i>scores</i>.</li>
</ol>
<li>A char calculate() method that calculates a Student object's average and returns a Student object's average and returns the grade character representative of their calculated average:</li>
<p></p>

   Grading Scale

| Letter | Average (a)    |
| ------ | -------------- |
| **O**  | 90 ≤ *a* < 100 |
| **E**  | 80 ≤ *a* < 90  |
| **A**  | 70 ≤ *a* < 80  |
| **P**  | 55 ≤ *a* < 70  |
| **D**  | 40 ≤ *a* < 55  |
| **T**  | *a* < 40       |

</ul>

# Input Format
<p>
THe locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls teh calculate method (which takes no arguments).
</p>
<p>
You are not responsible for reading the following input from stdin:
</p>
<p>
The first line contains <i>firstName</i>, <i> lastName</i>, and <i>id</i>, respectively. The second line contains the number of test scores. The third line of space-separated integers describes <i>scores</i>
</p>

# Constraints
<ul>
<li>1 ≤ |<i>firstName</i>|, |<i>lastName</i>| ≤ 10</li>
<li>|<i>id</i>| == 7</li>
<li>0 ≤ <i>score, average</i> ≤ 100</li>
</ul>

# Output Format
<p>
This is handled by the locked stub code in your editor. Your output will be correct if you Student class constructor and calculate() method are properly implemented.
</p>

# Sample Input

~~~~
Heraldo Memelli 8135627
2
100 80
~~~~

# Sample Output

~~~~
Name: Memelli, Heraldo
ID: 8135627
Grade: O
~~~~

# Explanation
<p>
The student had 2 scores to average: 100 and 80. The student's average grade is (100 + 80)/2 = 90. An average grade of 90 corresponds to the letter grade O, so our calculate) method should return the character 'O'.
</p>

