#!/usr/bin/env python3
import os
import sys

def check_environment():
    """Check if all required environment variables are set"""
    print("🔍 Checking environment...")
    
    creds = os.environ.get('GOOGLE_CREDENTIALS_JSON')
    sheet_id = os.environ.get('SPREADSHEET_ID')
    
    if not creds:
        print("❌ GOOGLE_CREDENTIALS_JSON not found in environment")
        return False
    
    if not sheet_id:
        print("❌ SPREADSHEET_ID not found in environment")
        return False
    
    print("✅ Environment variables found")
    print(f"✅ Spreadsheet ID: {sheet_id[:10]}...")
    print(f"✅ Credentials length: {len(creds)} characters")
    
    return True

if __name__ == "__main__":
    if not check_environment():
        print("❌ Environment check failed")
        sys.exit(1)
    
    # Import and run the main script only if environment is OK
    try:
        from fda_scraper import main
        success = main()
        sys.exit(0 if success else 1)
    except ImportError as e:
        print(f"❌ Import error: {e}")
        sys.exit(1)
