# Open Constellation of Nutritional Values: <br> Mapping the Health Star Rating System

The paper associated with the repository is available here : [Not yet published]

## OpenHSR dataset
### Description
The dataset includes 246 food products from Australian retailers in 2025. Each record contains about 20 variables covering nutrients, metadata, and Health Star Ratings (HSR). It enables analysis of nutritional quality and labeling diversity while following FAIR principles for accessibility and reusability.

- **Nutrient Composition:** Energy (kJ and kcal), protein, total fat, saturated fat, carbohydrates, sugars, fiber, and sodium (per 100 g).  
- **Metadata:** Product name, product type, category, country of origin, retailer, date collected, allergens, ingredients, and data source.  
- **Health Star Rating (HSR):** A score from 0.5 to 5 stars, representing overall nutritional quality.

The dataset is structured to support analysis of nutritional quality, HSR modeling, and food labeling research.

### Data Source
All data were manually collected from Australian retail products in 2025. Efforts were made to ensure accuracy and consistency, including verification against product packaging and standardized variable naming.

### Usage
The dataset can be used for:  
- Nutritional analysis  
- Machine learning models predicting HSR  
- Policy research or consumer behavior studies  

Please cite this dataset if used in your research (see **Citation** below).

### License
This dataset is licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Users are free to share and adapt the dataset, provided proper attribution is given.

### FAIR Principles
The dataset follows the FAIR principles:  
- **Findable:** Each product has a unique identifier; DOI assigned.  
- **Accessible:** Open access via GitHub under CC BY 4.0.  
- **Interoperable:** Standardized units, consistent variable names, and harmonized categories.  
- **Reusable:** Complete metadata, data dictionaries, and documentation support reproducibility and further research.

## Install
To reproduce the experiments, you can simply clone this repository and install the requierements in a new virtual env as follows:

```
git clone ValentinLafargue/HealthStarDataset
cd HealthStarDataset
python3 -m venv hsr
source hsr/bin/activate (or ./hsr/Script/activate given your setup)
pip install -r requirements.txt
```

## Code
The repository is organized this way:
- Data folder: OpenHSR.csv is our original data file explained above, OpenFoodFacts_clean_sample.csv is a dataset sample from [OpenFoodFacts](https://world.openfoodfacts.org/) which we create by selecting non-missing values on variable of interest and mapping the former categories to HSR categories.
- NN folder: We kept the neural network's weights for reproductibility.
- HS_description.ipynb: Notebook which describes the dataset and enabled us to create the graphs presented in our paper.
- HS_prediction.ipynb: Notebook used to produce the paper benchmark, it predicts the HSR using classical machine learning and neural networks.
- requirements.txt: librairies needed in the project
- utils.py: python fonctions used in the neural network 

## Citation
If you use this dataset, please cite:
> N'kam Suguem, F., & Lafargue, V. (2025). Open Health Star Rating (OpenHSR) (Version v1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17469191

If you find this repository useful in your research, please consider citing our paper.

```
{
Not yet published
}
```

## Contact
For questions or feedback, please contact: [Valentin Lafargue/valentin.lafargue@math.univ-toulouse.fr]




