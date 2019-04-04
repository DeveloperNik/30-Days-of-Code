# Day 8: Dictionaries & Maps

# Objective
<p>
Tidatm we;re kearbubg aviyt Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!
</p>

# Task
<p>
Given <i>n</i> names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each <i>name</i> queried, print the associated entry from your phone book on a new line in the form <code>name=phoneNumber;</code> if an entry for <i>name</i> is not found, print <code>Not found</code> instead.
</p>
<p>
<strong>Note:</strong> Your phone book should be a Dictionary/Map/HashMap data structure
</p>

# Input Format
<p>
The first line contains an integer, <i>n</i>, denoting the number of entries in the phone book.
</p>
<p>
Each of the <i>n</i> subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.
</p>
<p>
After the <i>n</i> lines of phone entries, there are an unkown number of lines of queries. Each line (query) contains a <i>name</i> to look up, and you must continue reading lines until there is no more input.
</p>
<p>
<strong>Note:</strong> Names consist of lowercase English alphabetic letters and are first names only.
</p>

# Constraints
<ul>
<li>1 ≤ <i>n</i> ≤ 10^5</li>
<li>1 ≤ <i>queries</i> ≤ 10^5</li>
</ul>

# Output Format
<p>
On a new line for each query, print <code>Not found</code> if the name has no corresponding entry in the phone book; otherwise, print the full <i>name</i> and <i>phoneNumber</i> in the format <code>name=phoneNumber.</code>
</p>

# Sample Input

~~~~
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
~~~~

# Sample Output

~~~~
sam=99912222
Not found
harry=12299933
~~~~

# Explanation
<p>
We add the following <i>n</i>  3 (Key,Value) pairs to our map so it looks like this:
</p>
<p>
<code>
<i>phoneBook</i> = {(<i>sam</i>, 99912222), (<i>tom</i>, 11122222), (<i>harry</i>, 12299933)}
</code>
</p>
<p>
We then process each query and print <code>key=value</code> if the queried <i>key</i> is found in the map; otherwise, we print <code>Not found.</code>
</p>
<p>Query 0: <code>sam</code></p>
<p>
Sam is one of the keys in our dictionary, so we print <code>sam=99912222.</code>
</p>
<p>Query 1: <code>edward</code></p>
<p>
Sam is not one of the keys in our dictionary, so we print <code>Not found.</code>
</p>
<p>Query 2: <code>harry</code></p>
<p>
Sam is one of the keys in our dictionary, so we print <code>harry=12299933</code>
</p>

