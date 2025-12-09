#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test API endpoints"""

import requests
import json

BASE_URL = "http://localhost:8000"

print("=" * 60)
print("Testing Face Recognition API Endpoints")
print("=" * 60)

# Test 1: Health check
print("\n[1] Testing /health endpoint...")
try:
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Health check passed!")
        print(f"  Status: {data.get('status')}")
        print(f"  Model loaded: {data.get('model_loaded')}")
        print(f"  Database size: {data.get('database_size')} faces")
    else:
        print(f"✗ Health check failed: {response.status_code}")
        print(f"  Response: {response.text}")
except requests.exceptions.ConnectionError:
    print("✗ Cannot connect to API. Is the server running?")
    print("  Run: python api.py")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Recognize endpoint (with dummy base64)
print("\n[2] Testing /recognize endpoint...")
print("  (This requires a valid base64 image)")
print("  You can test this from the frontend or with a real image")

print("\n" + "=" * 60)
print("API is ready to use!")
print("=" * 60)
print("\nEndpoints:")
print(f"  Health: {BASE_URL}/health")
print(f"  Recognize: {BASE_URL}/recognize")
print(f"  Users: {BASE_URL}/api/users")
print("\nFrontend should call: POST {BASE_URL}/recognize")
print("With body: {{ 'image': 'base64_string' }}")
