import { readFileSync } from "fs";

(() => {
    const data = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n');
    const nodes: { [x in string]: { node: string, connections: string[]; } } = {};
    for (const element of data) {
        const splitted = element.trim().split(': ');
        const newNode = { node: splitted[0], connections: splitted[1].split(' ') };
        nodes[newNode.node] = newNode;
    }
    nodes['out'] = { node: 'out', connections: [] };
    const res = dfs(nodes, nodes['svr'], 'fft', {}) * dfs(nodes, nodes['fft'], 'dac', {}) * dfs(nodes, nodes['dac'], 'out', {})
        + dfs(nodes, nodes['svr'], 'dac', {}) * dfs(nodes, nodes['dac'], 'fft', {}) * dfs(nodes, nodes['fft'], 'out', {});
    console.log(res);
})();

function dfs(allNodes: { [x in string]: { node: string, connections: string[]; } }, currentNode: { node: string, connections: string[]; }, goal: string, cache: { [x in string]: number }): number {
    if (cache[currentNode.node] !== undefined) {
        return cache[currentNode.node];
    }
    let sum = 0;
    for (const element of currentNode.connections) {
        if (element === goal) {
            return 1;
        }
        sum += dfs(allNodes, allNodes[element], goal, cache);
    }
    cache[currentNode.node] = sum;
    return sum;
}