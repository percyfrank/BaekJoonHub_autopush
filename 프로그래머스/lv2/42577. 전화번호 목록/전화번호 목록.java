import java.util.*;

// 전화번호부 전체를 set에 입력
// set에 있는 전화번호가 다른 전화번호 길이만큼 
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashSet<String> set = new HashSet<>();
        
        for(String num : phone_book) {
            set.add(num);
            // System.out.println(num);
        }
        
        for(int i=0; i<phone_book.length; i++) {
            for(int j = 0; j<phone_book[i].length(); j++) {
                if(set.contains(phone_book[i].substring(0,j))) answer = false;
            }
        }
    
        
        
        return answer;
    }
}