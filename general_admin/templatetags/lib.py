from django.utils.http import urlquote


# a = urlquote('脚本分享网')


def parse_filter_kwargs(kwargs):
    # kwargs: {'title':1,'price':12000}
    # return: title=1&price=12000
    l = []

    for k, v in kwargs.items():
        l.append('%s=%s' % (k, urlquote(v)))
    return '&'.join(l)


def get_arg_value(a, str_list):
    for i in str_list:
        try:
            if abs(int(i)) == abs(a):
                return i
        except:
            continue
    return None


def get_arg_index(a, str_list):
    for i in range(len(str_list)):
        try:
            if abs(int(str_list[i])) == abs(a):
                return i
        except:
            continue
    return None


def remove_previous_field(filter_dict, field):
    if field in filter_dict:
        del filter_dict[field]


if __name__ == '__main__':
    print('hello')

    print('love')
    print('fuck')

    for i in range(10):
        print(i)
