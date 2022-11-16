from menu import *
from coffee import *

# TODO 실행 로직


def main():
    is_on = True

    while is_on:
        # 1. 프롬프트
        choice = input("어떤 커피를 원하세요? (아메리카노/라떼/카푸치노) ")
    # 2. 프롬프트에서 "off" 자판기가 종료됩니다.
        if choice == "off":
            is_on = False
    # 3. 프롬프트에서 "report" 입력받을 경우
        elif choice == "report":
            print(f"물: {resources['water']}ml")
            print(f"우유: {resources['milk']}ml")
            print(f"커피: {resources['coffee']}g")
            print(f"수익: {profit:,}원")
    # 4. 재료는 충분한지 체크
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                # 5. 재료가 충분하면, 돈을 받습니다.
                payment = process_cash(drink["cost"])
        # 6. "트랜잭션"이 성공적인지 체크
                if is_transaction_successful(payment, drink["cost"]):
                    # 7. 커피를 만듭니다.
                    make_coffe(choice, drink["ingredients"])


if __name__ == "__main__":
    main()