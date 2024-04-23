# import asyncio  # Добавляем импорт asyncio
#
# import unittest
# import functional_components
#
# class TestFunctionalComponents(unittest.TestCase):
#
#     async def test_add(self):  # Добавляем аннотацию асинхронного вызова
#         self.assertEqual(functional_components.add(3, 5), 8)
#         self.assertEqual(functional_components.add(-1, 1), 0)
#         self.assertEqual(functional_components.add(0, 0), 0)
#
#     async def test_subtract(self):  # Добавляем аннотацию асинхронного вызова
#         self.assertEqual(functional_components.subtract(5, 3), 2)
#         self.assertEqual(functional_components.subtract(1, -1), 2)
#         self.assertEqual(functional_components.subtract(0, 0), 0)
#
#     async def test_multiply(self):  # Добавляем аннотацию асинхронного вызова
#         self.assertEqual(functional_components.multiply(3, 5), 15)
#         self.assertEqual(functional_components.multiply(-1, 1), -1)
#         self.assertEqual(functional_components.multiply(0, 5), 0)
#
#     async def test_divide(self):  # Добавляем аннотацию асинхронного вызова
#         self.assertEqual(functional_components.divide(10, 2), 5)
#         self.assertEqual(functional_components.divide(-10, 2), -5)
#         self.assertEqual(functional_components.divide(0, 5), 0)
#
#         with self.assertRaises(ValueError):
#             functional_components.divide(10, 0)
#
# if __name__ == '_main_':
#     unittest.main()
