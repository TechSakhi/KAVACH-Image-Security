#  KAVACH: Image Integrity & Ownership Security Framework

Kavach is a proactive, camera-integrated computer vision and cryptographic framework designed to secure digital images at the point of capture, protecting individuals from unauthorized AI edits, deepfakes, and privacy violations.

##  The Finish-Up-A-Thon Evolution: Old vs. New

This repository represents a high-speed sprint to transform a theoretical research concept into a live, executing software prototype. 

>  **Developer Context:** As a 20-year-old student currently utilizing the summer break before university admissions officially begin for my first year of college, this project marks my very first practical experience working with GitHub. Because I do not currently own a laptop, I had to learn version control, navigate coding environments, and build these low-level computer vision pipelines under highly constrained device access.

###  The Old Version (The Idea)
Originally, **Kavach** existed only as a theoretical architectural design paper (`kavach_2.pdf`). 
- It outlined a conceptual vision for a multi-layered image validation system using RGB, pixel matrices, and sensor noise to prevent digital tampering and unauthorized image distribution.
- No functional codebase, automation, or live validation engine existed.

###  The New Version (The Working Prototype)
During the hackathon, the entire core data pipeline was successfully brought to life in Python:
- **`Kavach_core.py`:** A fully operational backend engine that utilizes OpenCV and NumPy to ingest raw portrait images, extract RGB arrays, map structural layouts, isolate physical camera sensor grain via a Laplacian filter, and securely hash the unified payload with a 16-byte random salt using SHA-256.
- **`kavach_verify.py`:** A functional testing engine that evaluates original master files against modified assets or screenshot copies—calculating mathematical matrix differences (`cv2.absdiff`) and triggering automated structural layout or pixel manipulation alerts in the terminal.

## Tech Stack
- Python 3
- OpenCV (`cv2`)
- NumPy
- Hashlib & OS (Built-in Cryptography)

##  Future Roadmap (Scaling Kavach)
Following the core architecture laid out in our initial framework design, the production version of Kavach will scale across the following deployment phases:

### 1. AI Edit Classification
Instead of basic rule-based pixel difference checks, we will implement a Machine Learning Classification layer using `scikit-learn` or a lightweight Convolutional Neural Network (CNN). This module will analyze structural variance, Mean Squared Error (MSE), and localized Laplacian noise disruption to automatically categorize edits into specific buckets (e.g., blurring, color filters, object erasures, or structural deepfakes).

### 2. Hardware Camera API Integration
To prevent bad actors from tampering with image data before a UID can be generated, the logic must run directly at the point of capture. Packaging this Python framework into mobile libraries running on Android Camera2 or iOS AVFoundation APIs will allow Kavach to sign raw sensor data-streams the exact millisecond the shutter clicks.

### 3. Cloud Ledger & Reverse Monitoring Ecosystem
To actively monitor and protect user privacy across the web, the system will deploy:
- **Secure UID Registry:** Automatically syncing generated master hashes to a secure, user-controlled cloud database.
- **Automated Verification Web Scrapers:** Deploying lightweight background scrapers to read online image streams, hash them on the fly, and match them against the master registry.
- **Granular Privacy Alerts:** Providing a user dashboard where individuals can customize notification triggers (e.g., allowing simple background cropping but instantly alerting the owner if structural facial manipulations are flagged).
