/*
import java.util.*;

public class StackProgram {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc  = new Scanner(System.in);
        String A;
        Stack<Integer> st = new Stack<Integer>();
        int n = sc.nextInt();
        sc.nextLine();
        int[] result = new int[n];
        for (int j=0; j<n; j++){

            A = sc.nextLine();
            for(int i=0; i<A.length(); i++)
            {
                if(A.charAt(i)=='(')
                st.push(1);
                else
                st.pop();
            }
            if(st.empty())
             result[j]=1;
            else 
            result[j]=0;
        }
        sc.close();
        for (int i = 0; i<n; i++)
        System.out.println(result[i]);
    }
}

*/

//import java.lang.*;
import java.util.*;
class StackProgram {
    public static int balance(String A){
        Stack<Integer> st = new Stack<Integer>();
        for(int i=0; i<A.length(); i++)
            {
                if(A.charAt(i)=='('){
                    st.push(1);
                    continue;
                }

                    if(st.empty()){
                        return -1;
                    }
                    else
                        st.pop(); 
            }
        if(st.empty())
            return 1;
        else 
            return -1;
    }
}
   /* public static void StackProgram(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc  = new Scanner(System.in);
        String A;
        int n = sc.nextInt();
        sc.nextLine();
        int[] result = new int[n];
        for (int j=0; j<n; j++){

            A = sc.nextLine();
            int r = balance(A);
            if(r == 1)
             result[j]=1;
            else 
            result[j]=0;
        }
        sc.close();
        for (int i = 0; i<n; i++)
        System.out.println(result[i]);
        sc.close();
    }
}

// ----------TIPS FOR MY FUTURE SELF (JUST IN CASE I POP BY TO REVISE)------------------------
//the commented program does not work well for all test cases 
// comment the logical error, in case you find it.
// lesson I learnt while doing this - Always use abstraction !!!


// Also note that I added a nextLine() after using nextInt() that is because nextInt does not 
// go to the next line when it encounters '\n' therefore I added a nextLine() 
// to know more about stack data structure check out - https://docs.oracle.com/javase/7/docs/api/java/util/Stack.html#Stack()
//---------------------------------------------------------------------------------------------



*/

//Meanwhile check out the other data structures in Java as well!!!
/*
1D Array	Medium	16 minutes	
MultiDimensional Arrays	
ArrayList	
Stacks
Queues	
Deque	
PriorityQueue	
PriorityQueue Comparator
Classes	
*/