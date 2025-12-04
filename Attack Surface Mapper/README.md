# Attack Surface Mapper

A comprehensive Python-based OSINT reconnaissance platform that combines Google Search API, GitHub leak detection, subdomain enumeration, port scanning, and intelligent correlation analysis to identify an organization's complete attack surface.

## Overview

**Attack Surface Mapper** automates professional security reconnaissance by discovering exposure patterns that traditional scanners miss. It performs deep reconnaissance on target domains without direct interaction with internal systems, making it fully external and ethical OSINT-driven - perfect for VAPT engagements, bug bounty hunting, and security audits.

## Key Features

### 1. Google Search API Reconnaissance
- Intelligent Google dorking through official API
- Detects admin panels, login pages, and debug interfaces
- Identifies exposed files (PDF, DOCX, SQL, ENV, LOG)
- Finds publicly indexed API documentation
- Discovers cloud storage misconfigurations (AWS S3, Azure Blob, GCS)

### 2. GitHub API Secret & Leak Scanner
- Scans public repositories for sensitive information
- Detects hardcoded credentials and API keys
- Pattern-based detection for 15+ secret types
- Analyzes commit history for leaked secrets

### 3. Subdomain Enumeration
- Certificate Transparency log queries (crt.sh)
- DNS brute-force on common subdomains
- Wildcard DNS detection
- Intelligent categorization by purpose

### 4. Port Scanner
- Multi-threaded concurrent scanning
- 24+ common service ports detection
- Service identification and banner grabbing

### 5. Correlation Engine
- Merges findings from all reconnaissance sources
- Identifies critical combinations
- Intelligent risk scoring (0-100)

## Installation

```bash
git clone https://github.com/LingeshwarKulal/attack-surface-mapper.git
cd attack-surface-mapper
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API credentials
```

## Usage

```bash
# Basic scan
python src/main.py -t example.com

# Complete reconnaissance
python src/main.py -t example.com --with-subdomains --with-portscan --html-report

# Subdomain enumeration only
python src/main.py -t example.com --with-subdomains --skip-google --skip-github
```

## Use Cases

- **VAPT Engagements**: Initial reconnaissance phase
- **Bug Bounty Hunting**: Asset discovery and exposure detection
- **Red Team Operations**: External attack surface mapping
- **Security Audits**: Identifying public data leaks
- **Continuous Monitoring**: Regular security posture assessment

## Requirements

- Python 3.8 or higher
- Google Custom Search API key and CSE ID
- GitHub Personal Access Token

## Author

**Lingeshwar Kulal** - [@LingeshwarKulal](https://github.com/LingeshwarKulal)

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is provided for educational and authorized security testing purposes only. Always ensure you have explicit authorization before scanning any target.

---

For the complete source code and documentation, visit: [attack-surface-mapper](https://github.com/LingeshwarKulal/attack-surface-mapper)
