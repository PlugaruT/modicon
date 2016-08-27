from modicon import Modicon

if __name__ == '__main__':
    m = Modicon()

    result = m.get_all_bits_state()
    print(result)

