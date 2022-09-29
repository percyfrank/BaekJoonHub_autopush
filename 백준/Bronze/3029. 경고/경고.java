import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] now =  br.readLine().split(":");
        String[] throwtime =  br.readLine().split(":");

        int[] arr = new int[3];

        for(int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(throwtime[i]) - Integer.parseInt(now[i]);
        }

        if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
            arr[0] = 24;
            arr[1] = 0;
            arr[2] = 0;
        }

        if(arr[2] < 0){
            arr[1]--;
            arr[2] += 60;
        }

        if(arr[1] < 0) {
            arr[0]--;
            arr[1] += 60;
        }

        if(arr[0] < 0) {
            arr[0] += 24;
        }

        System.out.printf("%02d:%02d:%02d",arr[0],arr[1],arr[2]);

    }
}