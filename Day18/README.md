# Day 18: Queues and Stacks

<p>
Welcome to Day 18! Today we're learning about Stacks and Queues. Check out the Tutorial tab for learning materials and an instrucitonal video!
</p>
<p>
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, <i><strong>s</strong></i>, is a palindrome?
</p>
<p>
To solve this challenge, we must first take each character in <i><strong>s</strong></i>, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as teh characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means <i><strong>s</strong></i> isn't a palindrome).
</p>
<p>
Write the following declarations and implementations:
</p>
<ol>
<li>
Two instance variables: one for your <i><strong>stack</strong></i>, and one for your <i><strong>queue</strong></i>.
</li>
<li>
A void pushCharacter(char ch) method that pushes a character onto a stack.
</li>
<li>
A void enqueueCHaracter(char ch) method that enqueues a character in the <i><strong>queue</strong></i> instance variable.
</li>
<li>
A char popCharacter() method that pops and returns the character at the top of the <i><strong>stack</strong></i> instance variable.
</li>
<li>
A char dequeueCharacter() method that dequeues and returns the first character in the <i><strong>queue</strong></i> instance variable.
</li>
</ol>

# Input Format
<p>
You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string <i><strong>s</strong></i>. It then calls the methods specified above to pass each character to your instance variables.
</p>

# Constraints
<ul>
<li>
<i><strong>s</strong></i> is composed of lowercase English letters.
</li>
</ul>

# Output Format
<p>
You are not responsible for printing any output to stdout.
</p>
<p>
If your code is correctly written and <i><strong>s</strong></i> is a palindrome, the locked stub code will print
<code>
The word, s, is a palindrome.;
</code>
otherwise, it will print
<code>
The word, s, is not a palindrome.
</code>
</p>

# Sample Input

~~~~
racecar
~~~~

# Sample Output

~~~~
The word, racecar, is a palindrome.
~~~~