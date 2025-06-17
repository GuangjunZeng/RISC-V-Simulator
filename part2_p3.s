.globl _start

_start:
    li a1, 1
    li a2, 2
    li a3, 0
    li a4, 16
    mul a6, a2, a1
    sw a6, 0x12(zero)
    li a6, 2048
    sw a6, 0x36(zero)
    li a6, 10
    sw a6, 0x20(zero)
    li x8, 0
    li x5, 4
    li x6, 1
    li x7, 1

loop:
    lw a5, 0x20(zero)

    # fmadd.i a3, a1, a2, a3
    .word 0x0686858B

    addi x8, x6, 0
    add x6, x7, x6
    addi a5, a5, 1
    addi a1, a1, 1
    addi a2, a2, 1
    sw a5, 0x20(zero)
    add x7, zero, x6
    lw a5, 0x12(zero)

    # fmadd.i a6, x8, a3, a3
    .word 0x06868C0B

    lw x8, 0x36(zero)
    nop
    addi a5, a5, 1
    andi x1, x8, 1
    nop
    sw a5, 0x12(zero)
    beq x1, zero, f2

f1:
    addi x8, x8, -1
    j end_condition

f2:
    srli x8, x8, 1

end_condition:
    sw x8, 0x36(zero)
    bnez x8, loop

    li a7, 93
    ecall
