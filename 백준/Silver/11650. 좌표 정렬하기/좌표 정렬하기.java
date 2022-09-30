import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 좌표 정렬하기 - 11650
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] coord = new int[N][2];


        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            coord[i][0] = Integer.parseInt(st.nextToken());
            coord[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(coord, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if(a[0] == b[0]) {
                    return a[1] - b[1];
                } else {
                    return a[0] - b[0];
                }
            }
        });

        for(int j = 0; j < N; j++) {
            System.out.printf(coord[j][0]+ " " + coord[j][1]);
            System.out.println();
        }

    }
}