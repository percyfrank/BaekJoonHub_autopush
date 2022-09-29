import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringBuffer sb = new StringBuffer();

        while(true) {

            String s = br.readLine();

            if(s.equals("END")) {
                break;
            }
            StringBuffer reverse = new StringBuffer(s).reverse();
            sb.append(reverse).append("\n");

        }
        System.out.println(sb);
    }
}