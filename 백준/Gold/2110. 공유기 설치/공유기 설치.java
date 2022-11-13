import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 공유기 설치 - 2110번
 */
public class Main {
    static int N;
    static int C;
    static int[] coord;
    static StringTokenizer st;

    public static void solve(){
        Arrays.sort(coord);
        int start = 1;
        int end = coord[N-1] - coord[0];

        while(true) {
            if(start > end) {
                System.out.println(end);
                break;
            }

            int mid = (start + end) / 2;
            int idx = coord[0];
            int cnt = 1;

            for (int i = 1; i <= N-1; i++) {
                if(coord[i] - idx >= mid) {
                    cnt++;
                    idx = coord[i];
                }
            }
            // 공유기 설치 갯수보다 적은 경우 -> 공유기 간격을 줄인다.
            if(cnt < C) {
                end = mid - 1;
            }
            // 공유기 설치 갯수보다 크거나 같은 경우 -> 공유기 간격을 늘린다.
            else {
                start = mid + 1;
            }
        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        coord = new int[N];
        for (int i = 0; i < N; i++) {
            coord[i] = Integer.parseInt(br.readLine());
        }
        solve();
    }
}
