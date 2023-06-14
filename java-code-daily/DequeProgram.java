//import java.lang.*;
import java.util.*;

public class DequeProgram {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Deque<Integer> Q = new ArrayDeque<Integer>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x, y;
        sc.nextLine();
        while(n-->0){
            x = sc.nextInt();
            y = sc.nextInt();
            sc.nextLine();
            switch(x){
                case 1:
                {
                    Q.offerLast(y);
                }
                break;
                case 2:
                {
                    Q.offerFirst(y);
                }
                break;
                case 3:
                {
                    if(Q.size()!=0)
                        System.out.println(Q.peekFirst());
                    else 
                        System.out.println(-1);
                }
                break;
                case 4:
                {
                    if(Q.size()!=0)
                        System.out.println(Q.peekLast());
                    else 
                        System.out.println(-1);
                }
                break;
                case 5:
                {
                    if(Q.peekLast()!=null)
                        Q.pollFirst();
                }
                break;
                case 6:
                {
                    if(Q.peekLast()!=null)
                        Q.pollLast();
                }
                break;
                default: 
                break;
            }
        }
        sc.close();
    }
}

// ----------TIPS FOR MY FUTURE SELF (JUST IN CASE I POP BY TO REVISE)------------------------
//what I learned from this is that - there are so many classes, interfaces and collections available 
//ready to use. We must familarise ourselves with them and get to know their basic methods and attributes.
// Also, read the question patiently, dont assume stuff, coz when you preassume and code, you'll waste 
//a lot of time trying to figure out where you went wrong.
//----------------------------------------------------------------------------------------------



/*
Problem Description

The Deque interface of the Java collections framework provides the functionality of a double-ended queue. It extends the Queue interface.

Classes that Implement Deque:

In order to use the functionalities of the Deque interface, we need to use classes that implement it:

ArrayDeque
LinkedList
In a regular queue, elements are added from the rear and removed from the front. However, in a deque, we can insert and remove elements from both front and rear.

In Java, we must import the java.util.Deque package to use Deque.

Syntax:

Deque<String> names= new ArrayDeque<>();

Tha above statement creates a Deque of Strings, we can now push and remove Strings from this deque easily.

Methods of Deque:

addFirst() - Adds the specified element at the beginning of the deque. Throws an exception if the deque is full.
addLast() - Adds the specified element at the end of the deque. Throws an exception if the deque is full.
offerFirst() - Adds the specified element at the beginning of the deque. Returns false if the deque is full.
offerLast() - Adds the specified element at the end of the deque. Returns false if the deque is full.
getFirst() - Returns the first element of the deque. Throws an exception if the deque is empty.
getLast() - Returns the last element of the deque. Throws an exception if the deque is empty.
peekFirst() - Returns the first element of the deque. Returns null if the deque is empty.
peekLast() - Returns the last element of the deque. Returns null if the deque is empty.
removeFirst() - Returns and removes the first element of the deque. Throws an exception if the deque is empty.
removeLast() - Returns and removes the last element of the deque. Throws an exception if the deque is empty.
pollFirst() - Returns and removes the first element of the deque. Returns null if the deque is empty.
pollLast() - Returns and removes the last element of the deque. Returns null if the deque is empty.
size() - Return an integer denoting the total number of elements in the deque at present.
Task:

Complete the code given below.

You need to answer Q queries, in each query you are given two integers x and y:

if x = 1 then push the integer y to the back of the deque.
if x =2 then push the integer y to the front of the deque.
if x = 3 then return the front element of the deque if the deque is not empty else return -1
if x = 4 then return the last element of the deque if the deque is not empty else return -1
if x = 5 then remove the front element from the deque if the deque is not empty else do nothing. No need to return anything in this query.
if x = 6 then remove the last element from the deque if the deque is not empty else do nothing. No need to return anything in this query.
 


Problem Constraints

1 <= Q <= 100

1 <= x <= 6

1 <= y <= 100


Input Format

First line of input contains a single integer Q.

Next Q lines each contain two integers x and y for that query.

 

Output Format

For each query in which x = 3 or x = 4 print its answer in separate lines.


Example Input

Input 1:

 7
 2 1
 1 5
 3 -1
 4 -1
 5 -1
 6 -1
 3 -1

Example Output

Output 1:

 1
 5
 -1


Example Explanation

Explanation 1:

 Query 1: x = 2 so we need to push y i.e 1 to the front of the deque so deque = [1]
 Query 2: x = 1 so we need to push y i.e 5 to the back of the deque so deque = [1, 5]
 Query 3: x = 3 so we need to print the front element of the deque i.e 1
 Query 4: x = 4 so we need to print the last element of the deque i.e 5
 Query 5: x = 5 so we need to remove the front element of the deque so deque = [5]
 Query 6: x = 6 so we need to remove the last element of the deque so deque = []
 Query 7: x = 3 so we need to print the front element of the deque but as the deque is empty so we will print -1. 
*/