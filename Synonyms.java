/* Question : 
You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?*/
import java.util.*;

class Synonyms{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        boolean flag = true;
        String[] words = sc.nextLine().split(" ");
        String[] words1 = sc.nextLine().split(" ");
        String[] words2 = sc.nextLine().split(" ");
        if(words1.length==words2.length){
            for(int i = 0; i<words1.length;i++){
                if(words1[i].equals(words2[i])){
                    flag = true;
                }
                else {
                if(words1[i].equals(words[0])||words1[i].equals(words[1])){
                    if(words2[i].equals(words[0])||words2[i].equals(words[1])){
                        flag = true;
                        continue;
                    }
                }
                    flag = false;
                    break;
                }
            }
        }
        else
            flag = false;
        System.out.println(flag);
        sc.close();
    }
}