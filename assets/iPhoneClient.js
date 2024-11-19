const ws = new WebSocket("ws://192.168.90.149:8765");

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    updateDisplay(data.pixels); // Implement display logic
};

function updateDisplay(pixels) {
    const display = document.getElementById("display");
    display.innerHTML = ""; // Clear existing pixels
    pixels.forEach(pixel => {
        const div = document.createElement("div");
        div.style.backgroundColor = `rgb(${pixel.r}, ${pixel.g}, ${pixel.b})`;
        div.style.width = "20px";
        div.style.height = "20px";
        div.style.display = "inline-block";
        display.appendChild(div);
    });
}
