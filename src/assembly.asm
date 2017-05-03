.data
	newline: .asciiz "\n"
	space: .asciiz " "
.text
main:
	sub $sp, $sp, 4
	jal _main
	add $sp, $sp, 0
	lw $t1, 0($sp)
	add $sp, $sp, 4
	li $v0, 10
	syscall
f1:
	sub $sp, $sp, 8
	sw $s7, 0($sp)
	add $s7, $zero, $sp
	sw $ra, -8($s7)
	sw $s5, -16($s7)
	sw $s4, -24($s7)
	sw $s3, -32($s7)
	sw $s2, -40($s7)
	sw $s1, -48($s7)
	sw $s0, -56($s7)
	sub $sp, $sp, 72
	lw $t0, 8($s7)
	add $t1, $zero, 0
	beq $t0, $t1, L4
	add $t0, $zero, 0
	sw $t0, -60($s7)
	b L5
L4:
	add $t0, $zero, 1
	sw $t0, -60($s7)
L5:
	lw $t0, -60($s7)
	bne $t0, $zero L7
	b L9
L7:
	add $t0, $zero, 1
	sw $t0, 12($s7)
	add $sp, $s7, 8
	lw $s0, -56($s7)
	lw $s1, -48($s7)
	lw $s2, -40($s7)
	lw $s3, -32($s7)
	lw $s4, -24($s7)
	lw $s5, -16($s7)
	lw $ra, -8($s7)
	lw $s7, 0($s7)
	jr $ra
	b L23
L9:
	lw $t0, 8($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -64($s7)
	sub $sp, $sp, 4
	lw $t0, -64($s7)
	sw $t0, 0($sp)
	jal f2
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -68($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 2
	mul $t0, $t0, $t1
	sw $t0, -72($s7)
	lw $t0, -72($s7)
	sw $t0, 12($s7)
	add $sp, $s7, 8
	lw $s0, -56($s7)
	lw $s1, -48($s7)
	lw $s2, -40($s7)
	lw $s3, -32($s7)
	lw $s4, -24($s7)
	lw $s5, -16($s7)
	lw $ra, -8($s7)
	lw $s7, 0($s7)
	jr $ra
L23:
f2:
	sub $sp, $sp, 8
	sw $s7, 0($sp)
	add $s7, $zero, $sp
	sw $ra, -8($s7)
	sw $s5, -16($s7)
	sw $s4, -24($s7)
	sw $s3, -32($s7)
	sw $s2, -40($s7)
	sw $s1, -48($s7)
	sw $s0, -56($s7)
	sub $sp, $sp, 72
	lw $t0, 8($s7)
	add $t1, $zero, 0
	beq $t0, $t1, L27
	add $t0, $zero, 0
	sw $t0, -60($s7)
	b L28
L27:
	add $t0, $zero, 1
	sw $t0, -60($s7)
L28:
	lw $t0, -60($s7)
	bne $t0, $zero L30
	b L32
L30:
	add $t0, $zero, 1
	sw $t0, 12($s7)
	add $sp, $s7, 8
	lw $s0, -56($s7)
	lw $s1, -48($s7)
	lw $s2, -40($s7)
	lw $s3, -32($s7)
	lw $s4, -24($s7)
	lw $s5, -16($s7)
	lw $ra, -8($s7)
	lw $s7, 0($s7)
	jr $ra
	b L46
L32:
	lw $t0, 8($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -64($s7)
	sub $sp, $sp, 4
	lw $t0, -64($s7)
	sw $t0, 0($sp)
	jal f1
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -68($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 2
	mul $t0, $t0, $t1
	sw $t0, -72($s7)
	lw $t0, -72($s7)
	sw $t0, 12($s7)
	add $sp, $s7, 8
	lw $s0, -56($s7)
	lw $s1, -48($s7)
	lw $s2, -40($s7)
	lw $s3, -32($s7)
	lw $s4, -24($s7)
	lw $s5, -16($s7)
	lw $ra, -8($s7)
	lw $s7, 0($s7)
	jr $ra
L46:
_main:
	sub $sp, $sp, 8
	sw $s7, 0($sp)
	add $s7, $zero, $sp
	sw $ra, -8($s7)
	sw $s5, -16($s7)
	sw $s4, -24($s7)
	sw $s3, -32($s7)
	sw $s2, -40($s7)
	sw $s1, -48($s7)
	sw $s0, -56($s7)
	sub $sp, $sp, 68
	add $t0, $s7, -60
	sw $t0, -64($s7)
	lw $t0, -64($s7)
	li $v0, 5
	syscall
	sw $v0, ($t0)
	sub $sp, $sp, 4
	lw $t0, -60($s7)
	sw $t0, 0($sp)
	jal f1
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -68($s7)
	lw $t0, -68($s7)
	li $v0, 1
	add $a0, $zero, $t0
	syscall
	add $t0, $zero, 0
	sw $t0, 8($s7)
	add $sp, $s7, 8
	lw $s0, -56($s7)
	lw $s1, -48($s7)
	lw $s2, -40($s7)
	lw $s3, -32($s7)
	lw $s4, -24($s7)
	lw $s5, -16($s7)
	lw $ra, -8($s7)
	lw $s7, 0($s7)
	jr $ra
