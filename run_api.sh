#!/bin/bash
echo "Activating conda environment: face-checkin"
source activate face-checkin
echo ""
echo "Starting Face Recognition API..."
echo "API will run at http://localhost:8000"
echo ""
python api.py
