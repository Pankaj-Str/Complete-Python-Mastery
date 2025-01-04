import heapq
import matplotlib.pyplot as plt

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[False] * cols for _ in range(rows)]
    distance = [[float('inf')] * cols for _ in range(rows)]

    pq = [(0, start)]
    distance[start[0]][start[1]] = 0

    while pq:
        dist, current = heapq.heappop(pq)
        x, y = current

        if current == end:
            break

        if visited[x][y]:
            continue

        visited[x][y] = True

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
                new_dist = dist + 1
                if new_dist < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_dist
                    heapq.heappush(pq, (new_dist, (new_x, new_y)))

    return distance, visited

def retrieve_path(maze, distances, visited, start, end):
    path = []
    x, y = end
    while (x, y) != start:
        path.append((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and visited[new_x][new_y] and distances[new_x][new_y] == distances[x][y] - 1:
                x, y = new_x, new_y
                break
    path.append(start)
    return path[::-1]

def visualize_maze(maze, path):
    rows, cols = len(maze), len(maze[0])
    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 1:
                plt.fill_between([y, y + 1], rows - x - 1, rows - x, color='black')
    
    for x, y in path:
        plt.fill_between([y, y + 1], rows - x - 1, rows - x, color='green')

    plt.xlim(0, cols)
    plt.ylim(0, rows)
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_point = (0, 0)
    end_point = (4, 4)

    distances, visited = dijkstra(maze, start_point, end_point)
    shortest_path = retrieve_path(maze, distances, visited, start_point, end_point)

    visualize_maze(maze, shortest_path)
