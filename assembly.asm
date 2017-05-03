.data
.text
main:
	sub $sp, $sp, 4
	jal _main
	add $sp, $sp, 0
	lw $t1, 0($sp)
	add $sp, $sp, 4
	li $v0, 1
	add $a0, $zero, $t1
	syscall
	li $v0, 10
	syscall
rfib:
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
	sub $sp, $sp, 84
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
	b L8
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
L8:
	lw $t0, 8($s7)
	add $t1, $zero, 1
	beq $t0, $t1, L11
	add $t0, $zero, 0
	sw $t0, -64($s7)
	b L12
L11:
	add $t0, $zero, 1
	sw $t0, -64($s7)
L12:
	lw $t0, -64($s7)
	bne $t0, $zero L14
	b L15
L14:
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
L15:
	lw $t0, 8($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -68($s7)
	sub $sp, $sp, 4
	lw $t0, -68($s7)
	sw $t0, 0($sp)
	jal rfib
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -72($s7)
	lw $t0, 8($s7)
	add $t1, $zero, 2
	sub $t0, $t0, $t1
	sw $t0, -76($s7)
	sub $sp, $sp, 4
	lw $t0, -76($s7)
	sw $t0, 0($sp)
	jal rfib
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -80($s7)
	lw $t0, -72($s7)
	lw $t1, -80($s7)
	add $t0, $t0, $t1
	sw $t0, -84($s7)
	lw $t0, -84($s7)
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
	sub $sp, $sp, 64
	add $t0, $zero, 9
	sw $t0, -60($s7)
	sub $sp, $sp, 4
	lw $t0, -60($s7)
	sw $t0, 0($sp)
	jal rfib
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -64($s7)
	lw $t0, -64($s7)
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
