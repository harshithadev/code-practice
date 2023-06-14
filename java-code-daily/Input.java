import java.util.*;
public class Input {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        //String[] str = sc.nextLine().split(" ");
        //System.out.println(str[0]+"\n"+str[1]);
        System.out.println(n1+"\n"+n2);
        sc.close();
    }
}

// ----------TIPS FOR MY FUTURE SELF (JUST IN CASE I POP BY TO REVISE)------------------------
//I believe that the first lesson in any programming language has to be it's input and output methods.
//Checkout Scanner class for various input methods. Some of them include... 
//nextInt(), next(), nextBool(), nextLine(), etc...
//https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html

//Also checkout BufferReader class, it takes less time when compared to Scanner class when inputing data.
//---------------------------------------------------------------------------------------------