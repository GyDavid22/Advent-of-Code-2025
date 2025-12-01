import { readFileSync } from 'fs';

(() => {
    const input = readFileSync('input.txt', { encoding: 'utf-8' }).split('\n');
    let dial = 50;
    const DIAL_MAX = 100;
    let count = 0;
    for (const element of input) {
        const parsed = Number.parseInt(element.slice(1));
        if (element[0] === 'R') {
            for (let i = 0; i < parsed; i++) {
                dial++;
                if (dial === DIAL_MAX) {
                    count++;
                    dial = 0;
                }
            }
        } else if (element[0] === 'L') {
            for (let i = 0; i < parsed; i++) {
                dial--;
                if (dial === -1) {
                    dial = DIAL_MAX - 1;
                } else if (dial === 0) {
                    count++;
                }
            }
        }
    }
    console.log(count);
})();