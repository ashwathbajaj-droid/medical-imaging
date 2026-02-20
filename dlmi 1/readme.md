# Brain Tumor Segmentation: Thresholding Analysis
> **Analyzing the performance of Otsu and Sauvola thresholding for Glioma detection in MRI scans.**

This project implements a medical imaging pipeline to segment brain tumors from the **LGG-MRI Segmentation** dataset. It serves as a technical benchmark to explore the limitations of classical computer vision techniques in neuroimaging.

## 🚀 Key Features
* **Automated Tumor Discovery:** Intelligently scans patient directories to isolate slices where a tumor is physically present.
* **Dual-Method Comparison:**
    * **Otsu Thresholding:** A global method that finds an optimal threshold by minimizing intra-class variance.
    * **Sauvola Thresholding:** A local adaptive method designed to handle lighting gradients and local contrast changes.
* **Validation Metrics:** Implementation of **Dice Coefficient** and **Jaccard Index** to quantify accuracy.



## 🛠️ Tech Stack
* **Python 3.x**
* **OpenCV:** Preprocessing and Otsu binarization.
* **Scikit-Image:** Sauvola adaptive filtering.
* **NumPy:** Logical operations for mask intersection.

---

## 📊 Results & Technical Analysis

| Metric | Otsu (Global) | Sauvola (Local) |
| :--- | :---: | :---: |
| **Dice Score** | **0.0461** | 0.0437 |
| **Jaccard Index** | **0.0236** | 0.0223 |

### 🧠 Why are these scores low?
In medical imaging, "failing" is an opportunity for analysis. The low Dice scores (approx. 4%) highlight three critical challenges in brain MRI segmentation:

1. **Intensity Overlap:** Glioma tissue often has similar pixel intensity to healthy white matter and the skull, causing the thresholding to "leak" into healthy tissue.
2. **Skull Interference:** Without **Skull Stripping**, the bright signal of the cranium is often mistaken for a tumor by global thresholding methods.
3. **Spatial Context:** Classical thresholding treats every pixel as an isolated unit. Tumors are defined by their shape and cluster-like behavior, which requires the spatial understanding of Deep Learning models.



---

## 📂 Dataset Source
This project uses the **LGG-MRI Segmentation Dataset** (Kaggle), featuring 110 patients with manual FLAIR abnormality masks.

## 🚀 Future Roadmap
- [ ] **Skull Stripping:** Implement morphological operations to remove the skull before thresholding.
- [ ] **Frangi Vesselness Filters:** Apply filters to differentiate tubular structures from solid masses.
- [ ] **U-Net Integration:** Implement a Convolutional Neural Network (CNN) to achieve state-of-the-art results (typically 0.85+ Dice).

## 💻 How to Run
1. Install dependencies: `pip install opencv-python numpy scikit-image`
2. Update `base_path` in the script to your local dataset directory.
3. Run the analysis: `python project_medical.py`
