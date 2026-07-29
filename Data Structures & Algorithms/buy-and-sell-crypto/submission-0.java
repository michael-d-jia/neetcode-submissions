class Solution {
    public int maxProfit(int[] prices) {
        int sell = 0;
        int buy = 1;
        int profit = 0;
        while (buy < prices.length) {
            if (prices[sell] < prices[buy]) {
                profit = Math.max(profit, prices[buy] - prices[sell]);
            } else {
                sell = buy;
            }
            buy++;
        }
        return profit;
    }
}
