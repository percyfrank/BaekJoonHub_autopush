import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 배열 합치기 - 11728번
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        
        int[] arr = new int[N + M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int j = N; j < N + M; j++) {
            arr[j] = Integer.parseInt(st.nextToken());

        }

        Arrays.sort(arr);
        StringBuffer sb = new StringBuffer();
        for(int i : arr) {
            sb.append(i).append(" ");
        }
        System.out.println(sb);
    }
}