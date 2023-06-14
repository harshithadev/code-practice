import java.util.*;

public class ArrayListProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a;
        ArrayList<Integer> al = new ArrayList<Integer>();
        boolean loop = true;
        while(loop){
            a = sc.nextInt();
            if (a>=0)
                al.add(a);
            else
                loop = false;
        }
        sc.close();
        int n = al.size()-1;
        //System.out.println(n);
        for(int i=n;i>=0;i--)
            System.out.println(al.get(i));
        //System.out.println(al);
    }
}

/*
credits : InterviewBit - 
Problem Description

In Java, we need to declare the size of an array before we can use it. Once the size of an array is declared, it's hard to change it.

To handle this issue, we can use the ArrayList class. It allows us to create resizable arrays.

Unlike arrays, arraylists can automatically adjust its capacity when we add or remove elements from it. Hence, arraylists are also known as dynamic arrays

Syntax of Creating an ArrayList:

// create Integer type arraylist
ArrayList arrayList = new ArrayList<>()
In the above program, we have used Integer not int. It is because we cannot use primitive types while creating an arraylist. Instead, we have to use the corresponding wrapper classes.

Basic syntax:

ArrayListName.size() : use this to get the size of arraylist.
ArrayListName.add(x) : Use this to append an element x to the ArrayList.
ArrayListName.get(i) : use this to access the ith index element in the ArrayList. Remember ArrayList uses 0 based indexing.
To read more about ArrayList click here

Task:

You are given a stream of positive integers as input and the stream ends when you encounter an negative element.

You need to save this numbers in an ArrayList and then print this numbers in reverse order.

NOTE: See example input/output for further understanding



Input Format

Input contains of several lines where each line contain a single integer denoting the stream of integers.


Output Format

Output the inputted stream in reverse format as space-separated integers in a single line.


Example Input

Input 1:

 11
 1
 2
 6
 0
 -2
Input 2:

 10
 2
 -1
Example Output

Explanation 1:

 0 6 2 1 11
Explanation 2:

 2 10
Example Explanation

Explanation 1:

 The inputted stream looks like: [11, 1, 2, 6, 0]
 We need to print the reverse of this.


 My Solution : 
 import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
        int a;
        ArrayList<Integer> al = new ArrayList<Integer>();
        boolean loop = true;
        while(loop){
            a = sc.nextInt();
            if (a>=0)
                al.add(a);
            else
                loop = false;
        }
        int n = al.size()-1;
        for(int i=n;i>=0;i--)
            System.out.print(al.get(i)+" ");
    }
}
*/