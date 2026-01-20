# Problem 2 – Data Processing and Visualization

## Objective
Retrieve student-related data from an external REST API, process the data to calculate the average test score, and visually represent individual student scores using a bar chart. The visualization helps in understanding score distribution and comparing individual performance against the overall average.

---

## Approach
A Python script was used to retrieve student-related data from a public REST API and visualize the processed information. A GET request was made to the **DummyJSON API** to fetch user data in JSON format. From the API response, the student name and a numeric field were extracted for analysis.

The extracted numeric values were converted into a NumPy array to calculate the average score. A bar chart was created using **Matplotlib** to represent individual student scores. To enhance interpretability, a horizontal reference line was added to the chart to indicate the average score, making it easier to compare individual values against the overall average.

---

## Assumptions
- A public REST API (DummyJSON) was used since no real student test score dataset was provided.
- The **age** field from the API response was treated as a simulated test score for demonstration purposes.
- Records with missing student names or score values were excluded to avoid calculation errors.
- A limited number of API records were used to keep the visualization readable.
- The average score was calculated using all valid records returned by the API.

---

## Result
Student scores were successfully processed and visualized using a bar chart, with the average score clearly highlighted for comparison.




### Architecture
```
problem2_api_visualization/
├── student_scores_api.py
├── README.md
└── scores_with_average.png
```    
