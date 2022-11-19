import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 기타 레슨 - 2343번
 */
public class Main {

    static int N;
    static int M;
    static StringTokenizer st;
    static int[] arr;   // 1 2 3 4 5 6 7 8 9

    public static void solve() {

        int start = 0;
        int end = 0;
        for (int i : arr) {
            start = Math.max(start, i);     // 9
            end += i;                       // 45
        }

        while(start <= end) {
            int mid = (start + end) / 2; // 27

            int sum = 0;
            int cnt = 1;
            for (int i = 0; i < N; i++) {
                if(sum + arr[i] > mid) {
                    sum = 0;
                    cnt++;
                }
                sum += arr[i];
            }
            if(cnt > M) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        System.out.println(start);
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        solve();
    }
}