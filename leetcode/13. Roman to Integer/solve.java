class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> equivalence = new HashMap<Character, Integer>();
        
        equivalence.put('I', 1);
        equivalence.put('V', 5);
        equivalence.put('X', 10);
        equivalence.put('L', 50);
        equivalence.put('C', 100);
        equivalence.put('D', 500);
        equivalence.put('M', 1000);

        StringBuilder builder = new StringBuilder();

        builder.append(s);
        builder.reverse();

        s = new String(builder);

        int response = 0;
        int last_numb = -1;

        for (char ch: s.toCharArray()) {
            int roman = equivalence.get(ch);
            if(last_numb > roman){
                response -=roman;
            } else {
                response +=roman;
            }
            last_numb = roman;
        }

        return response;
    }
}