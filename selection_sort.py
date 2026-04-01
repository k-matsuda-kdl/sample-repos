def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    print("初期状態:", a)

    for i in range(n):
        min_index = i
        print(f"\n--- {i+1}回目 ---")
        print(f"開始位置 {i} の値: {a[i]}")

        # 最小値を探す
        for j in range(i + 1, n):
            print(f"比較: {a[min_index]} と {a[j]}")
            if a[j] < a[min_index]:
                min_index = j
                print(f"→ 新しい最小値: {a[min_index]} (index {min_index})")

        # 最小値を先頭と交換
        print(f"交換: {a[i]} と {a[min_index]}")
        a[i], a[min_index] = a[min_index], a[i]

        print("現在の配列:", a)

    return a


# 実行
if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    sorted_data = selection_sort(data)

    print("\n最終結果:", sorted_data)