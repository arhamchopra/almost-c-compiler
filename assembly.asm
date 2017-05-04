.data
	newline: .asciiz "\n"
	spacebar: .asciiz " "
.text
main:
	sub $sp, $sp, 4
	jal _main
	add $sp, $sp, 0
	lw $t1, 0($sp)
	add $sp, $sp, 4
	li $v0, 10
	syscall
_main:
	sub $sp, $sp, 4
	sw $s7, 0($sp)
	add $s7, $zero, $sp
	sw $ra, -4($s7)
	sw $s5, -8($s7)
	sw $s4, -12($s7)
	sw $s3, -16($s7)
	sw $s2, -20($s7)
	sw $s1, -24($s7)
	sw $s0, -28($s7)
	sub $sp, $sp, 92
	add $t0, $zero, 0
	sw $t0, -64($s7)
	add $t0, $zero, 0
	sw $t0, -68($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 0
	bgt $t0, $t1, L10
	add $t0, $zero, 0
	sw $t0, -72($s7)
	b L11
L10:
	add $t0, $zero, 1
	sw $t0, -72($s7)
L11:
	lw $t0, -72($s7)
	bne $t0, $zero L13
	b L39
L13:
	add $t0, $zero, 4
	sw $t0, -76($s7)
	add $t0, $zero, 0
	sw $t0, -68($s7)
L19:
	lw $t0, -68($s7)
	add $t1, $zero, 5
	blt $t0, $t1, L22
	add $t0, $zero, 0
	sw $t0, -80($s7)
	b L23
L22:
	add $t0, $zero, 1
	sw $t0, -80($s7)
L23:
	lw $t0, -80($s7)
	bne $t0, $zero L31
	b L39
L25:
	lw $t0, -68($s7)
	sw $t0, -88($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -84($s7)
	lw $t0, -84($s7)
	sw $t0, -68($s7)
	b L19
L31:
	lw $t0, -64($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -92($s7)
	lw $t0, -92($s7)
	sw $t0, -64($s7)
	b L39
	b L25
L39:
	lw $t0, -64($s7)
	sw $t0, 4($s7)
	add $sp, $s7, 4
	lw $s0, -28($s7)
	lw $s1, -24($s7)
	lw $s2, -20($s7)
	lw $s3, -16($s7)
	lw $s4, -12($s7)
	lw $s5, -8($s7)
	lw $ra, -4($s7)
	lw $s7, 0($s7)
	jr $ra
