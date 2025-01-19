# CollabCite

### Explanation of the Code: Co-Authorship and Citation Analysis

This code is designed to analyze co-authorship networks and citation patterns in academic articles, providing insights into collaboration patterns, influential authors, and article impact. Below are the key functionalities and their explanations:

---

### **1. Dataset Loading**
- The code loads a CSV file (`PoPCites.csv`) containing information about authors, publication years, and citation metrics.
- Key columns include:
  - **Authors**: Names of authors for each paper.
  - **Year**: Year of publication.
  - **Cites**: Total citations.
  - **CitesPerYear**: Citations per year.

---

### **2. Co-Authorship Network Creation**
- A graph (`G`) is created to represent co-authorship relationships, where:
  - **Nodes**: Authors.
  - **Edges**: Co-authorship links between authors of the same paper.
- The graph is populated by iterating over the dataset, connecting authors from the same article.

---

### **3. Centrality Measures**
- **Degree Centrality**: Measures the number of connections (collaborators) each author has.
- **Betweenness Centrality**: Quantifies how often an author acts as a bridge in the network.

Node sizes are scaled based on their degree, emphasizing more connected authors.

---

### **4. Community Detection**
- Communities are identified using the **greedy modularity algorithm**:
  - Authors are grouped into communities based on their collaboration patterns.
  - Each community is assigned a unique color for visualization.

---

### **5. Network Visualization**
- The graph is plotted using the **spring layout** for better readability.
- Visualization highlights:
  - **Nodes**: Represent authors, colored by community and sized by degree.
  - **Edges**: Show limited connections for clarity, focusing on important nodes (degree > 10 or betweenness > 0.05).
  - **Labels**: Displayed for key authors.

The visualization provides an overview of collaboration patterns and influential contributors.

---

### **6. Overlay and Density Visualization**
- **Articles Per Year**: Bar chart showing the number of articles published annually, offering insights into publication trends.
- **Citations Per Year**: Histogram visualizing the distribution of yearly citations, highlighting the variability in article impact.

---

### **7. Advanced Network Analysis**
- **Closeness Centrality**: Measures how quickly an author can connect to others in the network.
- **Betweenness Centrality**: Identifies authors who act as bridges between communities.
- **Top Authors by Metrics**:
  - Authors with the highest betweenness and closeness centrality are displayed.

---

### **8. Author and Article Impact Analysis**
- **Prolific Authors**: Identifies authors with the highest number of articles.
- **Most Cited Articles**: Lists the top 5 articles with the highest total citations, providing insights into impactful works.

---

### **9. Visualization of Top Articles**
- A horizontal bar chart is used to display the top 5 most cited articles and their citation counts, emphasizing their significance in the field.

---

### **Key Outputs**
1. **Network Graph**: Displays the co-authorship network with communities and key connections.
2. **Publication Trends**: Bar chart showing the number of articles published per year.
3. **Citation Distribution**: Histogram of citations per year.
4. **Author Metrics**: Lists of top authors by centrality and publication count.
5. **Top Articles**: Bar chart visualizing the most cited articles.

---

### **Application**
This code is useful for:
- **Collaboration Analysis**: Understanding co-authorship patterns and identifying influential researchers.
- **Impact Evaluation**: Analyzing article citations to determine the most impactful works.
- **Community Detection**: Identifying research clusters and collaboration networks.
- **Visualization**: Presenting insights through intuitive plots for better understanding of academic trends.
