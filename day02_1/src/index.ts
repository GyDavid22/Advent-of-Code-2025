import { readFileSync } from "fs";

(() => {
    const ranges = readFileSync('input.txt', { encoding: 'utf-8' })
        .trim()
        .split(',')
        .map((val) => val.split('-'));
    let sum = 0;
    for (const element of ranges) {
        const bottom = Number.parseInt(element[0]);
        const top = Number.parseInt(element[1]);
        for (let i = bottom; i <= top; i++) {
            const asString = i.toString();
            const half = Math.floor(asString.length / 2);
            if (asString.slice(0, half) === asString.slice(half)) {
                sum += i;
            }
        }
    }
    console.log(sum);
})();