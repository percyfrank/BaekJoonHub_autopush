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
        char[] chr = s.toCharArray();
        int sum = 0;

        for(int i = 0; i < chr.length; i++) {
            sum += arr[chr[i]-'A'];
        }

        if(sum > 10) {
            sum %= 10;
        }

        System.out.println(sum % 2 == 1 ? "I'm a winner!" : "You're the winner?");

    }
}