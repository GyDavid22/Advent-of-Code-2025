import { readFileSync } from 'fs';

(() => {
    const input = readFileSync('input.txt', { encoding: 'utf-8' }).split('\n');
    let dial = 50;
    const DIAL_MAX = 100;
    let count = 0;
    for (const element of input) {
        if (element[0] === 'R') {
            dial = (dial + (Number.parseInt(element.slice(1)) % DIAL_MAX)) % DIAL_MAX;
        } else if (element[0] === 'L') {
            dial = dial - (Number.parseInt(element.slice(1)) % DIAL_MAX);
            if (dial < 0) {
                dial += DIAL_MAX;
            }
        }
        if (dial === 0) {
            count++;
        }
    }
    console.log(count);
})();