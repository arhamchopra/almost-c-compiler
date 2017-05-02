.data
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
	sub $sp, $sp, 60
	lw $t0, 12($s7)
	lw $t1, 8($s7)
	add $t0, $t0, $t1
	sw $t0, -60($s7)
	lw $t0, -60($s7)
	sw $t0, 16($s7)
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
	sub $sp, $sp, 60
	sub $sp, $sp, 4
	add $t0, $zero, 2
	sub $sp, $sp, 4
	sw $t0, 0($sp)
	add $t0, $zero, 3
	sub $sp, $sp, 4
	sw $t0, 0($sp)
	jal add
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -60($s7)
	add $t0, $zero, 1
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
