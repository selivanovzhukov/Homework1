import argparse


def shift(args) -> object:
    step = args.shift_element
    if step < 0:
        step = abs(step)
        for i in range(step):
            args.some_list.append(args.some_list.pop(0))
    else:
        for i in range(step):
            args.some_list.insert(0, args.some_list.pop())
    return args.some_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List shift')
    parser.add_argument('-some_list', nargs='+')
    parser.add_argument('-shift_element', type=int, default=4)
    args = parser.parse_args()
    shift_list = args
    print(shift(shift_list))
