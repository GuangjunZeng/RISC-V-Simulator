import sys

reg_map = {
    "zero": 0, "ra": 1, "sp": 2, "gp": 3, "tp": 4,
    "t0": 5, "t1": 6, "t2": 7,
    "s0": 8, "fp": 8, "s1": 9,
    "a0": 10, "a1": 11, "a2": 12, "a3": 13, "a4": 14, "a5": 15, "a6": 16, "a7": 17,
    "s2": 18, "s3": 19, "s4": 20, "s5": 21, "s6": 22, "s7": 23, "s8": 24, "s9": 25, "s10": 26, "s11": 27,
    "t3": 28, "t4": 29, "t5": 30, "t6": 31
}

# allow x0-x31 too
for i in range(32):
    reg_map[f'x{i}'] = i

def encode_fmadd_i(rd, rs1, rs2, rs3, funct2=0):
    opcode = 0b0001011  # 0x0B
    funct3 = 0b000      # fixed
    inst = (
        (rs3   << 27) |
        (funct2 << 25) |
        (rs2   << 20) |
        (rs1   << 15) |
        (funct3 << 12) |
        (rd    << 7) |
        opcode
    ) & 0xFFFFFFFF  # ✅ force 32-bit unsigned
    return inst

def main():
    if len(sys.argv) != 5:
        print("Usage: python gen_fmadd_word.py <rd> <rs1> <rs2> <rs3>")
        sys.exit(1)

    try:
        rd   = reg_map[sys.argv[1]]
        rs1  = reg_map[sys.argv[2]]
        rs2  = reg_map[sys.argv[3]]
        rs3  = reg_map[sys.argv[4]]
    except KeyError as e:
        print(f"Unknown register: {e}")
        sys.exit(1)

    inst = encode_fmadd_i(rd, rs1, rs2, rs3)
    print(f".word 0x{inst:08X}")

if __name__ == "__main__":
    main()

