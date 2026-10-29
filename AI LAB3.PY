graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):
if node == goal:
     return "FOUND", path
if limit == 0:
        if graph[node]:
return "CUTOFF", None
        return "FAILURE", None
cutoff_found = False

    for next_node in graph[node]:
        if next_node not in path:
            status, result = dls(
                next_node, goal, limit - 1,
                path + [next_node]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff_found = True

    if cutoff_found:
        return "CUTOFF", None

    return "FAILURE", None


for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("Limit:", limit, "| Status:", status, "| Path:", path)