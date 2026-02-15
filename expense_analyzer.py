# Автор: Александра Лебедева (github: alepew)
# Дата: Февраль 2026
# Проект: Анализатор расходов
# Описание: Программа для учёта трат с аналитикой
# ========================================

def privetstvie():
    print("="*50)
    print("Добро пожаловать в Анализатор расходов!".center(50))
    print("="*50)
    print("Эта программа поможет учесть твои траты :)")
    print("и проанализировать куда уходят деньги...\n")

def poluchit_traty():
    traty = []
    den = 1 # счётчик дней

    print("\nВВОД ДАННЫХ")
    print("Правила ввода:")
    print("- Вводи только числа (можно с копейками через точку)")
    print("- Если в день не было трат - просто нажми enter")
    print("- Для завершения введи 'стоп' или '0'\n")

    while True:
        vvod = input(f"День {den}:")

        if vvod.lower() == 'стоп' or vvod == '0':
            print("Ввод завершён")
            break

        if vvod == "":
            print("День без трат пропущен (вы там живы?)")
            den += 1
            continue
        
        try:
            vvod = vvod.replace(',','.')
            summa = float(vvod)
            if summa > 0:
                traty.append(summa)
                print(f"Добавлено: {summa} руб.")
            else:
                print("Сумма должна быть больше нуля!")
        except ValueError:
            print("Ошибка! Нужно ввести число (например: 500 или 1250.50)")
    return traty

def analizirovat_traty(traty):
    if not traty:
        return None
    
    analitika = {
        'obshaya_summa': sum(traty),
        'kolichestvo': len(traty),
        'sredniy_chek': sum(traty) / len(traty),
        'max_trata': max(traty),
        'min_trata': min(traty)
    }
    return analitika

def pokazat_otchet(analitika, traty):
    print("\n" + "=" * 50)
    print("ОТЧЕТ ПО РАСХОДАМ".center(50))
    print("=" * 50)

    if analitika is None:
        print("Нет данных для анализа")
        return
    
    print(f"Общая сумма: {analitika['obshaya_summa']:>10,.2f} руб.")
    print(f"Количество трат: {analitika['kolichestvo']:>10}")
    print(f"Средний чек: {analitika['sredniy_chek']:>10,.2f} руб.")
    print(f"Самая крупная: {analitika['max_trata']:>10,.2f} руб.")
    print(f"Самая минимальная: {analitika['min_trata']:>10,.2f} руб.")

    print("\nТраты по убыванию:")
    sortirovannye = sorted(traty, reverse=True)
    for i, summa in enumerate(sortirovannye[:5], 1):
        print(f"  {i}. {summa:>10,.2f} руб.")
    
    print("\nАНАЛИТИЧЕСКИЙ ВЫВОД:")
    if analitika['sredniy_chek'] > 5000:
        print("Средний чек высокий. Возможно, есть крупные покупки?")
    elif analitika['sredniy_chek'] < 500:
        print("Средний чек низкий. Хорошо контролируете свои траты!")
    else:
        print("Средний чек в норме.")

    print("=" * 50)

def sohranit_otchet(analitika, traty):
    try:
        with open('otchet.txt', 'w', encoding='utf-8') as file:
            file.write("ОТЧЕТ ПО РАСХОДАМ\n")
            file.write("=" * 30 + "\n")
            file.write(f"Общая сумма: {analitika['obshaya_summa']:.2f} руб.")
            file.write(f"Количество трат: {analitika['kolichestvo']}\n")
            file.write(f"Средний чек: {analitika['sredniy_chek']:.2f} руб.\n")
            file.write(f"Все траты: {traty}\n")

        print("\nОтчет сохранен в файл 'otchet.txt'")
    except:
        print("\nНе удалось сохранить файл)")

def main():
    privetstvie()
    traty = poluchit_traty()
    analitika = analizirovat_traty(traty)
    pokazat_otchet(analitika, traty)

    if analitika: 
        otvet = input("\nСохранить отчет в файл? (да\нет): ")
        if otvet.lower() in ['да', 'yes', 'y', 'lf']:
            sohranit_otchet(analitika, traty)

    print("\nСпасибо за использование Анализатора данных!")

if __name__ == "__main__":
    main()