const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const N = Number(input[0]);
const cost = input.slice(1).map(line => line.split(" ").map(Number));

const dp = Array.from({ length: N }, () => Array(1 << N).fill(-1));
// dp[1][0101] 현재 1에서 0,2 방문한 상태일 때 남은 도시 돌고 돌아가는 최소 비용

function tps(cur, visited) {
  // 이미 방문한 적이 있다면 재사용
  if (dp[cur][visited] !== -1) {
    return dp[cur][visited];
  }

  if (visited === (1 << N) - 1) {
    return cost[cur][0] !== 0 ? cost[cur][0] : Infinity;
  }

  let min = Infinity;

  for (let next = 0; next < N; next++) {
    if (cost[cur][next] === 0) continue;
    if (visited & (1 << next)) continue;
    // visited = 0101, next=2 (1 << 2) => 0100 => 0101 & 0100 = 1 이미 방문했으므로 제외

    const nextVisited = visited | (1 << next);
    // visited = 0101, next=1 (1 << 1) => 0010 => 0101 | 0010 = 0111

    min = Math.min(min, cost[cur][next] + tps(next, nextVisited));
    // 1에서 2가는 비용 + 2에서 끝까지가는 비용 최솟값
  }

  dp[cur][visited] = min;
  return min;
}

console.log(tps(0, 1));