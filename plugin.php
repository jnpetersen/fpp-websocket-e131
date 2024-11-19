<?php
// FPP Plugin - E1.31 WebSocket Transmitter
function StartPlugin() {
    // Call the Python WebSocket server script
    exec("python3 /home/fpp/media/plugins/fpp_plugin_websocket/scripts/websocket_server.py > /dev/null 2>&1 &");
}

function StopPlugin() {
    // Stop any running instances of the server
    exec("pkill -f websocket_server.py");
}
?>