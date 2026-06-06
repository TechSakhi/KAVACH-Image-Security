import cv2
import hashlib
import os
import numpy as np

# 1. Load the original portrait photo
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: 'sample.jpg' not found in this folder!")
else:
    # --- LAYER 1 & 2: RGB AND PIXEL ARRANGEMENT ---
    # Fix the color layout from BGR to standard RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixel_bytes = rgb_image.tobytes()
    
    # --- LAYER 3: NOISE PATTERN EXTRACTION ---
    # Convert to grayscale to isolate structural noise properties
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply a Laplacian filter to extract high-frequency sensor noise patterns
    noise_pattern = cv2.Laplacian(gray_image, cv2.CV_64F)
    noise_bytes = noise_pattern.tobytes()
    
    # --- CRYPTOGRAPHIC RANDOMIZATION ---
    # Generate 16 completely random bytes (The Salt)
    random_salt = os.urandom(16)
    
    # --- COMBINE ALL ELEMENTS INTO ONE PAYLOAD ---
    # We combine RGB/Pixels, Noise data, and the random salt together
    combined_payload = pixel_bytes + noise_bytes + random_salt
    
    # Pass the combined payload into SHA-256 to get the master UID
    master_uid = hashlib.sha256(combined_payload).hexdigest()
    
    print("==================================================")
    print(f"🔒 KAVACH SECURE 3-IN-1 MASTER UID GENERATED:")
    print(f"{master_uid}")
    print("==================================================")