# Open Constellation of Nutritional Values: <br> Mapping the Health Star Rating System

The paper associated with the repository is available here : [Not yet published]

## OpenHSR dataset
### Description
The dataset includes 246 food products from Australian retailers in 2025. Each record contains about 20 variables covering nutrients, metadata, and Health Star Ratings (HSR). It enables analysis of nutritional quality and labeling diversity while following FAIR principles for accessibility and reusability.

- **Nutrient Composition:** Energy (kJ and kcal), protein, total fat, saturated fat, carbohydrates, sugars, fiber, and sodium (per 100 g).  
- **Metadata:** Product name, product type, category, country of origin, retailer, date collected, allergens, ingredients, and data source.  
- **Health Star Rating (HSR):** A score from 0.5 to 5 stars, representing overall nutritional quality.

The dataset is structured to support analysis of nutritional quality, HSR modeling, and food labeling research.

#### Precise description
The dataset consists of product-level information organized in a tabular format. Each row represents a single product, and each column corresponds to a distinct variable. The fields included in the dataset are summarized below:

- product\_name: Name of the product.
- Size\_g: Product size in grams.
- Product\_type: Type or classification of the product.
- category: Broader category of the product.
- country: Country of origin or sale.
- retailer: Retailer or brand associated with the product.
- hsr: Health Star Rating displayed on the packaging.
- nutrient\_energy\_kj: Energy content in kilojoules per 100g.
- protein\_g\_per\_100g: Protein content per 100g.
- fat\_g\_per\_100g: Total fat per 100g.
- sat\_fat\_g\_per\_100g: Saturated fat per 100g.
- carbohydrates: Total carbohydrates per 100g.
- sugars\_g\_per\_100g: Sugar content per 100g.
- sodium\_mg\_per\_100g: Sodium content per 100g in milligrams.
- fiber\_g\_per\_100g: Dietary fiber per 100g.
- ingredients\_text: Full ingredient list.
- date\_collected: Date when the data was collected.
- allergen: Presence of allergens, if any.
- data\_source: Source from which the data was obtained.
- kcal\_per\_100g: Energy content in kilocalories per 100g.

All missing values have been explicitly removed to ensure data quality. Categorical variables have been harmonized to allow easy integration with other datasets and computational pipelines.

### Data Source
All data were manually collected from Australian retail products in 2025. Efforts were made to ensure accuracy and consistency, including verification against product packaging and standardized variable naming.

### Usage
The dataset can be used for:  
- Nutritional analysis  
- Machine learning models predicting HSR  
- Policy research or consumer behavior studies  

Please cite this dataset if used in your research (see **Citation** below).

### License
This dataset is licensed under the MIT License. Users are free to share and adapt the dataset, provided proper attribution is given.

### FAIR Principles
The dataset follows the FAIR principles:  
- **Findable:** Each product has a unique identifier; DOI assigned.  
- **Accessible:** Open access via GitHub under MIT License.  
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

### Algorithm implementation and evaluation

All algorithms employed in this study were implemented in Python using the scikit-learn library. For each algorithm, the implementation strategy depended on the availability and influence of hyperparameters. Algorithms with fixed or minimal hyperparameter configurations (e.g., Linear Regression) were applied using their default settings. In contrast, algorithms with tunable hyperparameters (e.g., Support Vector Machines) underwent a grid search with cross-validation to identify the optimal parameter values.

It is also important to note that data standardization was applied, which was useful depending on the algorithm’s sensitivity to feature scaling. While standardization had negligible impact on scale-invariant models such as Linear Regression and Decision Tree Regression, it was essential for distance-based and margin-based methods, including K-Nearest Neighbors and Support Vector Machines.

For the fine-tuning implementation, we used the OpenFoodFacts dataset to learn the Nutri-Scores. Our neural network results were obtained using Defazio et al. [Schedule-Free optimizer](https://github.com/facebookresearch/schedule_free).

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
For questions or feedback, please contact: [Valentin Lafargue](valentin.lafargue@math.univ-toulouse.fr)




