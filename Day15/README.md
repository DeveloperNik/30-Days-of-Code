# Day 15: Linked List

# Objective
<p>
Today we're working with Linked Lists. Check out the Tutorial tab for learning materials and an isntructional video!
</p>

---

<p>
A Node class is provided for you in teh editor. A Node object has an integer data field, <i>data</i>, and a Node instance pointer, <i>next</i>, pointing to another node (i.e.: the next node in a list).
</p>
<p>
A Node insert function is also declared in your editor. It has two parameters: a pointer, <i>head</i>, pointing to the first node of a linked list, and an integer <i>data</i> value that must be added to teh end of the list as a new Node object.
</p>

# Task
<p>
Complete the insert function in your editor so that it creates a new Node (pass <i>data</i> as the Node constructor argument) and inserts it at the tail of the linked list referenced by the <i>head</i> parameter. Once the new node is added, return the reference to the <i>head</i> node.
</p>
<p>
<strong>
Note:
</strong>
If the <i>head</i> argument passed to the insert function is null, then the initial list is empty.
</p>

# Input Format
<p>
The insert function has 2 parameters: a pointer to a Node named <i>head</,i>, and an integer value, <i>data</i>.
</p>
<p>
The constructor for Node has 1 parameter: an integer value for the <i>data</i> field.
</p>
<p>
You do not need to read anything from stdin.
</p>

# Output Format
<p>
Your insert function should return a reference to the <i>head</i> node of the linked list.
</p>

# Sample Input
<p>
The following input is handled for you by the locked code in the editor:
</p>
<p>
The first line contains T, the number of test cases.
</p>
<p>
The <i>T</i> subsequent lines of test cases each contain an integer to be inserted at the list's tail.
</p>

~~~~
4
2
3
4
1
~~~~

# Sample Output
<p>
The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:
</p>

~~~~
2 3 4 1
~~~~

# Explanation
<p>
<i>T</i> = 4, sot eh locked code in teh editor will be inserting 4 nodes.
</p>
<p>
The list is initially empty, so <i>head</i> is null; accounting for this, our code returns a new node containing the data value 2 as the <i>head</i> of our list. We then create and insert ndoes 3, 4, and 1 at the tail of our list. The resulting list returned by the last call to <i>insert</i> is [2, 3, 4, 1], so the printed output is 2 3 4 1.
</p>
![alt text](https://s3.amazonaws.com/hr-challenge-images/17168/1456961238-28488bfa0d-LinkedListExplanation.png)



