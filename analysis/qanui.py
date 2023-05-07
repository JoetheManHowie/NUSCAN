import itertools

def calculate_isolatability(cluster, graph):
    numerator = 0
    denominator = 0
    for (u, v), prob in graph.items():
        if u in cluster and v in cluster:
            numerator += prob
        if u in cluster or v in cluster:
            denominator += prob
    if denominator == 0:
        return 0
    return numerator / denominator

def calculate_unifiability(cluster1, cluster2, graph):
    numerator = 0
    denominator = 0
    for (u, v), prob in graph.items():
        if u in cluster1 and v in cluster2:
            numerator += prob
        elif u in cluster1 and v not in cluster1:
            denominator += prob
        elif u not in cluster2 and v in cluster2:
            denominator += prob
    if denominator == 0:
        return 0
    return numerator / denominator

def calculate_anui(clusters, graph):
    avi = sum(calculate_isolatability(cluster, graph) for cluster in clusters) / len(clusters)
    avu = sum(calculate_unifiability(cluster1, cluster2, graph) for cluster1, cluster2 in itertools.combinations(clusters, 2)) / len(list(itertools.combinations(clusters, 2)))
    if avu == 0:
        return avi
    return avi / (1 + avi * avu)
