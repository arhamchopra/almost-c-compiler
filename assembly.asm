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
ackermann:
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
	sub $sp, $sp, 96
	lw $t0, 8($s7)
	add $t1, $zero, 0
	beq $t0, $t1, L4
	add $t0, $zero, 0
	sw $t0, -64($s7)
	b L5
L4:
	add $t0, $zero, 1
	sw $t0, -64($s7)
L5:
	lw $t0, -64($s7)
	bne $t0, $zero L7
	b L11
L7:
	lw $t0, 4($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -68($s7)
	lw $t0, -68($s7)
	sw $t0, 12($s7)
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
L11:
	lw $t0, 4($s7)
	add $t1, $zero, 0
	beq $t0, $t1, L14
	add $t0, $zero, 0
	sw $t0, -72($s7)
	b L15
L14:
	add $t0, $zero, 1
	sw $t0, -72($s7)
L15:
	lw $t0, -72($s7)
	bne $t0, $zero L17
	b L29
L17:
	lw $t0, 8($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -76($s7)
	sub $sp, $sp, 4
	lw $t0, -76($s7)
	sw $t0, 0($sp)
	add $t0, $zero, 1
	sub $sp, $sp, 4
	sw $t0, 0($sp)
	jal ackermann
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -80($s7)
	lw $t0, -80($s7)
	sw $t0, 12($s7)
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
L29:
	lw $t0, 8($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -84($s7)
	lw $t0, 4($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -88($s7)
	sub $sp, $sp, 4
	lw $t0, 8($s7)
	sw $t0, 0($sp)
	sub $sp, $sp, 4
	lw $t0, -88($s7)
	sw $t0, 0($sp)
	jal ackermann
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -92($s7)
	sub $sp, $sp, 4
	lw $t0, -84($s7)
	sw $t0, 0($sp)
	sub $sp, $sp, 4
	lw $t0, -92($s7)
	sw $t0, 0($sp)
	jal ackermann
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -96($s7)
	lw $t0, -96($s7)
	sw $t0, 12($s7)
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
	sub $sp, $sp, 80
	add $t0, $s7, -64
	sw $t0, -72($s7)
	lw $t0, -72($s7)
	li $v0, 5
	syscall
	sw $v0, ($t0)
	add $t0, $s7, -68
	sw $t0, -76($s7)
	lw $t0, -76($s7)
	li $v0, 5
	syscall
	sw $v0, ($t0)
	sub $sp, $sp, 4
	lw $t0, -64($s7)
	sw $t0, 0($sp)
	sub $sp, $sp, 4
	lw $t0, -68($s7)
	sw $t0, 0($sp)
	jal ackermann
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -80($s7)
	lw $t0, -80($s7)
	li $v0, 1
	add $a0, $zero, $t0
	syscall
	add $t0, $zero, 0
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
