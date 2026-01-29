import os
import sys

print("Checking imports...")
try:
    import flask
    print("Flask imported")
    import torch
    print("Torch imported")
    import transformers
    print("Transformers imported")
    from ml_engine.recommendation_engine import HelplineRecommender
    print("Recommender imported")
    from ml_engine.emergency_classifier import EmergencyNLPModel
    print("Classifier imported")
    from ml_engine.audio_engine import AudioEngine
    print("Audio engine imported")
    from ml_engine.emotion_engine import EmotionEngine
    print("Emotion engine imported")
    print("All imports successful!")
except Exception as e:
    print(f"Import failed: {e}")
