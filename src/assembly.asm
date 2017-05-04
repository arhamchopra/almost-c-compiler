.data
	array: .space 40
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
partition:
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
	sub $sp, $sp, 216
	lw $t0, 8($s7)
	sw $t0, -64($s7)
	lw $t0, 8($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -72($s7)
	lw $t0, -72($s7)
	sw $t0, -68($s7)
L10:
	lw $t0, -68($s7)
	lw $t1, 4($s7)
	ble $t0, $t1, L13
	add $t0, $zero, 0
	sw $t0, -76($s7)
	b L14
L13:
	add $t0, $zero, 1
	sw $t0, -76($s7)
L14:
	lw $t0, -76($s7)
	bne $t0, $zero L23
	b L94
L16:
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -80($s7)
	lw $t0, -80($s7)
	sw $t0, -68($s7)
	b L10
L23:
	lw $t0, -64($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -84($s7)
	lw $t1, -84($s7)
	lw $t0, array($t1)
	sw $t0, -92($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -96($s7)
	lw $t1, -96($s7)
	lw $t0, array($t1)
	sw $t0, -104($s7)
	lw $t0, -92($s7)
	lw $t1, -104($s7)
	bgt $t0, $t1, L34
	add $t0, $zero, 0
	sw $t0, -108($s7)
	b L35
L34:
	add $t0, $zero, 1
	sw $t0, -108($s7)
L35:
	lw $t0, -108($s7)
	bne $t0, $zero L37
	b L16
L37:
	lw $t0, -68($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -116($s7)
	lw $t1, -116($s7)
	lw $t0, array($t1)
	sw $t0, -124($s7)
	lw $t0, -124($s7)
	sw $t0, -112($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -128($s7)
	lw $t1, -128($s7)
	lw $t0, array($t1)
	sw $t0, -136($s7)
	lw $t0, -64($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -140($s7)
	lw $t1, -140($s7)
	lw $t0, array($t1)
	sw $t0, -148($s7)
	lw $t1, -148($s7)
	lw $t0, -128($s7)
	sw $t1, array($t0)
	lw $t0, -64($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -152($s7)
	lw $t1, -152($s7)
	lw $t0, array($t1)
	sw $t0, -160($s7)
	lw $t1, -112($s7)
	lw $t0, -152($s7)
	sw $t1, array($t0)
	lw $t0, -68($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -164($s7)
	lw $t1, -164($s7)
	lw $t0, array($t1)
	sw $t0, -172($s7)
	lw $t0, -172($s7)
	sw $t0, -112($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -176($s7)
	lw $t1, -176($s7)
	lw $t0, array($t1)
	sw $t0, -184($s7)
	lw $t0, -64($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -188($s7)
	lw $t0, -188($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -192($s7)
	lw $t1, -192($s7)
	lw $t0, array($t1)
	sw $t0, -200($s7)
	lw $t1, -200($s7)
	lw $t0, -176($s7)
	sw $t1, array($t0)
	lw $t0, -64($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -204($s7)
	lw $t0, -204($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -208($s7)
	lw $t1, -208($s7)
	lw $t0, array($t1)
	sw $t0, -216($s7)
	lw $t1, -112($s7)
	lw $t0, -208($s7)
	sw $t1, array($t0)
	b L16
L94:
	lw $t0, -64($s7)
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
quicksort:
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
	lw $t0, 8($s7)
	lw $t1, 4($s7)
	bgt $t0, $t1, L99
	add $t0, $zero, 0
	sw $t0, -64($s7)
	b L100
L99:
	add $t0, $zero, 1
	sw $t0, -64($s7)
L100:
	lw $t0, -64($s7)
	bne $t0, $zero L102
	b L103
L102:
	add $t0, $zero, 1
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
L103:
	sub $sp, $sp, 4
	lw $t0, 8($s7)
	sw $t0, 0($sp)
	sub $sp, $sp, 4
	lw $t0, 4($s7)
	sw $t0, 0($sp)
	jal partition
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -72($s7)
	lw $t0, -72($s7)
	sw $t0, -68($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	sub $t0, $t0, $t1
	sw $t0, -76($s7)
	sub $sp, $sp, 4
	lw $t0, 8($s7)
	sw $t0, 0($sp)
	sub $sp, $sp, 4
	lw $t0, -76($s7)
	sw $t0, 0($sp)
	jal quicksort
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -80($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -84($s7)
	sub $sp, $sp, 4
	lw $t0, -84($s7)
	sw $t0, 0($sp)
	sub $sp, $sp, 4
	lw $t0, 4($s7)
	sw $t0, 0($sp)
	jal quicksort
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -88($s7)
	add $t0, $zero, 1
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
	sub $sp, $sp, 116
	add $t0, $zero, 0
	sw $t0, -64($s7)
L141:
	lw $t0, -64($s7)
	add $t1, $zero, 10
	blt $t0, $t1, L144
	add $t0, $zero, 0
	sw $t0, -72($s7)
	b L145
L144:
	add $t0, $zero, 1
	sw $t0, -72($s7)
L145:
	lw $t0, -72($s7)
	bne $t0, $zero L154
	b L165
L147:
	lw $t0, -64($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -76($s7)
	lw $t0, -76($s7)
	sw $t0, -64($s7)
	b L141
L154:
	add $t0, $s7, -68
	sw $t0, -80($s7)
	lw $t0, -80($s7)
	li $v0, 5
	syscall
	sw $v0, ($t0)
	lw $t0, -64($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -84($s7)
	lw $t1, -84($s7)
	lw $t0, array($t1)
	sw $t0, -92($s7)
	lw $t1, -68($s7)
	lw $t0, -84($s7)
	sw $t1, array($t0)
	b L147
L165:
	add $t0, $zero, 0
	sub $sp, $sp, 4
	sw $t0, 0($sp)
	add $t0, $zero, 9
	sub $sp, $sp, 4
	sw $t0, 0($sp)
	jal quicksort
	add $sp, $sp, 8
	lw $t1, 0($sp)
	add $sp, $sp, 4
	sw $t1, -96($s7)
	add $t0, $zero, 0
	sw $t0, -64($s7)
L176:
	lw $t0, -64($s7)
	add $t1, $zero, 10
	blt $t0, $t1, L179
	add $t0, $zero, 0
	sw $t0, -100($s7)
	b L180
L179:
	add $t0, $zero, 1
	sw $t0, -100($s7)
L180:
	lw $t0, -100($s7)
	bne $t0, $zero L189
	b L196
L182:
	lw $t0, -64($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -104($s7)
	lw $t0, -104($s7)
	sw $t0, -64($s7)
	b L176
L189:
	lw $t0, -64($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -108($s7)
	lw $t1, -108($s7)
	lw $t0, array($t1)
	sw $t0, -116($s7)
	lw $t0, -116($s7)
	li $v0, 1
	add $a0, $zero, $t0
	syscall
	li $v0, 4
	la $a0, spacebar
	syscall
	b L182
L196:
	add $t0, $zero, 0
	sw $t0, -64($s7)
	add $t0, $zero, 1
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
