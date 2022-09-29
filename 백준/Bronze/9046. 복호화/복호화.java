import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 9046 복호화
 */
public class Main {
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        int[] chart = new int[26];

        StringBuffer sb = new StringBuffer();

        for(int i = 0; i < T; i++) {

            String s = br.readLine();

            for (int j = 0; j < s.length(); j++) {
                // 테스트 케이스의 알파벳이 a ~ z 사이일 때만 해당
                // 테스트 케이스의 공백은 해당 안됨
                if (s.charAt(j) >= 'a' && s.charAt(j) <= 'z')
                    chart[s.charAt(j) - 'a']++;
            }

            int max = 0;   // 가장 많이 등장한 문자의 등장 횟수
            int cnt = 0;   // 가장 많이 등장한 문자의 갯수
            int idx = 0;   // 가장 많이 등장한 문자의 인덱스

            for (int k = 0; k < 26; k++) {
                max = Math.max(max, chart[k]);
            }

            for (int c = 0; c < 26; c++ ){
                if(max == chart[c]) {
                    idx = c;
                    cnt++;
                }
            }
            
            Arrays.fill(chart,0);

            if (cnt != 1) {
                sb.append("?").append("\n");
            } else {
                sb.append((char) (idx + 'a')).append("\n");
            }

        }
        System.out.println(sb);
    }
}