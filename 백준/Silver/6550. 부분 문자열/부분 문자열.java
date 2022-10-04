import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 부분 문자열 - 6550번
 */
public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = "";
        StringBuffer sb = new StringBuffer();
        while ((str = br.readLine()) != null) {

            String[] arr = str.split(" ");
            String s = arr[0];
            String t = arr[1];
//            StringTokenizer st = new StringTokenizer(str);
//            String s = st.nextToken();
//            String t = st.nextToken();

            int idx = 0;
            for(int i = 0; i < t.length(); i++) {
                if(s.charAt(idx) == t.charAt(i)) {
                    idx++;
                }
                if(idx == s.length()) {
                    break;
                }
            }

            if(idx == s.length()) {
                sb.append("Yes").append("\n");
            } else {
                sb.append("No").append("\n");
            }
        }
        System.out.println(sb);
    }
}