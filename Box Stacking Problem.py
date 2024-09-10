class Box:
    # Representation of a box
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self, other):
        return self.d * self.w < other.d * other.w

def maxStackHeight(arr, n):
    # Create an array of all rotations of the given boxes
    rot = [Box(0, 0, 0) for _ in range(3 * n)]
    index = 0

    for i in range(n):
        # Copy the original box
        rot[index].h = arr[i].h
        rot[index].d = max(arr[i].d, arr[i].w)
        rot[index].w = min(arr[i].d, arr[i].w)
        index += 1

        # First rotation of the box
        rot[index].h = arr[i].w
        rot[index].d = max(arr[i].h, arr[i].d)
        rot[index].w = min(arr[i].h, arr[i].d)
        index += 1

        # Second rotation of the box
        rot[index].h = arr[i].d
        rot[index].d = max(arr[i].h, arr[i].w)
        rot[index].w = min(arr[i].h, arr[i].w)
        index += 1

    # Now the number of boxes is 3n
    n *= 3

    # Sort the array 'rot[]' in non-increasing order of base area
    rot.sort(reverse=True)

    # Initialize msh values for all indexes
    msh = [0] * n

    for i in range(n):
        msh[i] = rot[i].h

    # Compute optimized msh values in bottom-up manner
    for i in range(1, n):
        for j in range(0, i):
            if (rot[i].w < rot[j].w and rot[i].d < rot[j].d):
                if msh[i] < msh[j] + rot[i].h:
                    msh[i] = msh[j] + rot[i].h

    maxm = -1
    for i in range(n):
        maxm = max(maxm, msh[i])

    return maxm

def input_boxes():
    print("Enter the number of boxes:")
    n = int(input().strip())
    boxes = []

    for i in range(n):
        while True:
            try:
                print(f"Enter dimensions for box {i + 1} (height width depth):")
                dimensions = input().strip().split()
                if len(dimensions) != 3:
                    raise ValueError("You must enter exactly three values.")
                h, w, d = map(int, dimensions)
                boxes.append(Box(h, w, d))
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please enter three integer values separated by spaces.")

    return boxes, n

if __name__ == "__main__":
    boxes, n = input_boxes()
    print("The maximum possible height of stack is", maxStackHeight(boxes, n))
