.data
	a: .word 0 
	b: .word 0 
	c: .space 80
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
	sub $sp, $sp, 96
	add $t0, $zero, 5
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -68($s7)
	add $t0, $s7, -84
	sw $t0, -76($s7)
	lw $t0, -76($s7)
	lw $t1, -68($s7)
	add $t0, $t0, $t1
	sw $t0, -72($s7)
	lw $t1, -72($s7)
	lw $t0, ($t1)
	sw $t0, -80($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 5
	sw $t1, ($t0)
	add $t0, $zero, 5
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -84($s7)
	add $t0, $s7, -84
	sw $t0, -92($s7)
	lw $t0, -92($s7)
	lw $t1, -84($s7)
	add $t0, $t0, $t1
	sw $t0, -88($s7)
	lw $t1, -88($s7)
	lw $t0, ($t1)
	sw $t0, -96($s7)
	lw $t0, -96($s7)
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
