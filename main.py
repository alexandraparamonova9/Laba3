from typing import Callable, Dict, List


def binary_tree(
    height: int,
    root: int,
    left_leaf : Callable[[int], int] = lambda x: 2 - (x - 1),
    right_leaf: Callable[[int], int] = lambda x: x * 2
) -> Dict[str, List]:
    """
    Рекурсивно создаёт бинарное дерево в виде словаря.

    Каждый узел дерева представлен в виде:
        {"значение_узла": [левое_поддерево, правое_поддерево]}

    Параметры:
        height (int): Высота дерева — количество шагов рекурсии.
                      Если height = 0, создаётся только корень.
        root (int): Начальное значение (корень дерева).
        left_leaf(Callable[[int], int]): Функция для вычисления левого потомка.
        right_leaf (Callable[[int], int]): Функция для вычисления правого потомка.

    Возвращает:
        Dict[str, List]: Словарь, представляющий бинарное дерево.
                         Ключ — строковое значение корня,
                         значение — список потомков (поддеревьев).
    """
    # Высота 0: только корень
    if height == 0:
        return {str(root): []}

    # Рекурсивное построение поддеревьев
    left = binary_tree(height - 1, left_leaf(root), left_leaf, right_leaf)
    right = binary_tree(height - 1, right_leaf(root), left_leaf, right_leaf)

    # Возвращаем текущий уровень дерева
    return {str(root): [left, right]}


if __name__ == "__main__":
    tree = binary_tree(4, 14, left_leaf=lambda x: 2 - (x - 1), right_leaf=lambda x: x * 2)
    print(tree)
