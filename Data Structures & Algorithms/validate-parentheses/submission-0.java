class Solution {
    public boolean isValid(String s) {
        if (!(s.toCharArray().length % 2 == 0)) {
            return false;
        }
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (!stack.isEmpty()) {
                char openBracket = stack.pop();
                if (openBracket == '(' && c == ')') {
                    continue;
                } else if (openBracket == '[' && c == ']') {
                    continue;
                } else if (openBracket == '{' && c == '}') {
                    continue;
                } else {
                    return false;
                }
            } else {
                return false;
            }

        }

        return stack.isEmpty();
    }
}
