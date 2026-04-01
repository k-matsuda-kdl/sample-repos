def quicksort(arr, depth=0):
    indent = "  " * depth  # 再帰の深さに応じてインデント

    print(f"{indent}入力: {arr}")

    if len(arr) <= 1:
        print(f"{indent}そのまま返す: {arr}")
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"{indent}pivot: {pivot}")
    print(f"{indent}left : {left}")
    print(f"{indent}middle: {middle}")
    print(f"{indent}right: {right}")

    # 再帰
    result = quicksort(left, depth + 1) + middle + quicksort(right, depth + 1)

    print(f"{indent}結合結果: {result}")
    return result


# 実行
if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    sorted_data = quicksort(data)
    print("\n最終結果:", sorted_data)