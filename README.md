# Server Guard & AI Metrics Monitor

Production-ready CLI tool for monitoring API endpoints, parsing JSON metrics, and resilient error handling.

## Features
- **CLI Interface**: Accepts target URLs via command-line arguments (`sys.argv`).
- **External Config**: Driven by `config.json` with safe fallback defaults.
- **Dual Production Logging**: Simultaneous console output and rotating file logs (`UTF-8`).
- **Resilience**: Protected against network timeouts, HTTP errors, and unexpected crashes.

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Start local mock server: `python mock_server.py`
3. Run monitor: `python script1.py`