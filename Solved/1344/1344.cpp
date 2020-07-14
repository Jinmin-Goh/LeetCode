// Problem No.: 1344
// Solver:      Jinmin Goh
// Date:        20200715
// URL: https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution {
public:
    double angleClock(int hour, int minutes) {
        float ans, minDeg, hDeg;
        hour = hour % 12;
        hDeg = hour * 30.0 + 0.5 * minutes;
        minDeg = 6.0 * minutes;
        ans = fabs(minDeg - hDeg);
        if(ans > 180){
            ans = 360 - ans;
        }
        return ans;
    }
};