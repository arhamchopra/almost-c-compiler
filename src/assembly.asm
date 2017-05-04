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
	sub $sp, $sp, 468
	add $t0, $zero, 2
	sw $t0, -64($s7)
	add $t0, $zero, 0
	sw $t0, -80($s7)
	add $t0, $zero, 0
	sw $t0, -68($s7)
L10:
	lw $t0, -68($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L13
	add $t0, $zero, 0
	sw $t0, -132($s7)
	b L14
L13:
	add $t0, $zero, 1
	sw $t0, -132($s7)
L14:
	lw $t0, -132($s7)
	bne $t0, $zero L22
	b L53
L16:
	lw $t0, -68($s7)
	sw $t0, -140($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -136($s7)
	lw $t0, -136($s7)
	sw $t0, -68($s7)
	b L10
L22:
	add $t0, $zero, 0
	sw $t0, -72($s7)
L25:
	lw $t0, -72($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L28
	add $t0, $zero, 0
	sw $t0, -144($s7)
	b L29
L28:
	add $t0, $zero, 1
	sw $t0, -144($s7)
L29:
	lw $t0, -144($s7)
	bne $t0, $zero L37
	b L16
L31:
	lw $t0, -72($s7)
	sw $t0, -152($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -148($s7)
	lw $t0, -148($s7)
	sw $t0, -72($s7)
	b L25
L37:
	lw $t0, -68($s7)
	add $t1, $zero, 8
	mul $t0, $t0, $t1
	sw $t0, -156($s7)
	add $t0, $s7, -96
	sw $t0, -168($s7)
	lw $t0, -168($s7)
	lw $t1, -156($s7)
	add $t0, $t0, $t1
	sw $t0, -160($s7)
	lw $t1, -160($s7)
	lw $t0, ($t1)
	sw $t0, -176($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -180($s7)
	lw $t0, -160($s7)
	lw $t1, -180($s7)
	add $t0, $t0, $t1
	sw $t0, -184($s7)
	lw $t1, -184($s7)
	lw $t0, ($t1)
	sw $t0, -188($s7)
	lw $t0, -184($s7)
	sw $t0, -192($s7)
	lw $t0, -192($s7)
	li $v0, 5
	syscall
	sw $v0, ($t0)
	b L31
	b L16
L53:
	add $t0, $zero, 0
	sw $t0, -68($s7)
L56:
	lw $t0, -68($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L59
	add $t0, $zero, 0
	sw $t0, -196($s7)
	b L60
L59:
	add $t0, $zero, 1
	sw $t0, -196($s7)
L60:
	lw $t0, -196($s7)
	bne $t0, $zero L68
	b L99
L62:
	lw $t0, -68($s7)
	sw $t0, -204($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -200($s7)
	lw $t0, -200($s7)
	sw $t0, -68($s7)
	b L56
L68:
	add $t0, $zero, 0
	sw $t0, -72($s7)
L71:
	lw $t0, -72($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L74
	add $t0, $zero, 0
	sw $t0, -208($s7)
	b L75
L74:
	add $t0, $zero, 1
	sw $t0, -208($s7)
L75:
	lw $t0, -208($s7)
	bne $t0, $zero L83
	b L62
L77:
	lw $t0, -72($s7)
	sw $t0, -216($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -212($s7)
	lw $t0, -212($s7)
	sw $t0, -72($s7)
	b L71
L83:
	lw $t0, -68($s7)
	add $t1, $zero, 8
	mul $t0, $t0, $t1
	sw $t0, -220($s7)
	add $t0, $s7, -112
	sw $t0, -232($s7)
	lw $t0, -232($s7)
	lw $t1, -220($s7)
	add $t0, $t0, $t1
	sw $t0, -224($s7)
	lw $t1, -224($s7)
	lw $t0, ($t1)
	sw $t0, -240($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -244($s7)
	lw $t0, -224($s7)
	lw $t1, -244($s7)
	add $t0, $t0, $t1
	sw $t0, -248($s7)
	lw $t1, -248($s7)
	lw $t0, ($t1)
	sw $t0, -252($s7)
	lw $t0, -248($s7)
	sw $t0, -256($s7)
	lw $t0, -256($s7)
	li $v0, 5
	syscall
	sw $v0, ($t0)
	b L77
	b L62
L99:
	add $t0, $zero, 0
	sw $t0, -68($s7)
L102:
	lw $t0, -68($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L105
	add $t0, $zero, 0
	sw $t0, -260($s7)
	b L106
L105:
	add $t0, $zero, 1
	sw $t0, -260($s7)
L106:
	lw $t0, -260($s7)
	bne $t0, $zero L114
	b L195
L108:
	lw $t0, -68($s7)
	sw $t0, -268($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -264($s7)
	lw $t0, -264($s7)
	sw $t0, -68($s7)
	b L102
L114:
	add $t0, $zero, 0
	sw $t0, -72($s7)
L117:
	lw $t0, -72($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L120
	add $t0, $zero, 0
	sw $t0, -272($s7)
	b L121
L120:
	add $t0, $zero, 1
	sw $t0, -272($s7)
L121:
	lw $t0, -272($s7)
	bne $t0, $zero L129
	b L108
L123:
	lw $t0, -72($s7)
	sw $t0, -280($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -276($s7)
	lw $t0, -276($s7)
	sw $t0, -72($s7)
	b L117
L129:
	add $t0, $zero, 0
	sw $t0, -76($s7)
L132:
	lw $t0, -76($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L135
	add $t0, $zero, 0
	sw $t0, -284($s7)
	b L136
L135:
	add $t0, $zero, 1
	sw $t0, -284($s7)
L136:
	lw $t0, -284($s7)
	bne $t0, $zero L144
	b L176
L138:
	lw $t0, -76($s7)
	sw $t0, -292($s7)
	lw $t0, -76($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -288($s7)
	lw $t0, -288($s7)
	sw $t0, -76($s7)
	b L132
L144:
	lw $t0, -68($s7)
	add $t1, $zero, 8
	mul $t0, $t0, $t1
	sw $t0, -296($s7)
	add $t0, $s7, -96
	sw $t0, -308($s7)
	lw $t0, -308($s7)
	lw $t1, -296($s7)
	add $t0, $t0, $t1
	sw $t0, -300($s7)
	lw $t1, -300($s7)
	lw $t0, ($t1)
	sw $t0, -316($s7)
	lw $t0, -76($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -320($s7)
	lw $t0, -300($s7)
	lw $t1, -320($s7)
	add $t0, $t0, $t1
	sw $t0, -324($s7)
	lw $t1, -324($s7)
	lw $t0, ($t1)
	sw $t0, -328($s7)
	lw $t0, -76($s7)
	add $t1, $zero, 8
	mul $t0, $t0, $t1
	sw $t0, -332($s7)
	add $t0, $s7, -112
	sw $t0, -344($s7)
	lw $t0, -344($s7)
	lw $t1, -332($s7)
	add $t0, $t0, $t1
	sw $t0, -336($s7)
	lw $t1, -336($s7)
	lw $t0, ($t1)
	sw $t0, -352($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -356($s7)
	lw $t0, -336($s7)
	lw $t1, -356($s7)
	add $t0, $t0, $t1
	sw $t0, -360($s7)
	lw $t1, -360($s7)
	lw $t0, ($t1)
	sw $t0, -364($s7)
	lw $t0, -328($s7)
	lw $t1, -364($s7)
	mul $t0, $t0, $t1
	sw $t0, -368($s7)
	lw $t0, -80($s7)
	lw $t1, -368($s7)
	add $t0, $t0, $t1
	sw $t0, -372($s7)
	lw $t0, -372($s7)
	sw $t0, -80($s7)
	b L138
L176:
	lw $t0, -68($s7)
	add $t1, $zero, 8
	mul $t0, $t0, $t1
	sw $t0, -376($s7)
	add $t0, $s7, -128
	sw $t0, -388($s7)
	lw $t0, -388($s7)
	lw $t1, -376($s7)
	add $t0, $t0, $t1
	sw $t0, -380($s7)
	lw $t1, -380($s7)
	lw $t0, ($t1)
	sw $t0, -396($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -400($s7)
	lw $t0, -380($s7)
	lw $t1, -400($s7)
	add $t0, $t0, $t1
	sw $t0, -404($s7)
	lw $t1, -404($s7)
	lw $t0, ($t1)
	sw $t0, -408($s7)
	lw $t0, -404($s7)
	lw $t1, -80($s7)
	sw $t1, ($t0)
	add $t0, $zero, 0
	sw $t0, -80($s7)
	b L123
	b L108
L195:
	li $v0, 4
	la $a0, newline
	syscall
	add $t0, $zero, 0
	sw $t0, -68($s7)
L199:
	lw $t0, -68($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L202
	add $t0, $zero, 0
	sw $t0, -412($s7)
	b L203
L202:
	add $t0, $zero, 1
	sw $t0, -412($s7)
L203:
	lw $t0, -412($s7)
	bne $t0, $zero L211
	b L242
L205:
	lw $t0, -68($s7)
	sw $t0, -420($s7)
	lw $t0, -68($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -416($s7)
	lw $t0, -416($s7)
	sw $t0, -68($s7)
	b L199
L211:
	add $t0, $zero, 0
	sw $t0, -72($s7)
L214:
	lw $t0, -72($s7)
	lw $t1, -64($s7)
	blt $t0, $t1, L217
	add $t0, $zero, 0
	sw $t0, -424($s7)
	b L218
L217:
	add $t0, $zero, 1
	sw $t0, -424($s7)
L218:
	lw $t0, -424($s7)
	bne $t0, $zero L226
	b L240
L220:
	lw $t0, -72($s7)
	sw $t0, -432($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 1
	add $t0, $t0, $t1
	sw $t0, -428($s7)
	lw $t0, -428($s7)
	sw $t0, -72($s7)
	b L214
L226:
	lw $t0, -68($s7)
	add $t1, $zero, 8
	mul $t0, $t0, $t1
	sw $t0, -436($s7)
	add $t0, $s7, -128
	sw $t0, -448($s7)
	lw $t0, -448($s7)
	lw $t1, -436($s7)
	add $t0, $t0, $t1
	sw $t0, -440($s7)
	lw $t1, -440($s7)
	lw $t0, ($t1)
	sw $t0, -456($s7)
	lw $t0, -72($s7)
	add $t1, $zero, 4
	mul $t0, $t0, $t1
	sw $t0, -460($s7)
	lw $t0, -440($s7)
	lw $t1, -460($s7)
	add $t0, $t0, $t1
	sw $t0, -464($s7)
	lw $t1, -464($s7)
	lw $t0, ($t1)
	sw $t0, -468($s7)
	lw $t0, -468($s7)
	li $v0, 1
	add $a0, $zero, $t0
	syscall
	li $v0, 4
	la $a0, spacebar
	syscall
	b L220
L240:
	li $v0, 4
	la $a0, newline
	syscall
	b L205
L242:
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
