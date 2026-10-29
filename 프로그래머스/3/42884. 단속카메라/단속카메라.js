function solution(routes) {
    routes.sort((a, b) => a[1] - b[1]);
    let answer = 0;
    let index = 0;
    
    while (index < routes.length) {
        const start = routes[index][0];
        const end = routes[index][1];
        
        while (index + 1 < routes.length && end >= routes[index + 1][0]) {
            index++;
        }
        answer++;
        index++;
    }
    return answer;
}
