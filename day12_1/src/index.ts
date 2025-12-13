// very naive solution, but apparently, it works

import { readFileSync } from "fs";

(() => {
    const input = parseInput();
    let count = 0;
    for (const element of input.trees) {
        const fullSize = element.size.x * element.size.y;
        let presentsSize = 0;
        for (let i = 0; i < element.presents.length; i++) {
            presentsSize += element.presents[i] * input.shapes[i].size;
        }
        if (presentsSize <= fullSize) {
            count++;
        }
    }
    console.log(count);
})();

function parseInput() {
    const data = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n').map((v) => v.trim());
    let i = 0;
    let isReadingShape = false;
    let isReadingTree = false;
    let currentShape: { size: number, pattern: Array<Array<boolean>>; } = { size: 0, pattern: [] };
    const shapes: (typeof currentShape)[] = [];
    const trees: {
        size: { x: number, y: number; },
        presents: number[];
    }[] = [];
    for (const element of data) {
        if (!isReadingShape && !isReadingTree && element === `${i}:`) {
            isReadingShape = true;
            continue;
        }
        if (isReadingShape && !isReadingTree && element === '') {
            isReadingShape = false;
            shapes.push(currentShape);
            currentShape = { size: 0, pattern: [] };
            i++;
            continue;
        }
        if (isReadingShape) {
            const line: Array<boolean> = [];
            for (const j of element) {
                if (j === '#') {
                    line.push(true);
                    currentShape.size++;
                } else {
                    line.push(false);
                }
            }
            currentShape.pattern.push(line);
        }
        if (!isReadingTree && !isReadingShape && element !== '') {
            isReadingTree = true;
        }
        if (isReadingTree) {
            const split = element.split(': ');
            const [x, y] = split[0].split('x').map((v) => Number.parseInt(v));
            const presents = split[1].split(' ').map((v) => Number.parseInt(v));
            trees.push({ size: { x, y }, presents });
        }
    }
    return {
        shapes,
        trees
    };
}