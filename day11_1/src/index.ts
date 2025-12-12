import { readFileSync } from "fs";

(() => {
    const data = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n');
    const nodes: { [x in string]: { node: string, connections: string[]; } } = {};
    for (const element of data) {
        const splitted = element.trim().split(': ');
        const newNode = { node: splitted[0], connections: splitted[1].split(' ') };
        nodes[newNode.node] = newNode;
    }
    console.log(dfs(nodes, nodes['you'], new Set<string>()));
})();

function dfs(allNodes: { [x in string]: { node: string, connections: string[]; } }, currentNode: { node: string, connections: string[]; }, visitedNodes: Set<string>): number {
    if (visitedNodes.has(currentNode.node)) {
        return 0;
    }
    let sum = 0;
    for (const element of currentNode.connections) {
        if (element === 'out') {
            return 1;
        }
        visitedNodes.add(currentNode.node);
        sum += dfs(allNodes, allNodes[element], visitedNodes);
        visitedNodes.delete(currentNode.node);
    }
    return sum;
}