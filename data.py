def main():
    data = input('Please enter your string')
    return_data =convert(data)
    print('The original text is ',data)
    print('The converted text is',return_data)


def convert(data):
    bin_data = ''.join(format(ord(i),'b')for i in data)
    return bin_data


if __name__ =='__main__':
    main()

