import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
       
        HashMap<String, Integer> map = new HashMap<>();
        
        // 장르별 재생 횟수 누적
        for(int i=0; i<genres.length;i++) {
            map.put(genres[i],map.getOrDefault(genres[i],0)+plays[i]);
        }
        
        // 장르 리스트에 넣기
        List<String> list = new ArrayList<>();
        for(String key : map.keySet()) {
            list.add(key);
        }
        
        // 장르별 재생횟수 내림차순으로 정렬
        Collections.sort(list,(o1,o2) -> map.get(o2)-map.get(o1));
        
        
        List<Integer> resultList = new ArrayList<>();
        
        // 이중 for문하면 천만
        for(int i=0;i<list.size();i++) {
            
            String genre = list.get(i);
            // System.out.println(genre);
            
            // 재생 가장 많이 된 노래 인덱스 찾기
            int max = 0;
            int first = -1;
            for(int j=0;j<genres.length;j++) {
                if(genre.equals(genres[j]) && plays[j] > max) {
                    max = plays[j];
                    first = j;
                }
            }
            
            // System.out.println(first);
            
            // 재생 두번째로 가장 많이 된 노래 인덱스 찾기
            max = 0;
            int second = -1;
            for(int j=0;j<genres.length;j++) {
                if(genre.equals(genres[j]) && plays[j] > max && j != first) {
                    max = plays[j];
                    second = j;
                }
            }
            // System.out.println(second);
            
            resultList.add(first);
            
            // 장르에 속한 곡이 하나일수도 있음
            if(second!=-1) resultList.add(second);
            
        }
        
        int[] answer = new int[resultList.size()];
        for(int i=0;i<answer.length;i++) {
            answer[i] = resultList.get(i);
        }
        
        System.out.println(Arrays.toString(answer));
        
        return answer;
    }
}