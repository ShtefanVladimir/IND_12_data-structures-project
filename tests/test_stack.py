"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from unittest import TestCase

from src.stack import Node, Stack


class NodeTestCase(TestCase):
    def setUp(self):
        self.n1 = Node(5, None)
        self.n2 = Node('a', self.n1)

    def test_get_data_from_node(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'a')

    def test_id_node(self):
        self.assertIs(self.n1, self.n2.next_node)


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertIsNone(self.stack.top.next_node.next_node.next_node)

        with self.assertRaises(AttributeError):
            _ = self.stack.top.next_node.next_node.next_node.data

    def test_pop(self):
        self.stack.push('data1')
        data = self.stack.pop()

        self.assertIsNone(self.stack.top)
        self.assertEqual(data, 'data1')

        self.stack.push('data1')
        self.stack.push('data2')
        data = self.stack.pop()

        self.assertEqual(self.stack.top.data, 'data1')
        self.assertEqual(data, 'data2')
