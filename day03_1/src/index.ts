import { readFileSync } from "fs";

interface IPlaces {
    value: string,
    place: number,
};

(() => {
    const banks = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n');
    let sum = 0;
    for (const element of banks) {
        let highest: IPlaces = { value: element[0], place: 0 };
        let secondHighest = highest;
        for (let i = 0; i < element.length; i++) {
            if (element[i] > highest.value) {
                highest = { value: element[i], place: i };
            }
        }
        if (highest.place === element.length - 1) {
            for (let i = 0; i < highest.place; i++) {
                if (element[i] > secondHighest.value) {
                    secondHighest = { value: element[i], place: i };
                }
            }
        } else {
            secondHighest = { value: element[highest.place + 1], place: highest.place + 1 };
            for (let i = highest.place + 1; i < element.length; i++) {
                if (element[i] > secondHighest.value) {
                    secondHighest = { value: element[i], place: i };
                }
            }
        }
        const joltage = ''.concat(...([highest, secondHighest].sort((a, b) => a.place - b.place).map((v) => v.value)));
        sum += Number.parseInt(joltage);
    }
    console.log(sum);
})();