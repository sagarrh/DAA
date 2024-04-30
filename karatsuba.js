
function normalMultiply(x, y) {
    return x * y;
}


function karatsubaMultiply(x, y) {
    if (x < 10 || y < 10) {
        return x * y;
    } else {
        const n = Math.max(String(x).length, String(y).length);
        const half = Math.floor(n / 2);

        const a = Math.floor(x / Math.pow(10, half));
        const b = x % Math.pow(10, half);
        const c = Math.floor(y / Math.pow(10, half));
        const d = y % Math.pow(10, half);

        const ac = karatsubaMultiply(a, c);
        const bd = karatsubaMultiply(b, d);
        const ad_plus_bc = karatsubaMultiply(a + b, c + d) - ac - bd;

        return ac * Math.pow(10, 2 * half) + ad_plus_bc * Math.pow(10, half) + bd;
    }
}


function measureExecutionTime(fn, ...args) {
    const start = performance.now();
    fn(...args);
    const end = performance.now();
    return end - start;
}


const x = 123292222021312456732;
const y = 112132310932212998221;

console.log("Normal multiplication result:", normalMultiply(x, y));
console.log("Karatsuba multiplication result:", karatsubaMultiply(x, y));

const normalTime = measureExecutionTime(normalMultiply, x, y);
const karatsubaTime = measureExecutionTime(karatsubaMultiply, x, y);

console.log("Time taken for normal multiplication:", normalTime, "milliseconds");
console.log("Time taken for Karatsuba multiplication:", karatsubaTime, "milliseconds");
