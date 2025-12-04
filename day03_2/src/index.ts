import { readFileSync } from "fs";

(() => {
    const banks = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n').map((v) => v.trim());
    let sum = 0;
    for (const element of banks) {
        sum += Number.parseInt(getMax(12, element, 0));
    }
    console.log(sum);
})();

function getMax(charsLeft: number, joltages: string, bottom: number): string {
    if (charsLeft === 0) {
        return '';
    }

    let maxindex = bottom;
    for (let i = bottom; i < joltages.length; i++) {
        if (joltages[i] > joltages[maxindex] && joltages.length - i >= charsLeft) {
            maxindex = i;
        }
    }

    return joltages[maxindex].concat(getMax(charsLeft - 1, joltages, maxindex + 1));
}
