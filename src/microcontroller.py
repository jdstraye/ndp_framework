from enum import Enum
import logging

class INST(Enum):
    MAC = 0
    MPY = 1
    ADD = 2
    SUB = 3
    LDB = 4
    STB = 5
    NOP = 6
    LOG = 7

class RegisterFile:
    def __init__(self, size: int = 16):
        self.__registers = [0] * size

    # Operations on the entire register, e.g. registers = [1, 2, 3, 4]
    @property
    def registers(self):
        return self.__registers
    
    # Operations on an index, e.g. registers[2] = 5
    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.__registers):
            raise IndexError("Register index out of range")
        self.__registers[index] = value

    def __getitem__(self, index):
        if index < 0 or index >= len(self.__registers):
            raise IndexError("Register index out of range")
        return self.__registers[index]


class Memory:
    def __init__(self, size: int = 1024):
        self.__memory = [0] * size

    def __setitem__(self, address, value):
        if address < 0 or address >= len(self.__memory):
            raise IndexError("Memory address out of range")
        self.__memory[address] = value

    def __getitem__(self, address):
        if address < 0 or address >= len(self.__memory):
            raise IndexError("Memory address out of range")
        return self.__memory[address]



class ALU:
    def mac(self, a, b, acc):
        return a * b + acc

    def mpy(self, a, b):
        return a * b

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

class Microcontroller:
    def __init__(self, memory_size=1024, register_file_size=16):
        self.__pc = 0
        self.__memory = Memory(memory_size)
        self.__acc = 0 # Typical location of the ALU result
        self.__register_file = RegisterFile(register_file_size)
        self.__alu = ALU()

    @property
    def pc(self):
        return self.__pc

    @pc.setter
    def pc(self, value):
        self.__pc = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    @property
    def acc(self):
        return self.__acc

    @acc.setter
    def acc(self, value):
        self.__acc = value

    @property
    def register_file(self):
        return self.__register_file

    @register_file.setter
    def register_file(self, value):
        self.__register_file = value

    def fetch_instruction(self):
        instruction = self.__memory[self.__pc]
        opcode = instruction >> 4
        arguments = instruction & 0x0F
        return opcode, arguments

    def execute_instruction(self, instruction, *args):
        if instruction == INST.MAC:
            self.__acc = self.__alu.mac(self.__register_file[args[0]], self.__register_file[args[1]], self.__acc)
        elif instruction == INST.MPY:
            self.__acc = self.__alu.mpy(self.__register_file[args[0]], self.__register_file[args[1]])
        elif instruction == INST.ADD:
            self.__acc = self.__alu.add(self.__register_file[args[0]], self.__register_file[args[1]])
        elif instruction == INST.SUB:
            self.__acc = self.__alu.sub(self.__register_file[args[0]], self.__register_file[args[1]])
        elif instruction == INST.LDB:
            self.__register_file[args[0]] = self.__memory[args[1]]
        elif instruction == INST.STB:
            self.__memory[args[0]] = self.__register_file[args[1]]
        elif instruction == INST.NOP:
            pass
        elif instruction == INST.LOG:
            logging.info(f"Logging: {args}")

    def step(self):
        instruction = self.fetch_instruction()
        (opcode, arguments) = instruction
        self.execute_instruction(opcode, arguments)
        self.__pc += 1