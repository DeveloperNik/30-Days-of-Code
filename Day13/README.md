# Day 13: Abstract Classes

# Objective
<p>
Today, we're taking what we learned yesterday about Inheritance and extending it to Abstract Classes. Because this is a very specific Object-Oriented concept, submissions are limited to the few languages that use this construct. Check out the Tutorial tab for learning materials and an instructional video!
</p>

# Task
<p>
Given a Book class and a Solution class, write a MyBook class that does the following:
</p>
<ul>
<li>Inherits from Book</li>
<li>Has a parameterized constructor taking these 3 parameters:</li>
<ol>
<li>string <i>title</i></li>
<li>string <i>author</i></li>
<li>int <i>price</i></li>
</ol>
<li>Implements the Book class' abstract display() method so it prints these 3 lines:</li>
<ol>
<li><code>Title:</code>, a space, and then the current isntance's <i>title</i>.</li>
<li><code>Author:</code>, a space, and then the current instance's <i>author</i></li>
<li><code>Price:</code>, a space, and then the current instance's <i>price</i></li>
</ol>
</ul>

<p>
<strong>Note:</strong> Because these classes are being written in the same file, you must not use an access modifier (e.g.: <code>public</code>) when declaring MyBook or your code will not execute.
</p>

# Input Format
<p>
You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls teh MyBook class constructor (passing it the necessary arguments). It then calls teh display method on the Book object.
</p>

# Output Format
<p>
The <i>void display</i>() method should print and label the repsective <i>title, author,</i> and <i>price</i> of the MyBook object's instance (with each value on its own line) like so:
</p>

~~~~
Title: $title
Author: $author
Price: $price
~~~~

<p><strong>Note:</strong> The $ is prepended to variable names to indicate they are placeholders for variables.</p>

# Sample Input
<p>
The following input from stdin is handled by the locked stub code in your editor:
</p>

~~~~
The Alchemist
Paulo Coelho
248
~~~~

# Sample Output
<p>
The following output is printed by your display() method:
</p>

~~~~
Title: The Alchemist
Author: Paulo Coelho
Price: 248
~~~~
