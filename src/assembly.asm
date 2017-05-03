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
	sub $sp, $sp, 88
L1:
	add $t0, $zero, 0
	sw $t0, -64($s7)
L4:
	add $t0, $zero, 1
	sw $t0, -64($s7)
L5:
L7:
	lw $t0, -60($s7)
	add $t1, $zero, 10
	add $t0, $t0, $t1
	sw $t0, -72($s7)
	lw $t0, -72($s7)
	sw $t0, -68($s7)
	lw $t0, -60($s7)
	sw $t0, -80($s7)
	lw $t0, -60($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -76($s7)
	lw $t0, -76($s7)
	sw $t0, -60($s7)
	lw $t0, -84($s7)
	sw $t0, -68($s7)
L25:
	lw $t0, -88($s7)
	sw $t0, -60($s7)
	add $t0, $zero, 1000
	sw $t0, -60($s7)
