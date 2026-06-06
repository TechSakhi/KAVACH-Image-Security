import cv2
import numpy as np

# 1. Load both the original and the edited photos
original = cv2.imread("sample.jpg")
edited = cv2.imread("sample_edited1.jpg")

if original is None or edited is None:
    print("Error: Make sure both 'sample.jpg' and 'sample_edited.jpg' are in this folder.")
else:
    # 2. Convert both to standard RGB layout
    orig_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    edit_rgb = cv2.cvtColor(edited, cv2.COLOR_BGR2RGB)
    
    print("--- Running Kavach Integrity Verification ---")
    
    # 3. Check if the physical layout/dimensions changed (e.g., This happens during Cropping,Resizing,or when taking a screenshot)
    if orig_rgb.shape != edit_rgb.shape:
        print("\n❌ ALERT: Tampering Detected!")
        print("Modification Type: Structral Layout change(Screenshot,crop,or Resize detected).")
    else:
        # 4. If dimensions match, calculate pixel-level alterations
        # cv2.absdiff finds the exact mathematical differences between the matrices
        pixel_difference = cv2.absdiff(orig_rgb, edit_rgb)
        altered_pixels = np.count_nonzero(pixel_difference)
        
        if altered_pixels == 0:
            print("\n✅ Verification SUCCESS: Image is completely authentic and unaltered.")
        else:
            print("\n❌ ALERT: Tampering Detected!")
            print("Modification Type: Pixel Manipulation / Object Edit")
            print(f"Altered pixel data blocks discovered: {altered_pixels}")