# # Функция для расчета ROI
# def calculate_roi(initial_investment, final_value):
#     return ((final_value - initial_investment) / initial_investment) * 100
#
# # Функция для расчета NPV
# def calculate_npv(initial_investment, cash_flows, discount_rate):
#     npv = -initial_investment
#     npv += sum(cash_flow / (1 + discount_rate) ** (i + 1) for i, cash_flow in enumerate(cash_flows))
#     return npv
#
# # Пример использования функций
# initial_investment = 100000
# final_value = 150000
# cash_flows = [-10000, 20000, 25000, 30000, 35000]  # Пример денежных потоков
# discount_rate = 0.1
#
# roi = calculate_roi(initial_investment, final_value)
# npv = calculate_npv(initial_investment, cash_flows, discount_rate)
#
# print("ROI: {:.2f}%".format(roi))
# print("NPV: {:.2f}".format(npv))