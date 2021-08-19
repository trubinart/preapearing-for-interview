offer_1 = {'begin_sum': 1000,
           'end_sum': 10000,
           '6': 0.5,
           '12': 0.6,
           '24': 0.5}

offer_2 = {'begin_sum': 10000,
           'end_sum': 100000,
           '6': 0.6,
           '12': 0.7,
           '24': 0.65}

offer_3 = {'begin_sum': 100000,
           'end_sum': 1000000,
           '6': 0.7,
           '12': 0.8,
           '24': 0.75}

offer_list = [offer_1, offer_2, offer_3]

def deposit(amount, time):
    num = 0

    for offer in offer_list:
        num += 1
        if amount > offer['begin_sum'] and amount < offer['end_sum']:
            if time < 6:
                interest_rate = offer['6']
            elif time > 6 and  time < 24:
                interest_rate = offer['12']
            else:
                interest_rate = offer['24']
            final_summ = amount * (1 + interest_rate) ** (interest_rate / time)
            print(int(final_summ))

        if amount > offer['end_sum'] and num == len(offer_list):
            interest_rate = offer['24']
            final_summ = amount * (1 + interest_rate) ** (interest_rate / time)
            print(int(final_summ))

if __name__ == "__main__":
    deposit(19000000, 15)
