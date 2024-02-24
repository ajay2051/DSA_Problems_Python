# Create management hierarchy of a company

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.name + self.designation)
        for child in self.children:
            child.print_tree()


def build_management_tree():
    root = TreeNode(" Ajay ", " CEO ")

    dept_head = TreeNode(" Binod ", " Department Head ")
    dept_head.add_child(TreeNode(" Bishal ", " Developer "))

    cto = TreeNode(" Mike ", " CTO ")
    cto.add_child(TreeNode(" John ", " Tester "))

    root.add_child(dept_head)
    root.add_child(cto)

    root.print_tree()


if __name__ == "__main__":
    build_management_tree()
