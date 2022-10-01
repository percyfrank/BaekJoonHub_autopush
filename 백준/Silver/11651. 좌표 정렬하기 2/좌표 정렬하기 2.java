import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 좌표 정렬하기 2 - 11651번
 */
public class Main {
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] coord = new int[N][2];

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            coord[i][0] = Integer.parseInt(st.nextToken());
            coord[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(coord, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {

                if(o1[1] == o2[1]) {
                    return o1[0] - o2[0];
                } else {
                    return o1[1] - o2[1];
                }
            }
        });

        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < N; i++) {
            sb.append(coord[i][0] + " " + coord[i][1]).append("\n");
        }

        System.out.println(sb);

    }
}