# Guide: How to Use This Repo and Post on LinkedIn

This guide outlines exactly how to run the analyses locally, update the files, and execute the LinkedIn posting strategy to maximize your professional visibility.

---

## Part 1: How to Use This Repository

### 1. Local Setup
To run the notebooks and inspect the code locally, follow these steps in your terminal:

```bash
# Clone the repository (if you are on a new machine)
git clone https://github.com/the-irritater/Stat_That_Make_Data_Speak.git
cd Stat_That_Make_Data_Speak

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate

# Install all required libraries
pip install -r requirements.txt
```

### 2. Running the Applied Notebooks
Each folder under `applied/notebooks/` contains a `.py` (Jupytext script) and a `.ipynb` (Jupyter Notebook) version. 

To open and interact with the notebooks:
```bash
# Start the Jupyter server
jupyter notebook
```
This will launch Jupyter in your web browser. You can click on the `applied/notebooks/` directory and open any of the 7 notebooks to run the code cells, modify values, and view the generated charts.

### 3. Editing Code (Jupytext Workflow)
We use Jupytext to keep Python scripts and Jupyter Notebooks in sync. This is clean and prevents Git conflicts.
- If you edit the `.py` script (e.g. `03-what-drives-sales.py`), you can convert it to a notebook and execute it using:
  ```bash
  jupytext --to ipynb applied/notebooks/03-what-drives-sales.py -o applied/notebooks/03-what-drives-sales.ipynb
  jupyter nbconvert --to notebook --execute --inplace applied/notebooks/03-what-drives-sales.ipynb
  ```

---

## Part 2: LinkedIn Step-by-Step Posting Strategy

The goal of this repository is to establish you as a Data Analyst who can translate statistical concepts into real-world business decisions. 

Follow this step-by-step workflow to share your work on LinkedIn:

### Step 1: Follow the Weekly Content Calendar
To stay consistent without burning out, use this rotation:

| Day | Post Type | What You Share | What to Attach |
|---|---|---|---|
| **Monday** | Concept Post | A simple breakdown of a theory concept from `modules/01-basics/` (e.g., Types of Data) | A PDF carousel or text diagram |
| **Wednesday** | Applied Post | A walkthrough of one of the 7 applied notebooks | The corresponding `.png` chart |
| **Friday** | Case Study | A deep dive into one of the 2 case studies | The case study comparison chart |

### Step 2: Extract Your Post Draft
Every applied notebook and case study contains a pre-written, emoji-free, professional **LinkedIn Post Draft** at the bottom of the file.
1. Open the notebook or `.py` file of the analysis you want to share.
2. Scroll to the **LinkedIn Post Draft** section.
3. Copy the text.

### Step 3: Get Your Visual Assets
LinkedIn posts with images receive up to 2x more engagement. Every notebook exports a clean chart in its directory:
- Notebook 1: `applied/notebooks/01_distributions.png`
- Notebook 2: `applied/notebooks/02_key_chart.png`
- Notebook 3: `applied/notebooks/03_correlation_heatmap.png`
- Notebook 4: `applied/notebooks/04_duration_vs_spend.png`
- Notebook 5: `applied/notebooks/05_discount_ab_test.png`
- Notebook 6: `applied/notebooks/06_customer_segments_scatter.png`
- Notebook 7: `applied/notebooks/07_ab_test_results.png`
- Case Study 1: `applied/case-studies/screen-time-vs-productivity/screen_time_vs_productivity_scatter.png`
- Case Study 2: `applied/case-studies/discount-vs-retention/discount_retention_curve.png`

*Action:* Download the corresponding `.png` file to your computer/phone.

### Step 4: Publish the Post
1. Open LinkedIn and click **Start a post**.
2. Paste the copied text draft.
3. Add the corresponding `.png` chart to the post as an image.
4. Replace the `[GitHub link]` placeholder in the text with the actual link to that specific file on your GitHub repository.
   - Example for Notebook 3: `https://github.com/the-irritater/Stat_That_Make_Data_Speak/blob/main/applied/notebooks/03-what-drives-sales.ipynb`
5. Click **Post**.

---

## Part 3: The Visibility Loop (Why This Works)

When you post, you create a direct pipeline:
1. **Recruiter reads your post** on LinkedIn. They see a clear business problem (e.g., "Do deep discounts actually increase repeat purchases?").
2. **They look at the chart** and see professional, clear visualization skills.
3. **They click the GitHub link** to see how you coded the analysis.
4. **They arrive at a fully documented repository** with clean READMEs, executable notebooks, and organized datasets.

This workflow instantly upgrades your application from "just another CV" to a verified portfolio of applied business data analysis.
