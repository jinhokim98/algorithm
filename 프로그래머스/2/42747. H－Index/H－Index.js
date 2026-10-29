function solution(citations) {
    const list = citations.sort((a, b) => b - a);
    let answer = 0;
    
    for (let i = 0; i < list.length; i++) {
        if (list[i] > i) {
            answer += 1;
        }
    }
    
    return answer;
}