/* Question : 

This problem was asked by Alibaba.
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.

Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d.

*/

import java.util.*;

class GoldbabgsConjecture {
    static boolean checkForPrime(int inputNumber)
    {
    boolean isItPrime = true;
        if(inputNumber <= 1) {
            isItPrime = false;
            return isItPrime;
        }
        else{
            for (int i = 2; i<= inputNumber/2; i++) {
            if ((inputNumber % i) == 0){
                isItPrime = false;
                break;
                }
            }
            return isItPrime;
        }
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int no = sc.nextInt();
            for(int i=1; i<no/2; i++){
                if(checkForPrime(i)){
                    if(checkForPrime(no-i)){
                        System.out.println(i+" "+(no-i));
                        break;
                    }
                }
            }
        sc.close();
    }
}


// I copy pasted the prime number program from the internet, shouldnt have, next time I am coding on my own.