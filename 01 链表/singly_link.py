class SinglyLinkNode(object):
    """定义单向链表结点"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLink(object):
    """单向链表"""
    def __init__(self):
        # 定义哨兵节点
        self.guard = SinglyLinkNode(None)

    def insert_value_to_head(self, data):
        """从头部插入值"""
        node = SinglyLinkNode(data)
        self.insert_node_to_head(node)

    def insert_node_to_head(self, node):
        """从头部插入结点"""
        node.next = self.guard.next
        self.guard.next = node

    def insert_value_to_tail(self, data):
        """从尾部插入值"""
        node = SinglyLinkNode(data)
        self.insert_node_to_tail(node)

    def insert_node_to_tail(self, node):
        """从尾部插入结点"""
        p = self.guard
        while p.next is not None:
            p = p.next
        p.next = node

    def find_node_by_index(self, index):
        """根据结点位置检索结点"""
        p = self.guard
        position = 0
        while p.next and position != index:
            position += 1
            p = p.next
        return p

    def find_node_by_value(self, value):
        """根据结点内容检索结点"""
        p = self.guard
        while p.next and p.data != value:
            p = p.next
        return  p

    def delete_node_by_index(self, index):
        """根据结点位置删除节点"""
        p = self.guard
        position = 0
        while p.next:
            if position == index:
                p.next = p.next.next
                break
            else:
                position += 1
                p = p.next

    def deleta_node_by_value(self, value):
        """根据结点值删除节点"""
        p = self.guard
        while p.next:
            if p.next.data == value:
                p.next = p.next.next
                break
            else:
                p = p.next

    def insert_value_after_value(self, value, new_value):
        """在某个节点值后面插入值"""
        p = self.guard
        while p.next and p.data != value:
            p = p.next

        self.insert_value_after_node(p, new_value)

    def insert_value_before_value(self, value, new_value):
        """在某个节点值前面插入值"""
        p = self.guard
        while p.next and p.next.data != value:
            p = p.next

        self.insert_value_after_node(p, new_value)

    def insert_value_by_index(self, index, new_value):
        """在某个节点位置插入值"""
        position = 0
        p = self.guard
        while p.next and position != index:
            p = p.next
            position += 1

        self.insert_value_after_node(p, new_value)

    @staticmethod
    def insert_value_after_node(node, new_value):
        """在节点后插入新的值"""
        new_node = SinglyLinkNode(new_value)
        new_node.next = node.next
        node.next = new_node

    @staticmethod
    def insert_node_after_node(node, new_node):
        """在节点后插入新节点"""
        new_node.next = node.next
        node.next = new_node

    def reverse(self):
        """链表反转"""
        head = self.guard.next
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        self.guard.next = pre

    def combine_link(self, singly_link):
        """合并两个有序列表"""
        h1 = self.guard.next
        h2 = singly_link.guard.next
        self.guard = SinglyLinkNode(None)
        current = self.guard

        while h1 or h2:
            if h1 is None:
                current.next = h2
                break

            if h2 is None:
                current.next = h1
                break

            if h1.data >= h2.data:
                current.next = h2
                h2 = h2.next
            else:
                current.next = h1
                h1 = h1.next
            current = current.next

    def find_last_n_node(self, n):
        """查找倒数第n个节点"""
        fast = self.guard
        slow = self.guard
        position = 0
        while fast.next is not None:
            if position == n:
                slow = slow.next
                fast = fast.next
            else:
                position += 1
                fast = fast.next
        return  slow

    def delete_last_n_node(self, n):
        """删除倒数第n个节点"""
        fast = self.guard
        slow = self.guard
        position = 0
        while fast.next is not None:
            if position == n + 1:
                slow = slow.next
                fast = fast.next
            else:
                position += 1
                fast = fast.next

        if position == n+1:
            slow.next = slow.next.next

    def find_mid_node(self):
        """查找链表的中间节点"""
        fast = self.guard
        slow = self.guard
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next is None:
            if slow.next is None:
                print("空链表无中间节点")
            else:
                print("中间节点的值：(%s, %s)" % (slow.data, slow.next.data))
            return

        if fast.next.next is None:
            print("中间节点的值：(%s)" % slow.next.data)

    def  find_cycle_length_point(self):
        """判断链表是否有环，若有环返回环的"长度和入环点"""
        has_cycle = False
        fast, slow = self.guard, self.guard

        while slow.next and fast.next and fast .next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break

        if not has_cycle:
            '''没有环时，返回环长度为0，入环点为-1 '''
            return 0, -1

        '''计算环长度，思想：slow步长为1，再次回到初始位置时为1圈'''
        position = 0
        slow_pos = slow
        while True:
            position += 1
            slow = slow.next
            if slow == slow_pos:
                break
        cycle_length = position

        '''寻找入环点，思路：fast提前环的长度出发，然后slow再出发，当他们相遇的时候即为入环点位置'''
        cycle_point = 0
        position = 0
        fast, slow = self.guard.next, self.guard.next
        while position < cycle_length:
            fast = fast.next
            position += 1
        while True:
            if slow == fast:
                return cycle_length, cycle_point
            cycle_point += 1
            slow, fast = slow.next, fast.next

    # 重写__iter__方法，方便for关键字调用打印值
    def __iter__(self):
        node = self.guard.next
        while node:
            yield node.data
            node = node.next

    def print_all(self):
        """打印链表"""
        for value in self:
            print(value, end = "->")
        print('')


if __name__ == '__main__':
    singly_link = SinglyLink()
    for i in range(10):
        singly_link.insert_value_to_tail(i)
    singly_link.print_all()

    # ------------------------- 链表查询 -------------------
    i = 4
    print("找到第 %s 个节点的值：%s" % (i, singly_link.find_node_by_index(i)))
    print("找到值为 %s 的节点的值：%s" % (i, singly_link.find_node_by_value(4)))

    # ------------------------- 链表增删 -------------------
    print("删除节点位置第 %s" % i)
    singly_link.delete_node_by_index(i)
    singly_link.print_all()
    i = 5
    print("删除节点值为 %s" % i)
    singly_link.deleta_node_by_value(i)
    singly_link.print_all()

    m, n = 6, 100
    print("在节点值为 %s 后面插入值 %s" % (m, n))
    singly_link.insert_value_after_value(m, n)
    singly_link.print_all()

    m, n = 6, 100
    print("在节点值为 %s 前面插入值 %s" % (m, n))
    singly_link.insert_value_before_value(m, n)
    singly_link.print_all()

    m, n = 6, 88
    print("把值 %s 插入节点位置 %s" % (n, m))
    singly_link.insert_value_by_index(m, n)
    singly_link.print_all()

    # ------------------------- 链表反转 -------------------
    print("链表反转")
    singly_link.reverse()
    singly_link.print_all()

    # -------------------------- 合并两个有序链表 ---------------
    print('\n合并两个有序链表')
    sl_1 = SinglyLink()
    for i in [0, 4]:
        sl_1.insert_value_to_tail(i)
    print("链表1：")
    sl_1.print_all()

    sl_2 = SinglyLink()
    for i in [1, 12]:
        sl_2.insert_value_to_tail(i)
    print("链表2：")
    sl_2.print_all()
    print("链表2合并到链表1后：")
    sl_1.combine_link(sl_2)
    sl_1.print_all()

    # -------------------------- 查找倒数第n个节点 ---------------
    print()
    singly_link = SinglyLink()
    for i in range(5):
        singly_link.insert_value_to_tail(i)
    singly_link.print_all()
    i = 1
    print("查找倒数第%s个节点值：%s" % (i, singly_link.find_last_n_node(i)))

    # -------------------------- 删除倒数第n个节点 ---------------
    singly_link.delete_last_n_node(i)
    print("删除倒数第 %s 个节点"  % i)
    singly_link.print_all()

    # -------------------------- 求链表的中间结点  ---------------
    singly_link.find_mid_node()

    # -------------------------- 检测链表是否有环和入环点  ---------------
    print("环长度：%s；入环点：%s" % (singly_link.find_cycle_length_point()))

    singly_link = SinglyLink()
    for _ in range(10):
        if _ == 3:
            pre = SinglyLinkNode(_)
            singly_link.insert_node_to_tail(pre)
        elif _ == 9:
            after = SinglyLinkNode(_)
            after.next = after
            singly_link.insert_node_to_tail(after)
        else:
            singly_link.insert_node_to_tail(SinglyLinkNode(_))
    print("环长度：%s；入环点：%s" % (singly_link.find_cycle_length_point()))
