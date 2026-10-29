function solution(brown, yellow) {
    const divider = [];
    for (let i = 1; i <= yellow; i++) {
        if (yellow % i === 0) {
            divider.push(i);
        }
    }
    
    for (let i = 0; i < divider.length / 2; i++) {
        const left = divider[i];
        const right = divider[divider.length - 1 - i];
        
        const totalCarpet = (left + 2) * (right + 2);
        if (totalCarpet - yellow === brown) {
            return [right + 2, left + 2];
        }
    }
}