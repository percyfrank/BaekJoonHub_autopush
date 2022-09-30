import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 이 구역의 승자는 누구야? - 20154
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = {3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1};

        String s = br.readLine();

        int[] arrcnt = new int[s.length()];
        for(int i = 0 ; i < s.length();i++) {
            for(int j = 0; j < arr.length; j++) {
                if(s.charAt(i) == ((char)(j+'A'))) {
                    arrcnt[i] = arr[j];
                }
            }
        }

        int sum = 0;
        for(int i = 0; i < arrcnt.length; i ++){
            sum += arrcnt[i];
            if(sum > 10) {
                sum %= 10;
            }
        }

        System.out.println(sum % 2 == 1 ? "I'm a winner!" : "You're the winner?");

    }
}