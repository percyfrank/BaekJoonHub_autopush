import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 숫자 갯수, 배열
        int N = Integer.parseInt(br.readLine());

        String[] s = br.readLine().split("");

        int sum = 0;
        for(int i = 0; i < N; i++) {
            sum += Integer.parseInt(s[i]);
        }

        System.out.println(sum);
    }
}