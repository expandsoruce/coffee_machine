# TODO 커피머신 만들기
# 수익
profit = 0

# 자판기에 있는 재료 자원
resources = {
    "water": 700,
    "milk": 300,
    "coffee": 200,
}


def is_resource_sufficient(order_ingredient):
    """Bool을 반환, 재료가 충분한지 확인하는 함수"""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"{item}이 부족합니다.")
            return False
    return True


def process_cash(drink_cost):
    """전체 받은 금액을 반환, 음료의 가격을 입력받고, 지폐, 동전의 개수를 입력받는 함수"""
    cash_list = [10000, 5000, 1000, 500, 100, 50, 10]
    total = 0
    for cash in cash_list:
        if total < drink_cost:
            total += int(input(f"{cash:,}원짜리 몇 개입니까? : ")) * cash
    return total


def is_transaction_successful(money_received, drink_cost):
    "불린 반환, 트랜잭션이 성공적으로 이루어졌는지 체크하는 함수"
    if money_received >= drink_cost:
        change = money_received - drink_cost
        if change:
            print(f"거스름돈 {change}원이 있습니다.")
        global profit
        profit += drink_cost
        return True
    else:
        print("돈이 충분하지 않습니다. 넣은 돈 다 돌려드립니다.")
        return False


def make_coffe(drink_name, ingredients):
    """재료를 소모하여 커피를 만드는 함수"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"여기 {drink_name} 나왔습니다. ☕ 즐거운 시간되세요!")
