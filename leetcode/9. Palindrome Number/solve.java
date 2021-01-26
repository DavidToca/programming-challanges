class Solution {
    public boolean isPalindrome(int x) {
        String s1 = String.valueOf(x);
        StringBuilder builder = new StringBuilder();
        builder.append(s1);
        builder.reverse();
        return s1.equals(builder.toString());
    }
}