# Day 4: Class vs. Instance

# Objective
<p>In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!</p>

# Task
<p>Write an Person class with an instance variable, <i>age</i>, and a constructor that takes an integer, <i>initialAge</i>, as a parameter. The constructor must assign <i>initialAge</i> to <i>age</i> after confirming the argument passed as <i>initialAge</i> is not negative; if a negative argument is passed as <i>initialAge</i>, the constructor should set <i>age</i> to 0 and print <code>Age is not valid, setting age to 0</code>. In addition, you must write the following methods:</p>
<ol>
<li>yearPassed() should increase the <i>age</i> instance variable by 1.</li>
<li>amIOld() should perform the following conditional actions:<li>
<ul>
<li>if <i>age</i> < 13, print <code>You are young.</code></li>
<li>if <i>age</i> ≥ 13 and <i>age</i> < 18 print <code>You are a teenager</code></li>
<li>Otherwise, print <code>You are old.</code>.<li>
</ul>
</ol>
<p>To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the futur. The Code that creates each instance of you Person class is in the main method. Don't worry if you don't understand it all quite yet!</p>
<p><strong>Note:</strong>Do not remove or alter teh stub code in the editor.</p>

# Input Format
<p>Input is handled for you by the stub code in the editor</p>
<p>The first line contains an integer, <i>T</i> (the number of test cases), and the <i>T</i> subsequent lines each contain an integer denoting the <i>age</i> of a Person instance.

# Constraints
<ul>
<li>1 ≤ <i>T</i> ≤ 4</li>
<li>-5 ≤ <i>age</i> ≤ 30</li>
</ul>

# Output Format
<p>Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print 2 or 3 lines (depending on where or not a valid <i>initialAge</i> was passed to the constructor).</p>

# Sample Input

~~~~
 4
-1
10
16
18
~~~~

# Sample Output

~~~~
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
~~~~

# Explanation
<p>Test Case 0: <i>initialAge</i> = -1</p>
<p>Because<i>initialAge</i> < 0, our code must set <i>age<i> to 0 and print the "Age is not valid..." message followed by the young message. Three years pass and <i>age</i> = 3, so we pring the young message again.</p>
<p>Test Case 1:<i>initialAge</i> = 10</p>
<p>Because <i>initialAge</i> < 13, our code should print that the person is young. Three years pass and <i>age</i> = 13, so we print that the person is now a teenager.</p>
<p>Test Case 2:<i>initialAge</i> = 16</p>
<p>Because 13 ≤ <i>initialAge</i> < 18, our code should print tha tthe person is a teenager. Three years pass and <i>age</i> = 19, so we print that the person is old.</p>
<p>Test Case 3: <i>initialAge</i> = 18</p>
<p>Because <i>initialAge</i> ≥ 18, our code should print that the person is old. Three years pass and the person is still old at <i>age</i> = 21, so we print the old massage again.</p>
<p><strong>The extra line at the end of the output is supposed to be there and is trimmed before being compared against the test case's expected output. If you're failing this challenge, check your logic and review your print statements for spelling errors.</strong></p>