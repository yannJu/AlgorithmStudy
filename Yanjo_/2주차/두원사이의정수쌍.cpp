#include <string>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    
    for (long i = 1; i <= r2; i++) {
        long r2Points = 0, r1Points = 0;
        
        r2Points += (long long)floor(sqrt(1.0 * r2 * r2 - 1.0 * i * i));
        if (i < r1) r1Points += (long long)ceil(sqrt(1.0 * r1 * r1 - 1.0 * i * i));
            
        answer += r2Points - r1Points + 1;
    }
    
    answer *= 4;
    return answer;
}