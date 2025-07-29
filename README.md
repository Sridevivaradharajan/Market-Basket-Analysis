# Market-Basket-Analysis
Market Basket Analysis with Tableau dashboard using Association Rule Mining on grocery transactions.
## 🚀 Getting Started

### Prerequisites

To successfully set up and run this project, ensure you have the following installed:

* Python (version 3.7 or higher)
* Jupyter Notebook
* Tableau Desktop

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/yourusername/Market_Basket_Analysis.git](https://github.com/yourusername/Market_Basket_Analysis.git)
    cd Market_Basket_Analysis
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate # For Windows: `venv\Scripts\activate`
    ```

3.  **Install required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Perform Data Preparation and Association Rule Mining:**
    * Navigate to `notebooks/market_basket_analysis.ipynb`.
    * Execute all cells within the notebook to process the data, apply the Apriori algorithm, and generate the association rules. The resulting rules will typically be exported in a CSV format, ready for Tableau.

2.  **Explore the Tableau Dashboard:**
    * Open `tableau/Market Basket Analysis Dashboard.twbx` using Tableau Desktop.
    * Interact with the dashboard to explore the derived item associations and gain actionable insights.

---

## 📈 Analysis and Insights

The `market_basket_analysis.ipynb` notebook outlines the detailed methodology, encompassing:

* **Data Loading and Exploration:** Initial understanding of the transactional dataset.
* **Data Preprocessing:** Transformation of raw data into a suitable format, including one-hot encoding, for the Apriori algorithm.
* **Apriori Algorithm Implementation:** Execution of the Apriori algorithm to discover frequent itemsets and subsequently generate association rules.
* **Rule Filtering:** Refinement of rules based on predefined minimum **support**, **confidence**, and **lift** thresholds to identify the most significant relationships.

The accompanying Tableau dashboard provides an interactive platform for visualizing these rules, enabling users to:

* Identify the most frequently purchased itemsets.
* Analyze rules based on their **antecedent** (IF) and **consequent** (THEN) items.
* Dynamically filter rules using **support**, **confidence**, and **lift** metrics.
* Uncover previously unidentifiable patterns in customer purchasing behavior.

---

## 🎯 Key Metrics Explained

* **Support ($Support(A \rightarrow B)$):** Quantifies how frequently an itemset appears in the dataset. A higher support value indicates a more common itemset.
    $$Support(A \rightarrow B) = P(A \cup B) = \frac{\text{Number of transactions containing A and B}}{\text{Total number of transactions}}$$

* **Confidence ($Confidence(A \rightarrow B)$):** Measures the likelihood of item B being purchased given that item A has already been purchased.
    $$Confidence(A \rightarrow B) = P(B|A) = \frac{Support(A \cup B)}{Support(A)}$$

* **Lift ($Lift(A \rightarrow B)$):** Assesses how much more likely item B is to be purchased when item A is purchased, relative to its individual purchase frequency.
    * A **Lift** value greater than 1 suggests a positive correlation between A and B.
    * A **Lift** value less than 1 indicates a negative correlation.
    * A **Lift** value of 1 implies no correlation between A and B.
    $$Lift(A \rightarrow B) = \frac{Confidence(A \rightarrow B)}{P(B)} = \frac{Support(A \cup B)}{Support(A) \times Support(B)}$$

---

## 🤝 Contributing

We welcome contributions to this project. If you have any suggestions for improvements, new features, or encounter any issues, please feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. For more details, please refer to the `LICENSE` file (if applicable).

---

## 📧 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)
Project Link: [https://github.com/y
