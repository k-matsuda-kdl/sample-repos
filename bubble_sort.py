def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()  # 元の配列を壊さないようにコピー

    print("初期状態:", a)

    for i in range(n):
        print(f"\n--- {i+1}回目のループ ---")

        for j in range(0, n - i - 1):
            print(f"比較: {a[j]} と {a[j+1]}", end="")

            if a[j] > a[j + 1]:
                # 交換
                a[j], a[j + 1] = a[j + 1], a[j]
                print(" → 交換")
            else:
                print(" → そのまま")

            print("現在の配列:", a)

        print(f"{i+1}回目終了:", a)

    return a


# 実行
if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    sorted_data = bubble_sort(data)

    print("\n最終結果:", sorted_data)