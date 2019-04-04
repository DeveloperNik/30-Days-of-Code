# Day 2: Operators

# Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instruction video!

# Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of teh meal price being added as tax) for a meal, find and print the meal's total cost.
# Note:
Be sure to use precise values for your calculations, or you may end up with an incorrecly rounded result!

# Input Format
<p>There are 3 lines of numeric input:</p>
<p>The first line has a double, <em>mealCost</em> (the cost of the meal before tax and tip).</p>
<p>The second line has an integer, <em>tipPercent</em> (the percentage of <em>mealCost</em> being added as tip).</p>
<p>The third line has an integer, <em>taxPercent</em> (the percentage of <em>mealCost</em> being added as tax).</p>

# Output Format
Print the total meal cost, where <em>totalCost</em> is the rounded integer result of teh entire bill (<em>mealCost</em> with added tax and tip).

# Sample Input
<p><code>12.00</code></p>
<p><code>20</code></p>
<p><code>8</code></p>

# Sample Output
<code>15</code>

# Explanation
<p>Given:</p>
<p><em>mealCost</em> = 12, <em>tipPercent</em> = 20, <em>taxPercent</em> = 8</p>
<p>Calculations:</p>
<p><em>tip</em> = 12 x (20/100) = 2.4</p>
<p><em>tax</em> = 12 x (8/100) = 0.96</p>
<p><em>totalCost</em> = <em>mealCost</em> + <em>tip</em> + <em>tax</em> = 12 + 2.4 + 0.96 = 15.36</p>
<p><em>round(totalCost</em> = 15</p>
<p>we round <em>totalCost</em> to the nearest dollar (integer) and then print our result, 15.</p>