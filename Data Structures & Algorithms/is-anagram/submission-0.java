class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charsS = s.toCharArray();
        char[] charsT = t.toCharArray();
        Arrays.sort(charsS);
        Arrays.sort(charsT);    
        String sortedS = new String(charsS);
        String sortedT = new String(charsT);
        if (sortedS.equals(sortedT)) {
            return true;
        }
        else {
            return false;
        }
    }
}
