# Dataset
**Dataset Source:** https://www.kaggle.com/datasets/mrmars1010/banana-quality-dataset/data

This dataset was uploaded by MARS_1010 to Kaggle on November, 7th, 2024. This detailed banana dataset includes crucial information about banana samples from various regions and types. The main attributes are:

- **sample_id:** A unique identifier assigned to each banana sample in the dataset. This allows the samples to be tracked and referenced uniquely.

- **variety:** The cultivar or breed of banana, such as Cavendish, Red Dacca, or Lady Finger. Knowing the specific banana variety provides context about the sample's physical characteristics and growing conditions.

- **region:** The geographic origin of the banana, such as Ecuador, Philippines, or Costa Rica. The region can influence factors like climate, soil, and growing practices that impact the banana's qualities.

- **quality_score:** A numerical score, likely on a scale of 1-4 that rates the overall quality of the banana sample. This could encompass factors like appearance, texture, and lack of defects.

- **quality_category:** A text label that categorizes the quality score into broader groupings like "Excellent" etc
This provides an easier-to-understand quality assessment.

- **ripeness_index:** A numerical index representing the ripeness level of the banana, potentially ranging from 1 (green/unripe) to 10 (overripe). This quantifies the maturity of the fruit.

- **ripeness_category:** A text label like "Green", "Yellow", "Ripe", or "Overripe" that corresponds to the ripeness index. This gives a clear, qualitative ripeness classification.

- **sugar_content_brix:** The sugar content of the banana measured in degrees Brix. This is a common way to assess the sweetness and quality of the fruit.

- **firmness_kgf:** The firmness of the banana measured in kilograms-force. This indicates the texture and maturity of the sample.

- **length_cm:** The physical length of the banana in centimeters. This size metric can vary by variety and growing conditions.

# Description of the problem
The dataset provided detailed formations about bananas. I will use that information to train a model that can score and categorize quality of banana.

# Instruction how to run the projects

**Needed Libraries:**
- Pandas
- Matplotlib
- Numpy
- Scikit-learn
- Xgboost
- Flask
- pickle
- request

**To install and run project**

```docker run nguyennoah/banana-quality-prediction```

**If you cannot download the docker image, then run:**

```docker build -t banana-quality-prediction .```

```docker run -it -p 9696:9696 banana-quality-prediction:latest```

**To make a request:**

```python request.py```
- This file will send 1 row and multiple rows to predict.

