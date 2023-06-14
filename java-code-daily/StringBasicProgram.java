/*
Problem Description

"A string is traditionally a sequence of characters, either as a literal constant or as some kind of variable." — Wikipedia: String (computer science)

This exercise is to test your understanding of Java Strings. A sample String declaration:

String myString = "Hello World!"

The elements of a String are called characters. The number of characters in a string is called the length, and it can be retrieved with the String.length() method.

Some important methods for Strings in Java:

stringName.charAt(index) : returns char value for the particular index
stringName.isEmpty() : checks if string is empty.(Return type boolean).
Learn more about strings and its methods by clicking here.

Task:

Given two strings of lowercase English letters, A  and B, perform the following operations:

Sum the lengths of A and B.
Determine if A is lexicographically larger than B (i.e.: does B come before A in the dictionary?).
Capitalize the complete string A and B and print them on a single line, separated by a space.

Input Format

The first line contains string A. The second line contains another string B. The strings are comprised of only lowercase English letters.


Output Format

There are three lines of output:

For the first line, sum the lengths of A and B.

For the second line, write Yes if A is lexicographically greater than B otherwise print No instead.

For the third line, Capitalize the complete string A and B and print them on a single line, separated by a space.


Example Input

Input 1:

 abc
 def


Example Output

Output 1:

 6
 No
 ABC DEF
*/

import java.util.*;

public class StringBasicProgram {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
        String a,b;
        a = sc.nextLine();
        b = sc.nextLine();
        sc.close();
        System.out.println(a.length()+b.length());
        //int n = Math.min(a.length(), b.length());
    
        if (a.compareTo(b)>0 )
            System.out.println("Yes");
        else 
            System.out.println("No");
        System.out.println(a.toUpperCase()+" "+b.toUpperCase());
        sc.close();
    }
}


// ----------TIPS FOR MY FUTURE SELF (JUST IN CASE I POP BY TO REVISE)------------------------
// Check out as many String functions as possible, make it a habit to see if the method already exists, 
//coz there is no point in coding a logic that is a pre-existing method.
// 
//---------------------------------------------------------------------------------------------

