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
add:
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
	sub $sp, $sp, 60
	lw $t0, 4($s7)
	sw $t0, 8($s7)
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
	sub $sp, $sp, 88
	add $t0, $zero, 0
	sw $t0, -64($s7)
L6:
	lw $t0, -64($s7)
	add $t1, $zero, 10
	blt $t0, $t1, L9
	add $t0, $zero, 0
	sw $t0, -68($s7)
	b L10
L9:
	add $t0, $zero, 1
	sw $t0, -68($s7)
L10:
	lw $t0, -68($s7)
	bne $t0, $zero L18
	b L29
L12:
	lw $t0, -64($s7)
	sw $t0, -76($s7)
	lw $t0, -64($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -72($s7)
	lw $t0, -72($s7)
	sw $t0, -64($s7)
	b L6
L18:
	add $t0, $zero, 12
	sw $t0, -80($s7)
	lw $t0, -64($s7)
	add $t1, $zero, 7
	blt $t0, $t1, L24
	add $t0, $zero, 0
	sw $t0, -84($s7)
	b L25
L24:
	add $t0, $zero, 1
	sw $t0, -84($s7)
L25:
	lw $t0, -84($s7)
	bne $t0, $zero L27
	b L27
L27:
	b L12
	b L12
L29:
	sub $sp, $sp, 4
	lw $t0, -64($s7)
	sw $t0, 0($sp)
	jal add
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -88($s7)
