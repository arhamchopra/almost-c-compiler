.data
.text
main:
	add $t0, $zero, 2
	sw $t0, -8($sp)
	add $t0, $zero, 3
	sw $t0, -12($sp)
	lw $t0, -8($sp)
	lw $t1, -12($sp)
	add $t0, $t0, $t1
	sw $t0, -16($sp)
	lw $t0, -16($sp)
	sw $t0, -20($sp)
	li $v0, 1
	lw $t1, 0($sp)
	add $a0, $zero, $t1
	syscall
	li $v0, 10
	syscall
