### Dijkstra.py
One example of a complicated problem that can be solved using Python is finding the shortest path in a graph. Here's an example of how to implement Dijkstra's algorithm for finding the shortest path in a graph.
In this code, we first initialize the distances to all nodes in the graph as infinity except for the starting node, which we set to 0. We also initialize an empty set of visited nodes and a heap containing the starting node with a distance of 0.

We then enter a loop that continues as long as there are nodes in the heap. In each iteration, we extract the node with the smallest distance from the heap using heapq.heappop(). If the node has already been visited, we skip it and continue to the next node. Otherwise, we add the node to the set of visited nodes and iterate over its neighbors. For each neighbor, we calculate the new distance as the sum of the distance to the current node and the weight of the edge connecting the nodes. If the new distance is less than the current distance to the neighbor, we update the distance and add the neighbor to the heap with the new distance.

Finally, we return the distances to all nodes in the graph from the starting node.

Note that this code assumes that the graph is represented as a dictionary of dictionaries, where each inner dictionary contains the neighbors and weights of a node.

### Leetcode 3rd solution
To find the length of the longest substring without repeating characters, we can use the sliding window technique. We can maintain a window of characters in the string and move the window from left to right while keeping track of the characters in the window. If we encounter a character that is already in the window, we move the left end of the window to the right until the duplicate character is removed from the window. 

In this code, we start with an empty set window and a left index left pointing to the start of the string. We iterate over the characters of the string using a right index right. For each character s[right], we check if it is already in the window. If it is, we remove the character at left from the window and move left one step to the right. We continue this process until there are no more duplicate characters in the window. We add s[right] to the window, update the maximum length max_len if necessary, and continue to the next character.

Finally, we return the maximum length of any substring without repeating characters.
