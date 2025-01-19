import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from networkx.algorithms.community import greedy_modularity_communities

# 1. Load the dataset
file_path = r"E:\New folder (15)\New folder (3)\New folder (2)\New folder\New folder\downloads\New folder (9)\New folder (3)\New folder\مقالات\PoPCites.csv"
data = pd.read_csv(file_path)

# 2. Create the co-authorship network
G = nx.Graph()

# Loop through each article and add edges between authors
for authors in data['Authors'].dropna():
    author_list = [author.strip() for author in authors.split(',')]
    for i, author1 in enumerate(author_list):
        for author2 in author_list[i + 1:]:
            G.add_edge(author1, author2)

# 3. Calculate degree and betweenness centrality
degree_dict = dict(G.degree())
betweenness = nx.betweenness_centrality(G)

# Normalize node sizes based on the degree
node_sizes = [degree_dict[node] * 50 if degree_dict[node]
              > 10 else degree_dict[node] * 10 for node in G.nodes()]

# 4. Community detection (using greedy modularity)
communities = greedy_modularity_communities(G)
community_map = {}
for i, community in enumerate(communities):
    for name in community:
        community_map[name] = i

# Assign a color to each community
colors = list(mcolors.TABLEAU_COLORS.values())
node_colors = [colors[community_map[node] % len(colors)] for node in G.nodes()]

# 5. Set up the graph plotting
plt.figure(figsize=(15, 15))

# Position the nodes using a spring layout
pos = nx.spring_layout(G, seed=42, k=0.5)

# Draw nodes with their corresponding colors and sizes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes,
                       node_color=node_colors, alpha=0.9)

# 6. Select and display limited edges connected to important nodes
important_nodes = {node: node for node, deg in degree_dict.items()
                   if deg > 10 or betweenness[node] > 0.05}

# Initialize list of edges to draw
important_edges = []

# Display only the top 3 neighbors for each important node
for node in important_nodes:
    neighbors = sorted(G.neighbors(node), key=lambda x: degree_dict[x], reverse=True)[
        :3]  # Top 3 neighbors by degree
    for neighbor in neighbors:
        important_edges.append((node, neighbor))

# Set edge colors based on the node communities
edge_colors = []
for u, v in important_edges:
    if community_map[u] == community_map[v]:
        # Same color for edges within the same community
        edge_colors.append(colors[community_map[u] % len(colors)])
    else:
        # Gray for edges between different communities
        edge_colors.append('gray')

# Draw the important edges with proper colors
nx.draw_networkx_edges(G, pos, edgelist=important_edges,
                       edge_color=edge_colors, alpha=0.7, width=2)

# Draw labels for important nodes (degree > 10 or betweenness > 0.05)
nx.draw_networkx_labels(G, pos, labels=important_nodes,
                        font_size=14, font_weight='bold', font_color='black')

# Set the title and hide the axis
plt.title('Co-authorship Network with Limited Important Connections', fontsize=18)
plt.axis('off')

# Show the plot
plt.show()


# 6. مصورسازی همپوشانی (Overlay Visualization)
years = data['Year'].dropna().astype(int)
plt.figure(figsize=(10, 6))
years.value_counts().sort_index().plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Number of Articles')
plt.title('Number of Machine Learning in Agriculture Articles per Year')
plt.show()

# 7. مصورسازی تراکم داده‌ها (Density Visualization)
plt.figure(figsize=(10, 6))
plt.hist(data['CitesPerYear'].dropna(), bins=20, edgecolor='black')
plt.xlabel('Citations per Year')
plt.ylabel('Number of Articles')
plt.title('Density of Citations per Year')
plt.show()

# 8. تحلیل شبکه پیشرفته: Betweenness و Closeness Centrality
closeness = nx.closeness_centrality(G)

# نمایش نویسندگان با بالاترین Betweenness Centrality
top_betweenness = sorted(
    betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 authors by Betweenness Centrality:")
for author, centrality in top_betweenness:
    print(f"{author}: {centrality:.4f}")

# نمایش نویسندگان با بالاترین Closeness Centrality
top_closeness = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 authors by Closeness Centrality:")
for author, centrality in top_closeness:
    print(f"{author}: {centrality:.4f}")

# 9. تحلیل نویسندگان پربار بر اساس تعداد مقالات
author_count = data['Authors'].str.split(
    ',').explode().str.strip().value_counts().head(5)
print("\nTop 5 authors by number of articles:")
print(author_count)

# 10. تحلیل مقالات با بیشترین استناد
top_cited = data[['Title', 'Cites']].sort_values(
    by='Cites', ascending=False).head(5)
print("\nTop 5 most cited papers:")
print(top_cited)

# 11. مصورسازی مقالات مهم در نقشه علمی
plt.figure(figsize=(10, 6))
top_cited_titles = top_cited['Title']
top_cited_cites = top_cited['Cites']
plt.barh(top_cited_titles, top_cited_cites, color='skyblue')
plt.xlabel('Number of Citations')
plt.ylabel('Article Title')
plt.title('Top 5 Most Cited Articles in Machine Learning in Agriculture')
plt.show()
