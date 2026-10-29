function solution(m, n, puddles) {
    const dp = Array.from({length: n}, () => Array(m).fill(0));
    
    for (const [x, y] of puddles) {
        dp[y - 1][x - 1] = -1;
    }
    dp[0][0] = 1;
    
    for (let y = 0; y < n; y++) {
        for (let x = 0; x < m; x++) {
            if (dp[y][x] === -1) continue;
            if (x === 0 && y === 0) continue;
            const top = y > 0 && dp[y - 1][x] !== -1 ? dp[y - 1][x] : 0;
            const left = x > 0 && dp[y][x - 1] !== -1 ? dp[y][x - 1] : 0;
            dp[y][x] = (top + left) % 1000000007;
        }
    }
    return dp[n - 1][m - 1];
}