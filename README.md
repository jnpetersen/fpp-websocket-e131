# E1.31 WebSocket Transmitter Plugin for FPP

## Overview
This plugin streams E1.31 DMX data to a WebSocket server, allowing external devices to display pixel data in real-time.

## Installation
1. Place the `fpp_plugin_websocket` folder in `/home/fpp/media/plugins/`.
2. Restart FPPD.
3. Activate the plugin in the FPP interface.

## Usage
- WebSocket server runs on `ws://[FPP-IP]:8765`.
- Connect your iPhone or other device to this server.

## Customization
- Modify `websocket_server.py` for custom data parsing or transmission.
