from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from struct import pack, unpack
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from modicon.registers import REG
from modicon.bitmap import BITMAP


SLAVE_ID = 1


class Modicon(object):
    def __init__(self, port='/dev/ttyUSB0'):
        self.client = ModbusClient(method='rtu', port=port, timeout=1,
                                   stopbits=1, baudrate=19200, bytesize=8)
        self.client.connect()
        self.data_type_switcher = {
            'REAL': self.read_float_value,
            'DWORD': self.read_dword_value,
            'WORD': self.read_word_value,
            'INT': self.read_int_value,
            'SINT': self.read_sint_value,
        }

    def _get_holding_register_first(self, address, count):
        """
        Retrieve value from required register
        :param address: starting address to read from
        :param count: number of registers to read
        :return: array of values from register
        """
        raw = self.client.read_holding_registers(address, count, unit=SLAVE_ID)
        return raw.registers

    @staticmethod
    def convert_float_value(arr):
        """
        Convert values from register array
        :param arr: array of values to convert
        :return: value after converting
        """
        # because pymodbus by default returns all integers
        # as unsigned, to extract the float value from register,
        # we have to pack the values as unsigned int
        # and then unpack the sum of values as float
        val_1 = pack('H', arr[0])
        val_2 = pack('H', arr[1])
        total = unpack('f', val_1 + val_2)
        return total[0]

    def read_register_value(self, register):
        """
        Function for reading values from required register
        :param register: name of register to read from
        :return: value from register
        """
        address = REG[register][0]
        size = REG[register][1]
        data_type = REG[register][2]
        return self.data_type_switcher[data_type](address, size)

    def read_float_value(self, address, size):
        """
        Function for reading float values from register
        :param address: starting address to read from
        :param size: number of bytes to read
        :return: float value
        """
        value = self._get_holding_register_first(address, size)
        return self.convert_float_value(value)

    def read_int_value(self, address, size):
        """
        Function for reading integer values from register
        :param address: starting address to read from
        :param size: number of bytes to read
        :return: integer value
        """
        return self._get_holding_register_first(address, size)[0]

    def read_dword_value(self, address, size):
        """
        Function for reading double word values from register
        :param address: starting address to read from
        :param size: number of bytes to read
        :return: array of booleans
        """
        result = []
        value = self._get_holding_register_first(address, size)
        total = value[0] << 16
        total += value[1]
        binary_str = bin(total)[2:].zfill(32)
        result.extend([True if bit == '1' else False for bit in binary_str])
        return result

    def read_sint_value(self, address, size):
        """
        Function for reading signed integer values from register
        :param address: starting address to read from
        :param size: number of bytes to read
        :return: integer value
        """
        value = self._get_holding_register_first(address, size)
        # first we pack the value in unsigned int
        # then we unpack to the value to signed int to get real value
        raw = pack('H', value[0])
        result = unpack('h', raw)
        return result[0]

    def read_word_value(self, address, size):
        """
        Function for reading values from register
        :param address: starting address to read from
        :param size: number of bytes to read
        :return: integer value
        """
        return self._get_holding_register_first(address, size)[0]

    @staticmethod
    def word_to_bitmap(number):
        """
        Function for converting a integer to a 16 bitmap array
        :param number: value to convert to bitmap
        :return: array of booleans
        """
        result = []
        binary_str = bin(number)[2:].zfill(16)
        result.extend([True if bit == '1' else False for bit in binary_str])
        return result

    def get_bit_state(self, bit_name):
        """
        Function for retrieving specific bit state
        :param bit_name: name of needed bit
        :return: state of bit, boolean
        """
        bit_number = 0
        bit_register_name = ''
        for reg in BITMAP:
            if bit_name in BITMAP[reg].keys():
                bit_number = BITMAP[reg][bit_name]
                bit_register_name = reg
        reg_address = REG[bit_register_name][0]
        reg_size = REG[bit_register_name][1]
        value = self.read_dword_value(reg_address, reg_size)
        return value[bit_number]

    def get_all_bits_state(self):
        """
        Function for retrieving states of all bits
        :return: dict with all bits state
        """
        result = {}
        for reg in BITMAP:
            for bit in BITMAP[reg].keys():
                result[bit] = self.get_bit_state(bit)
        return result

    def get_bits_states_from_reg(self, reg_name):
        """
        Function for retrieving states of bits from
        specific register
        :param reg_name: name of register to read from
        :return: dict with all bits state
        """
        result = {}
        for bit in BITMAP[reg_name]:
            result[bit] = self.get_bit_state(bit)
        return result
