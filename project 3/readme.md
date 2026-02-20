# Retinal Vessel Segmentation: Local Thresholding Comparison
> **A comparative study of Niblack vs. Sauvola binarization for medical image analysis on the DRIVE dataset.**

This project implements a classical computer vision pipeline to extract blood vessels from retinal fundus images. It focuses on **Green Channel extraction** and compares two local adaptive thresholding techniques to determine which is more effective at identifying vascular structures.

## 🚀 Key Features
* **Auto-Discovery:** Automatically scans Kaggle/local directories to find the DRIVE dataset folders.
* **Optimized Preprocessing:** Extracts the green channel and applies histogram equalization to maximize vessel contrast.
* **Advanced Binarization:** Implements both **Niblack** and **Sauvola** adaptive thresholding.
* **Quantitative Analysis:** Calculates the **Sensitivity (True Positive Rate)** for both methods against professional ground truth masks.



## 📊 Results
Based on the DRIVE dataset training images, the performance comparison is as follows:

| Method | Average Sensitivity (TPR) | Verdict |
| :--- | :--- | :--- |
| **Niblack** | **0.7854** | Higher sensitivity; captures more vessel detail. |
| **Sauvola** | **0.5859** | More conservative; misses thinner vascular branches. |

---

## 🛠️ Tech Stack
* **Python 3.x**
* **OpenCV:** Image processing and I/O.
* **Scikit-Image:** Implementation of Niblack and Sauvola filters.
* **NumPy:** Mathematical operations and mask comparisons.
* **Matplotlib:** Visualization of segmentation results.

---

## ⚙️ How it Works
1. **Green Channel Extraction:** Blood vessels have the highest absorption in the green spectrum, making them appear darkest.
2. **Histogram Equalization:** Standardizes the intensity distribution to handle varying lighting conditions in fundus photography.
3. **Local Thresholding:** Instead of a global threshold, the algorithm looks at a **41px window** to calculate a threshold based on local mean and standard deviation:
   * **Niblack:** $T = m + k \times s$
   * **Sauvola:** $T = m \times (1 + k \times (\frac{s}{R} - 1))$
4. **Evaluation:** Compares the binary output against the `1st_manual` ground truth images using the True Positive Rate metric.



---

### Future Improvements
- [ ] Add **Frangi Vesselness Filters** to improve tubular structure detection.
- [ ] Implement a **Field of View (FOV) mask** to remove noise at the circular borders of the retina.
- [ ] Integrate a **U-Net (Deep Learning)** approach to compare classical CV vs. AI.
