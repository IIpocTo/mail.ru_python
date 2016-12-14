months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def get_month_name(month):
    return months[month]


def transform_data(variables, acc=None):
    if len(variables) == 0:
        return acc
    else:
        year, month, total = variables.pop(-1)
        if acc is None:
            acc = {year: {get_month_name(month): total}}
        else:
            if acc.get(year) is not None:
                if get_month_name(month) not in acc[year]:
                    acc[year][get_month_name(month)] = total
            else:
                acc[year] = {get_month_name(month): total}
        acc_new = transform_data(variables, acc)
        return acc_new
