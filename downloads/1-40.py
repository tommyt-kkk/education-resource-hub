def read_complex(prompt):
    """
    读取复数，支持 i 或 j 作为虚数单位
    """
    while True:
        s = input(prompt).strip()
        s = s.replace(" ", "")
        s = s.replace("i", "j")
        try:
            return complex(s)
        except ValueError:
            print("输入格式错误，请重新输入，例如：1+2i, 3-4i, 5, -2i")


def print_complex(z):
    """
    更友好地输出复数
    """
    a = z.real
    b = z.imag

    eps = 1e-10
    if abs(a) < eps:
        a = 0
    if abs(b) < eps:
        b = 0

    if b == 0:
        return f"{a:.6g}"
    elif a == 0:
        return f"{b:.6g}i"
    elif b > 0:
        return f"{a:.6g}+{b:.6g}i"
    else:
        return f"{a:.6g}{b:.6g}i"


def solve_linear_system(A, b):
    """
    使用高斯消元法解复数线性方程组 Ax = b
    """
    n = len(A)

    # 构造增广矩阵
    M = [A[i] + [b[i]] for i in range(n)]

    eps = 1e-12

    # 高斯消元
    for col in range(n):
        # 寻找主元
        pivot = col
        for row in range(col + 1, n):
            if abs(M[row][col]) > abs(M[pivot][col]):
                pivot = row

        if abs(M[pivot][col]) < eps:
            return None  # 没有唯一解

        # 交换行
        M[col], M[pivot] = M[pivot], M[col]

        # 主元行归一化
        pivot_value = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= pivot_value

        # 消去其他行
        for row in range(n):
            if row != col:
                factor = M[row][col]
                for j in range(col, n + 1):
                    M[row][j] -= factor * M[col][j]

    # 提取解
    x = [M[i][n] for i in range(n)]
    return x


def main():
    print("复数一次方程组求解程序")
    print("最多支持 4 个未知数")
    print("复数可以输入为：1+2i, 3-4i, 5, -2i")
    print()

    while True:
        try:
            n = int(input("请输入未知数个数："))
            if 1 <= n <= 4:
                break
            else:
                print("未知数个数必须在 1 到 4 之间。")
        except ValueError:
            print("请输入整数。")

    A = []
    b = []

    print()
    print(f"你需要输入 {n} 个方程的系数。")
    print("假设未知数为 x1, x2, x3, x4 ...")
    print()

    for i in range(n):
        print(f"请输入第 {i + 1} 个方程：")

        row = []
        for j in range(n):
            coef = read_complex(f"  x{j + 1} 的系数：")
            row.append(coef)

        const = read_complex("  方程右端常数项：")

        A.append(row)
        b.append(const)

        print()

    result = solve_linear_system(A, b)

    if result is None:
        print("该方程组没有唯一解，可能无解或有无穷多解。")
    else:
        print("方程组的解为：")
        for i, value in enumerate(result):
            print(f"x{i + 1} = {print_complex(value)}")


if __name__ == "__main__":
    main()