class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        # If the color is already the same, nothing to do.
        if original == color:
            return image

        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color   # mark as visited by changing the color

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Visit only cells with the original color
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        q.append((nr, nc))

        return image

        

        
        