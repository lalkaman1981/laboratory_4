"""
gives a statistics about Olegs day
"""

import matplotlib.pyplot as plt
import laboratory_4.oleg as oleg


def test(days):
    """
    test days of Oleg
    """
    lst_doom, lst_study, lst_sleep = [], [], []
    lst_days = []

    for i in range(days):
        doom, study, sleep = oleg.oleg_day(24)

        lst_doom.append(doom)
        lst_study.append(study)
        lst_sleep.append(sleep)
        lst_days.append(i + 1)

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].plot(lst_days, lst_doom, marker='o', linestyle='-')
    axs[0].set_xlabel('Days')
    axs[0].set_ylabel('Hours in Doom')
    axs[0].grid(True)

    axs[1].plot(lst_days, lst_study, marker='o', linestyle='-')
    axs[1].set_xlabel('Days')
    axs[1].set_ylabel('Study hours')
    axs[1].grid(True)

    axs[2].plot(lst_days, lst_sleep, marker='o', linestyle='-')
    axs[2].set_xlabel('Days')
    axs[2].set_ylabel('Sleep hours')
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test(90)
