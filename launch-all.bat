@echo off
echo 🚀 Starting Saathi Helpline App...

echo 1. Starting ML Backend (Port 5001)...
start cmd /k ".\.venv\Scripts\python ml_engine/api.py"

echo 2. Starting Node.js Backend (Port 5000)...
start cmd /k "cd saathi-backend && node server.js"

echo 3. Starting React Frontend (Port 3000)...
start cmd /k "npm start"

echo ✅ All components are starting!
echo ML Engine: http://localhost:5001
echo Node Backend: http://localhost:5000
echo Frontend: http://localhost:3000
pause
