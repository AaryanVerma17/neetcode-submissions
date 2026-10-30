class Solution {
    public boolean isAnagram(String s, String t) {
        // If lengths do not match, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // Array to store frequencies of 26 lowercase English letters
        int[] charCounts = new int[26];

        // Increment counts for string s, decrement counts for string t
        for (int i = 0; i < s.length(); i++) {
            charCounts[s.charAt(i) - 'a']++;
            charCounts[t.charAt(i) - 'a']--;
        }

        // If all character frequencies balances out to zero, they are anagrams
        for (int count : charCounts) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}
