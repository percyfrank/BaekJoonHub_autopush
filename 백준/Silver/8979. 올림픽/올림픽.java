import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

/**
 * 올림픽 - 8979번
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] medal = new int[N][4];

        for (int i = 0; i < N; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            medal[i][0] = Integer.parseInt(st1.nextToken());
            medal[i][1] = Integer.parseInt(st1.nextToken());
            medal[i][2] = Integer.parseInt(st1.nextToken());
            medal[i][3] = Integer.parseInt(st1.nextToken());
        }

        Arrays.sort(medal, (a, b) -> {
            if (a[1] == b[1]) {
                if (a[2] == b[2]) {
                    return b[3] - a[3];
                } else {
                    return b[2] - a[2];
                }

            } else {
                return b[1] - a[1];
            }
        });

        HashMap<Integer, Integer> map = new HashMap<>();

        int start = 1;
        int cnt = 1;
        int idx = 1;
        map.put(medal[0][0],start);

        for (int i = 0; i < N - 1; i++) {
            if (medal[i][1] == medal[i + 1][1] && medal[i][2] == medal[i + 1][2] && medal[i][3] == medal[i + 1][3]) {
                map.put(medal[i+1][0],start);
                idx = start;
                cnt++;
            } else {
                map.put(medal[i+1][0],i+2);
                start = i+2;
                cnt = 1;
            }
        }

        for(int i : map.keySet()) {
            if(i == K) {
                System.out.println(map.get(i));
            }
        }

    }
}