import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 카드 구매하기 2 - 16194번
 */
public class Main {

    static int[] dp;
    static int N;

    public static int card(int num) {
        dp[0] = 0;
        for (int i = 1; i <= num; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i-j] + dp[j]);
            }
        }
        return dp[num];
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            dp[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(card(N));
    }
}