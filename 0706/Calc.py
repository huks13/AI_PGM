while True:
    print("\n=== 계산기 ===")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")

    menu = input("메뉴 선택: ")

    if menu == "5":
        print("프로그램을 종료합니다.")
        break

    if menu not in ["1", "2", "3", "4"]:
        print("잘못된 입력입니다.")
        continue

    num1 = float(input("첫 번째 숫자: "))
    num2 = float(input("두 번째 숫자: "))

    match menu:
        case "1":
            result = num1 + num2
            print(f"결과: {result}")

        case "2":
            result = num1 - num2
            print(f"결과: {result}")

        case "3":
            result = num1 * num2
            print(f"결과: {result}")

        case "4":
            if num2 == 0:
                print("0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
                print(f"결과: {result}")