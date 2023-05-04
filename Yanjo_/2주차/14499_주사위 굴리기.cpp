/*
문제
크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 

  2
4 1 3
  5
  6
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

입력
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

출력
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

예제 입력 1 
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
예제 출력 1 
0
0
3
0
0
8
6
3
예제 입력 2 
3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3
예제 출력 2 
0
0
0
3
0
1
0
6
0
예제 입력 3 
2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
예제 출력 3 
0
0
0
0
예제 입력 4 
3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2
예제 출력 4 
0
0
0
6
0
8
0
2
0
8
0
2
0
8
0
2
*/

#include  <iostream>
#include <vector>
using namespace std;

struct DIR {
    int y, x;
    DIR(int _y, int _x): y(_y), x(_x) {};
};

DIR dir[4] = {
    DIR(0, 1), //R
    DIR(0, -1), // L
    DIR(-1, 0), //U
    DIR(1, 0) //D
};

int main() {
    int N, M, r, c, K;
    DIR now(0, 0);

    cin >> N >> M >> r >> c >> K;
    now.y = r; now.x = c;
    vector<vector<int> > dice(4, vector<int>(3, 0)), map(N, vector<int>(M, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) cin >> map[i][j];
    }

    for (int i = 0; i < K; i++) {
        int op;

        cin >> op;
        DIR d = dir[op - 1]; // 방향 setting
        DIR next(now.y + d.y, now.x + d.x);

        if ((next.y >= 0 && next.y < N) && (next.x >= 0 && next.x < M)) {
            if (op == 1) { // 동(R)
                int t0 = dice[1][0], t1 = dice[1][1], t2 = dice[1][2], f1 = dice[3][1];

                dice[1][0] = f1; dice[1][1] = t0; dice[1][2] = t1; dice[3][1] = t2;
            }
            else if (op == 2) { // 서(L)
                int t0 = dice[1][0], t1 = dice[1][1], t2 = dice[1][2], f1 = dice[3][1];

                dice[1][0] = t1; dice[1][1] = t2; dice[1][2] = f1; dice[3][1] = t0;
            }
            else if (op == 3) { // 북(U)
                int o1 = dice[0][1], t1 =dice[1][1], th1 = dice[2][1], f1 = dice[3][1];

                dice[0][1] = t1; dice[1][1] = th1; dice[2][1] = f1; dice[3][1] = o1;
            }
            else {// 남(D)
                int o1 = dice[0][1], t1 =dice[1][1], th1 = dice[2][1], f1 = dice[3][1];

                dice[0][1] = f1; dice[1][1] = o1; dice[2][1] = t1; dice[3][1] = th1;
            }

            cout << dice[1][1] << endl;
            if (map[next.y][next.x] == 0) map[next.y][next.x] = dice[3][1];
            else {
                dice[3][1] = map[next.y][next.x];
                map[next.y][next.x] = 0;
            }

            now.y = next.y; now.x = next.x;
        }
    }
}