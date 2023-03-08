import matplotlib.pyplot as plt

def convex_hull(points):
    # Jika titik kurang dari 3 maka tidak dapat membentuk convex hull
    if len(points) < 3:
        return []
    
    # Menentukan titik terkiri (paling kecil x) dan mengurutkan titik berdasarkan sudutnya terhadap titik terkiri
    leftmost_point = min(points, key=lambda point: point[0])
    sorted_points = sorted(points, key=lambda point: (leftmost_point[0]-point[0])/(leftmost_point[1]-point[1]) if leftmost_point[1]-point[1] != 0 else float('inf'))
    
    # Menginisialisasi stack dan menambahkan 2 titik awal ke stack
    stack = [sorted_points[0], sorted_points[1]]
    
    # Loop untuk mengecek apakah titik yang akan ditambahkan akan membentuk convex atau tidak
    for i in range(2, len(sorted_points)):
        top = stack[-1]
        second_top = stack[-2]
        while (top[0]-second_top[0])*(sorted_points[i][1]-top[1])-(top[1]-second_top[1])*(sorted_points[i][0]-top[0]) <= 0:
            stack.pop()
            if len(stack) < 2:
                break
            top = stack[-1]
            second_top = stack[-2]
        stack.append(sorted_points[i])
        
    # Menghasilkan list of line dari stack
    lines = []
    for i in range(len(stack)-1):
        lines.append((stack[i], stack[i+1]))
    lines.append((stack[-1], stack[0]))
    
    return lines
    
# Contoh penggunaan
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
lines = convex_hull(points)
print("output : ", lines)

# Menghasilkan gambar dari convex hull
x, y = zip(*points)
plt.scatter(x, y)
for line in lines:
    x, y = zip(*line)
    plt.plot(x, y)
plt.show()