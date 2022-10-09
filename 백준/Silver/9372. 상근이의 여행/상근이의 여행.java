import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 상근이의 여행 - 9372번
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuffer sb = new StringBuffer();

        int T = Integer.parseInt(br.readLine());
        for(int i = 0 ; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            for(int j = 0; j < M; j++) {
                br.readLine();
            }
            sb.append((N-1) + "\n");
        }
        System.out.println(sb);

    }
}