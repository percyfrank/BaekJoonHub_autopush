import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 세로읽기 - 10798
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuffer sb = new StringBuffer();

        char[][] arr = new char[5][15];

        for(int i = 0; i < 5; i++) {
            String s = br.readLine();
            for(int j = 0; j < s.length(); j++) {
                arr[i][j] = s.charAt(j);
            }
        }

        for(int i = 0; i < 15; i++) {
            for(int j = 0; j < 5; j++) {
                if(arr[j][i] == '\0') {
                   continue;
                } else {
                    sb.append(arr[j][i]);
                }
            }
        }
        System.out.println(sb);

    }
}