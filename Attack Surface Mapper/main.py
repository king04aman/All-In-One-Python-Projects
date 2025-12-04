#!/usr/bin/env python3
"""
Attack Surface Mapper - OSINT Reconnaissance Tool

A comprehensive Python-based OSINT reconnaissance platform that combines:
- Google Search API reconnaissance
- GitHub leak detection
- Subdomain enumeration
- Port scanning
- Intelligent correlation analysis

Author: Lingeshwar Kulal (@LingeshwarKulal)
Repositor: https://github.com/LingeshwarKulal/attack-surface-mapper
"""

import sys
import argparse
from typing import Optional

def main():
    """
    Main entry point for Attack Surface Mapper
    """
    parser = argparse.ArgumentParser(
        description='Attack Surface Mapper - OSINT Reconnaissance Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic scan
  python main.py -t example.com
  
  # Complete reconnaissance with all features
  python main.py -t example.com --with-subdomains --with-portscan --html-report
  
  # Subdomain enumeration only
  python main.py -t example.com --with-subdomains --skip-google --skip-github
  
  # Quick scan (skip rate-limited APIs)
  python main.py -t example.com --skip-google --with-subdomains --html-report
        """
    )
    
    # Required arguments
    parser.add_argument(
        '-t', '--target',
        required=True,
        help='Target domain (e.g., example.com)'
    )
    
    # Optional arguments
    parser.add_argument(
        '-c', '--config',
        help='Path to configuration file'
    )
    parser.add_argument(
        '-o', '--output',
        default='output/',
        help='Output directory (default: output/)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    # Scan control flags
    parser.add_argument(
        '--skip-google',
        action='store_true',
        help='Skip Google dorking'
    )
    parser.add_argument(
        '--skip-github',
        action='store_true',
        help='Skip GitHub scanning'
    )
    parser.add_argument(
        '--google-only',
        action='store_true',
        help='Run only Google dorking'
    )
    parser.add_argument(
        '--github-only',
        action='store_true',
        help='Run only GitHub scanning'
    )
    
    # New features
    parser.add_argument(
        '--with-subdomains',
        action='store_true',
        help='Enable subdomain enumeration'
    )
    parser.add_argument(
        '--with-portscan',
        action='store_true',
        help='Enable port scanning'
    )
    parser.add_argument(
        '--html-report',
        action='store_true',
        help='Generate beautiful HTML report'
    )
    
    args = parser.parse_args()
    
    print(f"""
╔═══════════════════════════════════════════════╗
║   Attack Surface Mapper - OSINT Tool          ║
║   v1.0 - By Lingeshwar Kulal                  ║
╚═══════════════════════════════════════════════╝

Target Domain: {args.target}
Verbose Mode: {'Enabled' if args.verbose else 'Disabled'}
Output Directory: {args.output}

Reconnaissance Modules:
  - Google Dorking: {'Enabled' if not args.skip_google and not args.github_only else 'Disabled'}
  - GitHub Scanning: {'Enabled' if not args.skip_github and not args.google_only else 'Disabled'}
  - Subdomain Enumeration: {'Enabled' if args.with_subdomains else 'Disabled'}
  - Port Scanning: {'Enabled' if args.with_portscan else 'Disabled'}
  - HTML Report: {'Enabled' if args.html_report else 'Disabled'}

Starting reconnaissance on {args.target}...
    """)
    
    # Import the actual reconnaissance modules
    try:
        print("[*] Initializing reconnaissance modules...")
        print("[+] For full functionality, clone the complete repository from:")
        print("    https://github.com/LingeshwarKulal/attack-surface-mapper")
        print("\n[*] This is a demonstration entry point.")
        print("[*] The full implementation includes:")
        print("    - Google Custom Search API integration")
        print("    - GitHub API secret scanning")
        print("    - Certificate Transparency enumeration")
        print("    - Multi-threaded port scanning")
        print("    - Intelligent correlation analysis")
        print("    - Beautiful HTML report generation")
        
        return 0
    except Exception as e:
        print(f"[!] Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
