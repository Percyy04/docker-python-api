#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script to check API setup"""

import sys
import traceback

print("=" * 50)
print("Testing API Setup")
print("=" * 50)

# Test 1: Check imports
print("\n[1] Testing imports...")
try:
    from flask import Flask, jsonify, request
    from flask_cors import CORS
    import cv2
    import numpy as np
    print("✓ All basic imports successful")
except Exception as e:
    print(f"✗ Import error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 2: Check src imports
print("\n[2] Testing src module imports...")
try:
    from src.face_model import init_insightface, extract_faces, extract_embedding
    from src.database import load_database, find_best_match
    print("✓ All src imports successful")
except Exception as e:
    print(f"✗ Src import error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 3: Check database files
print("\n[3] Testing database files...")
import os
from src.config import Config

embeddings_file = Config.embeddings_file
labels_file = Config.labels_file

if os.path.exists(embeddings_file):
    print(f"✓ Embeddings file exists: {embeddings_file}")
else:
    print(f"✗ Embeddings file NOT found: {embeddings_file}")
    print("  Run: python build_face_db.py")

if os.path.exists(labels_file):
    print(f"✓ Labels file exists: {labels_file}")
else:
    print(f"✗ Labels file NOT found: {labels_file}")
    print("  Run: python build_face_db.py")

# Test 4: Try to initialize model
print("\n[4] Testing InsightFace initialization...")
try:
    print("  Initializing model (this may take a moment)...")
    face_app = init_insightface()
    print("✓ InsightFace model initialized successfully")
except Exception as e:
    print(f"✗ Model initialization error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 5: Try to load database
print("\n[5] Testing database loading...")
try:
    db_embeddings, db_labels = load_database()
    print(f"✓ Database loaded: {len(db_labels)} faces")
except Exception as e:
    print(f"✗ Database loading error: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test 6: Test Flask app creation
print("\n[6] Testing Flask app creation...")
try:
    app = Flask(__name__)
    CORS(app)
    print("✓ Flask app created successfully")
except Exception as e:
    print(f"✗ Flask app creation error: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 50)
print("✓ All tests passed! API should work correctly.")
print("=" * 50)
print("\nYou can now run: python api.py")
