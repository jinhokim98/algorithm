const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");
const [N, ...rest] = input;

const n = Number(N);
const coordinate = rest.map((line) => line.split(' ').map(Number));
const calculateDistance = (x1, x2, y1, y2) => Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));

const dp = Array.from({ length: n }, () => Array(1 << n).fill(-1));

const tsp = (cur, visited) => {
  // -1이 아니면 최적이니깐 그거 가져다 사용해
  if (dp[cur][visited] !== -1) {
    return dp[cur][visited];
  }
  
  // 방문 다 했다면 처음으로 되돌아가기
  if (visited === (1 << n) - 1) {
    const [x1, y1] = coordinate[cur];
    const [x2, y2] = coordinate[0];
    
    const dist = calculateDistance(x1, x2, y1, y2);
    return dist;
  }
  
  let min = Infinity
  
  for (let next = 0; next < n; next++) {
    if (visited & (1 << next)) continue; // 방문한 곳 다시 방문하지 않음
    const nextVisited = visited | (1 << next);
    const [x1, y1] = coordinate[cur];
    const [x2, y2] = coordinate[next];
    const dist = calculateDistance(x1, x2, y1, y2);
    
    min = Math.min(min, dist + tsp(next, nextVisited))
  }
  
  dp[cur][visited] = min;
  return min
}

console.log(tsp(0, 1))