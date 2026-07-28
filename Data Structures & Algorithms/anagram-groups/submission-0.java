class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // create a list of list of strings
        // loop through string array
        // sort copy of string into ascending order
        // if exists add unsorted string to hashmap(sorted string, list of strings)
        // otherwise create new sorted string key and unsorted value
        // once loop finishs, loop through the map and add each list of strings to the list of list of strings

        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            map.computeIfAbsent(sorted, k -> new ArrayList<>()).add(strs[i]);
        }

       
        return new ArrayList<>(map.values());
    }
}
