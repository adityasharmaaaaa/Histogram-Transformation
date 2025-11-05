# 🖼️ Histogram Transformation using Python

This project performs **Histogram Transformation (Equalization)** on an image using **OpenCV**.  
Histogram equalization is a technique to improve the contrast of an image by redistributing its pixel intensity values — making dark regions lighter and light regions darker for better visibility and detail.

---

## 🚀 Features

- Reads an image and converts it to grayscale.
- Computes and displays both **original** and **equalized** histograms.
- Enhances image contrast using **Histogram Equalization**.
- Displays before-and-after comparison using **Matplotlib**.
- Saves the equalized image automatically to disk.

---

## 🧠 What is Histogram Equalization?

Histogram Equalization enhances image contrast by spreading out the most frequent intensity values.  
In simple terms:
- It **brightens dark images** and **balances contrast**.
- Useful in **medical**, **satellite**, and **low-light** images.
  

## 🧩 Dependencies

Make sure you have the following libraries installed:

```bash
pip install opencv-python numpy matplotlib
