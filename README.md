# Pneumonia Disease Detection Using Advanced Neural Network

## Overview
This project leverages advanced Convolutional Neural Networks (CNN) to detect pneumonia from chest X-ray images. The primary objective is to develop an end to end system that assists medical professionals in diagnosing pneumonia accurately and efficiently. 

## Abstract
The collaboration of machine learning with the medical field is expanding rapidly. Pneumonia, among other diseases, results in numerous deaths due to inadequate medical facilities and irregular checkups. This project utilizes supervised machine learning algorithms, particularly CNNs, to enhance the early detection and diagnosis of pneumonia from chest X-ray images.

## Key Features
- **Advanced CNN Models:** Utilizes and compares various CNN architectures such as VGG16, Inception V3, and a custom CNN model.
- **Image Preprocessing:** Includes normalization and data augmentation to enhance model performance.
- **User Interface:** A web-based interface using Flask for users to upload X-ray images and get predictions.

## Dataset
The dataset used is from Kaggle: "Chest X-ray Images (Pneumonia)" curated by Paul Mooney. It includes 5,856 validated chest X-ray images, categorized into training and testing sets.

| Distribution | Training | Testing |
|--------------|----------|---------|
| Normal       | 1349     | 234     |
| Pneumonia    | 3883     | 390     |
| **Total**    | 5232     | 624     |

## Methodology
### Data Preprocessing
- **Normalization:** Ensures each pixel value is scaled to the same range.
- **Data Augmentation:** Techniques such as zooming, rotating, and flipping images to increase diversity in the training dataset.

### Models Used
1. **VGG16:** A straightforward architecture known for its simplicity and effectiveness.
2. **Inception V3:** Utilizes inception modules for extracting features at multiple scales.
3. **Custom CNN Model:** Specifically designed for this project to optimize performance for pneumonia detection.

### Training
- The models were trained using the Keras framework with the sequential model approach.
- Each model's performance was evaluated using metrics such as precision, recall, F1-score, and overall accuracy.

## Results
The custom CNN model achieved the highest accuracy of 94%, outperforming VGG16 and Inception V3, which had accuracies of 87% and 93% respectively.

| Model           | Accuracy | Precision (Pneumonia) | Recall (Pneumonia) | F1-Score (Pneumonia) | Precision (Normal) | Recall (Normal) | F1-Score (Normal) |
|-----------------|----------|-----------------------|---------------------|----------------------|--------------------|-----------------|------------------|
| **VGG16**       | 87%      | 0.83                  | 0.99                | 0.91                 | 0.98               | 0.67            | 0.79             |
| **Inception V3**| 93%      | 0.92                  | 0.97                | 0.95                 | 0.95               | 0.85            | 0.90             |
| **Custom CNN**  | 94%      | 0.97                  | 0.93                | 0.95                 | 0.89               | 0.94            | 0.92             |

## Conclusion
The custom CNN model demonstrated superior performance in detecting pneumonia from chest X-ray images, making it a viable option for practical medical applications. Further collaboration with healthcare professionals is recommended to enhance the model's effectiveness in real-world settings.

## Installation and Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/pneumonia-detection.git
   cd pneumonia-detection
