from typing import Dict, Union, Optional


TreeNode = Dict[str, Union[int, "TreeNode", None]]


def gen_bin_tree(height: int, root: int) -> Optional[TreeNode]:
    '''
    Рекурсивно строит бинарное дерево в виде словаря.

    Каждый узел дерева имеет ключи:
        value: значение узла
        left: левый потомок
        right: правый потомок

    Левый и правый потомок вычисляются по формулам:
        left  = 2 - (root - 1)
        right = root * 2
        height (int): Высота дерева (количество уровней).
        root (int): Значение в корне дерева.
        Optional[TreeNode]: Словарь, представляющий бинарное дерево,
                            или None, если высота дерева <= 0.

        >>> gen_bin_tree(2, 14)
        {
            'value': 14,
            'left': {'value': -11, 'left': None, 'right': None},
            'right': {'value': 28, 'left': None, 'right': None}
        }
    '''
    if height <= 0:
        return None

    left_val = 2 - (root - 1)
    right_val = root * 2

    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_val),
        "right": gen_bin_tree(height - 1, right_val),
    }

