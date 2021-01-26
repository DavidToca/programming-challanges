class Solution {
    public int reverse(int x) {
        int MIN_INT = -2147483648;
        int MAX_INT = 2147483647;

        String a = String.valueOf(x);

        String sign = "";

        if(a.charAt(0) == '-'){
            sign = "-";
            a = a.substring(1);
        }
        StringBuilder builder = new StringBuilder();

        builder.append(a);
        builder.reverse();

        if(sign == "-"){
            builder.insert(0, sign);
        }

        Long response = Long.parseLong(builder.toString());

        if(response <= MAX_INT && response >= MIN_INT){
            return response.intValue();
        }
        else{
            return 0;
        }

    }
}