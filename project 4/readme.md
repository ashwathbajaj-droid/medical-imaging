
# Cell Nuclei Segmentation: Marker-Controlled Watershed
> **An implementation of the Watershed algorithm to identify and separate individual cell nuclei in microscopy images.**

This project demonstrates a robust pipeline for segmenting overlapping objects in biological imaging. Using the **Data Science Bowl 2018** dataset, it compares standard Watershed segmentation against a **Marker-Controlled** approach to solve the common problem of "over-segmentation."

## 🚀 Key Features
* **Automated Data Discovery:** Dynamically locates the `stage1-train` directory within Kaggle environments.
* **Distance Transform Processing:** Converts binary masks into topographic maps where the centers of cells are the "deepest" points.
* **Peak Detection:** Uses a local maximum search (25x25 window) to identify the unique center of every nucleus.
* **Watershed Comparison:** Contrast between baseline Watershed (which often splits single cells) and Marker-Controlled Watershed (which preserves object integrity).



## 🛠️ Tech Stack
* **Python 3.x**
* **Scikit-Image:** For Watershed, Peak Local Max, and Otsu thresholding.
* **SciPy:** For Distance Transform and Labeling.
* **OpenCV:** For image I/O and Gaussian smoothing.
* **Matplotlib:** For multi-stage pipeline visualization.

---

## ⚙️ The Pipeline
1. **Preprocessing:** Grayscale conversion followed by a **5x5 Gaussian Blur** to reduce high-frequency noise that causes "false peaks."
2. **Global Thresholding:** Uses **Otsu’s Method** to create a binary mask, separating foreground (cells) from background.
3. **Euclidean Distance Transform (EDT):** Calculates the distance from every foreground pixel to the nearest background pixel.
4. **Marker Generation:** * Finds local peaks in the Distance Transform.
   * Assigns a unique integer ID to each peak.
5. **Watershed Transformation:** Treats the inverse distance map as a topographic surface and "floods" it starting only from the pre-defined markers.



## 📊 Comparison Results
* **Standard Watershed:** Tends to "over-segment," splitting a single cell into multiple fragments because of small fluctuations in pixel intensity.
* **Marker-Controlled Watershed:** Successfully treats each cell as a single instance by ignoring noise and focusing only on the calculated "seeds" or markers.

---

### Future Improvements
- [ ] Implement **Morphological Operations** (Opening/Closing) to clean up mask edges.
- [ ] Add **Adaptive Thresholding** for images with uneven illumination.
- [ ] Compare performance against a **U-Net** deep learning model.
