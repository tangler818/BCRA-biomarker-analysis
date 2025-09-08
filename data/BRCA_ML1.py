
"""BRCA Biomarker Analysis using RFE and Random Forest

This script selects the top (n) genes predictive of a target organ
(e.g "Bone") from gene expression comparisons. Normally would use train/test split, feel free to change n_features_to_select
| Change csv file to local path """



import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

#load with local path
file_path = r"C:\Users\Tangl\Downloads\PW1.csv"
df = pd.read_csv(file_path, index_col=0)
#Transpose the .csv
X = df.T

#Binary labels, select target organ from Bone, Breast, Brain, Liver, Lung, Lymph node, Muscle, Ovary, Pleura, Peritoneum, Skin,
y = X.index.to_series().apply(lambda x: 1 if "Bone" in x else 0).values

#Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#Run RFE with Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=2005) #can change random state to test for reproduced results
selector = RFE(model, n_features_to_select=5, step=0.05)            #step is .05 for thorough but quick results
selector = selector.fit(X_scaled, y)

#Results go to console in order of rank
gene_ranks = pd.DataFrame({
    "Gene": X.columns,
    "Rank": selector.ranking_,
    "Selected": selector.support_
}).sort_values(by="Rank")


print("Top selected genes:")
top_genes_ordered = gene_ranks[gene_ranks["Selected"]].sort_values(by="Rank")
print(top_genes_ordered["Gene"].tolist())


