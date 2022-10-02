import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 비밀번호 발음하기 - 4659번
 */
public class Main {
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuffer sb = new StringBuffer();

        while(true) {

            int[] alpha = new int[26];
            boolean flag1 = true; boolean flag2 = true; boolean flag3 = true;

            String s = br.readLine();

            if(s.equals("end"))
                break;

            int cnt = 0;
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u')
                    cnt++;
            }

            if(cnt == 0) flag1 = false;

            int cntmoeum = 0;
            int cntjaeum = 0;
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u') {
                    cntjaeum = 0;
                    cntmoeum++;
                    if(cntmoeum == 3)  {
                        flag2 = false;
                        break;
                    }
                } else {
                    cntmoeum = 0;
                    cntjaeum++;
                    if(cntjaeum == 3) {
                        flag2 = false;
                        break;
                    }
                }
            }

            char idx = ' ';
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == idx) {
                    if(s.charAt(i) == 'e' || s.charAt(i) == 'o') {

                    } else{
                        flag1 = false;
                        break;
                    }
                }
                idx = s.charAt(i);
            }

            for(int i = 0; i < 26; i++) {
                if(alpha[i] == 2) {
                    flag3 = false;
                }
            }
            

            if(flag1 == true && flag2 == true && flag3 == true) {
                sb.append("<"+s+">"+" is acceptable.").append("\n");
            } else {
                sb.append("<"+s+">"+" is not acceptable.").append("\n");
            }
        }

        System.out.println(sb);

    }
}