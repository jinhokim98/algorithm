function solution(n, costs) {
    const graph = Array.from({length: n}, () => []);
    costs.forEach(([start, end, cost]) => {
        graph[start].push([end, cost]);
        graph[end].push([start, cost]);
    });
    
    // 1. 간선 정렬
    costs.sort((a, b) => a[2] - b[2]);
    // 2. 유니온파인드 초기화
    const parent = Array.from({length: n}).map((_, index) => index);
    const mst = [];
    let totalCost = 0;
    
    for (const [u, v, cost] of costs) {
        if (find(parent, u) !== find(parent, v)) {
            union(parent, u, v);
            mst.push([u, v, cost]);
            totalCost += cost;
        }
    }
    
    return totalCost;
}


const find = (parent, x) => {
    if (parent[x] !== x) {
        parent[x] = find(parent, parent[x]);
    }
    
    return parent[x];
}

const union = (parent, a, b) => {
    const rootA = find(parent, a);
    const rootB = find(parent, b);
    if (rootA !== rootB) {
        parent[rootB] = rootA;
    }
}