import os
import sys

# Add ml_engine to path so we can import modules
sys.path.append(os.path.join(os.getcwd(), 'ml_engine'))

print("Checking imports...")
try:
    import flask
    print("Flask imported")
    import torch
    print("Torch imported")
    import transformers
    print("Transformers imported")
    
    print("Importing recommendation_engine...")
    import recommendation_engine
    print("recommendation_engine imported")
    
    print("Importing emergency_classifier...")
    import emergency_classifier
    print("emergency_classifier imported")
    
    print("Importing audio_engine...")
    import audio_engine
    print("audio_engine imported")
    
    print("Importing emotion_engine...")
    import emotion_engine
    print("emotion_engine imported")
    
    print("All imports successful!")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
