function Water(heights) {
    const n = heights.length;
    const water = new Array(n).fill(0);
    if (n === 0) return { total: 0, water };

    let left = 0;
    let right = n - 1;
    let leftMax = 0;
    let rightMax = 0;
    let totalWater = 0;

    while (left <= right) {
        if (heights[left] <= heights[right]) {
            if (heights[left] >= leftMax) {
                leftMax = heights[left];
            } else {
                const trapped = leftMax - heights[left];
                water[left] = trapped;
                totalWater += trapped;
            }
            left++;
        } else {
            if (heights[right] >= rightMax) {
                rightMax = heights[right];
            } else {
                const trapped = rightMax - heights[right];
                water[right] = trapped;
                totalWater += trapped;
            }
            right--;
        }
    }

    return { total: totalWater, water };
}

function parseInput(str) {
    if (typeof str !== 'string') return { ok: false, error: 'Input must be a string' };

    const parts = str.split(',')
        .map(s => s.trim())
        .filter(s => s.length > 0);

    if (parts.length === 0) return { ok: false, error: 'Please provide at least one number' };

    const arr = [];
    for (let i = 0; i < parts.length; i++) {
        const p = parts[i];
        if (!/^\+?\d+$/.test(p)) return { ok: false, error: `Invalid number at position ${i + 1}: "${p}"` };
        const v = Number(p);
        if (!Number.isFinite(v) || v < 0) return { ok: false, error: `Non-negative integer required at position ${i + 1}` };
        arr.push(v);
    }
    return { ok: true, arr };
}

function render() {
    const input = document.getElementById("inputArr").value;
    const parsed = parseInput(input);

    const resultEl = document.getElementById("result");
    const container = document.getElementById("container");

    if (!parsed.ok) {
        resultEl.textContent = 'Error: ' + parsed.error;
        container.innerHTML = '';
        return;
    }

    const arr = parsed.arr;
    const { total, water } = Water(arr);

    resultEl.textContent = `Total Water: ${total} Units`;

    const maxUnit = Math.max(0, ...arr, ...water);
    const width = 40;
    const scale = 20;

    const yAxisWidth = 40;
    const svgW = arr.length * width + yAxisWidth;
    const svgH = Math.max(120, maxUnit * scale + 20);

    let svg = `<svg width="${svgW}" height="${svgH}" xmlns="http://www.w3.org/2000/svg">`;

    svg += `<line x1="${yAxisWidth - 10}" y1="0" x2="${yAxisWidth - 10}" y2="${svgH}" stroke="black" stroke-width="2"></line>`;

    for (let h = 0; h <= maxUnit; h++) {
        const y = svgH - h * scale;
        svg += `<line x1="${yAxisWidth - 15}" y1="${y}" x2="${yAxisWidth - 10}" y2="${y}" stroke="black" stroke-width="1"></line>`;
        svg += `<text x="${yAxisWidth - 20}" y="${y + 4}" font-size="12" text-anchor="end">${h}</text>`;
    }

    arr.forEach((h, i) => {
        const x = yAxisWidth + i * width;
        const blockH = h * scale;
        const waterH = water[i] * scale;

        if (blockH > 0) {
            svg += `<rect class="block" x="${x + 4}" y="${svgH - blockH}" width="${width - 8}" height="${blockH}"></rect>`;
        }

        if (waterH > 0) {
            const waterY = svgH - blockH - waterH;
            svg += `<rect class="water" x="${x + 4}" y="${waterY}" width="${width - 8}" height="${waterH}"></rect>`;
        }

        svg += `<text class="axis" x="${x + width / 2}" y="${svgH - 4}" text-anchor="middle" font-size="10">${i}</text>`;
    });

    svg += `</svg>`;
    container.innerHTML = svg;
}
