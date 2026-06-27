# Analisis y diseño de algoritmos
Intergrantes: 
- Daniel Bolivar
- Jeremy Astaiza

## Ejecutar ejercicios:
```
# para ejecutar el ejercicio 1 correr:
python3 exercise1/main.py 

# para ejecutar el ejercicio 2 correr:
python3 exercise2/main.py 
```

# Soluciones
En las carpetas contenidas en este repositorio se encuentra cada una de las soluciones de los ejercicios.

## Enunciados ejercicios

### Ejercicio 1
Link: https://www.hackerrank.com/challenges/countingsort4/problem

Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

Design your counting sort to be stable.

**Example**

The first two strings are replaced with '-'. Since the maximum associated integer is , set up a helper array with at least two empty arrays as elements. The following shows the insertions into an array of three empty arrays.

i	string	converted	list
0				[[],[],[]]
1 	a 	-		[[-],[],[]]
2	b	-		[[-],[-],[]]
3	c			[[-,c],[-],[]]
4	d			[[-,c],[-,d],[]]
The result is then printed:  .

**Function Description**

Complete the countSort function in the editor below. It should construct and print the sorted strings.

countSort has the following parameter(s):

string arr[n][2]: each arr[i] is comprised of two strings, x and s
Returns
- Print the finished array with each element separated by a single space.

**Note:** The first element of each , , must be cast as an integer to perform the sort.

**Input Format**

The first line contains , the number of integer/string pairs in the array .
Each of the next  contains  and , the integers (as strings) with their associated strings.

**Constraints**
```
  1<= n <= 1000000
  n is even
  1<= |s| <= 10
  0 <= x <= 100, x pertenece ar

  s[i] consists of characters in the range ascii [a-z]

```

**Output Format**

Print the strings in their correct order, space-separated on one line.

**Sample Input**
```
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the
```
**Sample Output**
```
- - - - - to be or not to be - that is the question - - - -
```

**Explanation**

The correct order is shown below. In the array at the bottom, strings from the first half of the original array were replaced with dashes.
```
0 ab
0 ef
0 ab
0 ef
0 ij
0 to
1 be
1 or
2 not
2 to
3 be
4 ij
4 that
4 is
4 the
5 question
6 cd
6 gh
6 cd
6 gh
```
```
sorted = [['-', '-', '-', '-', '-', 'to'], ['be', 'or'], ['not', 'to'], ['be'], ['-', 'that', 'is', 'the'], ['question'], ['-', '-', '-', '-'], [], [], [], []]
```

### Ejercicio 2
Link: https://www.hackerrank.com/challenges/stockmax/problem

Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next number of days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

**Example**

prices = [1, 2]

Buy one share day one, and sell it day two for a profit of 1. Return 1.

prices = [2, 1]

No profit can be made so you do not buy or sell stock those days. Return 0.

**Function Description**

Complete the stockmax function in the editor below.

stockmax has the following parameter(s):
- prices: an array of integers that represent predicted daily stock prices

**Returns**
- int: the maximum profit achievable

**Input Format**

The first line contains the number of test cases t.

Each of the next t pairs of lines contain:
- The first line contains an integer n, the number of predicted prices for WOT.
- The next line contains n space-separated integers prices[i], each a predicted stock price for day i.

**Constraints**
```
  1 <= t <= 10
  1 <= n <= 50000
  1 <= prices[i] <= 100000
```

**Output Format**

Output t lines, each containing the maximum profit which can be obtained for the corresponding test case.

**Sample Input**
```
STDIN          Function
-----          --------
3              q = 3
3              prices[] size n = 3
5 3 2          prices = [5, 3, 2]
3              prices[] size n = 3
1 2 100        prices = [1, 2, 100]
4              prices[] size n = 4
1 3 1 2        prices = [1, 3, 1, 2]
```

**Sample Output**
```
0
197
3
```

**Explanation**

For the first case, there is no profit because the share price never rises, return 0.

For the second case, buy one share on the first two days and sell both of them on the third day for a profit of 197.

For the third case, buy one share on day 1, sell one on day 2, buy one share on day 3, and sell one share on day 4. The overall profit is 3.