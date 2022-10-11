.class public input
.super java/lang/Object
.field public static numero I
.method public static fatorial(I)I
.limit stack 5
.limit locals 100
iload 0
istore 0
ldc 1
istore 1
iload 0
iload 1
if_icmpgt true0
ldc 0
goto cmp_end0
true0:
ldc 1
cmp_end0:
istore 2
iload 2
ldc 0
if_icmpeq if_0
iload 0
istore 3
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 3
invokevirtual java/io/PrintStream/print(I)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc " "
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc ""
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
iload 0
istore 4
iload 0
istore 5
ldc 1
istore 6
iload 5
iload 6
isub
istore 7
iload 7
invokestatic input.fatorial(I)I
istore 8
iload 4
iload 8
imul
istore 9
iload 9
ireturn
if_0:
ldc 1
istore 10
iload 10
ireturn
.end method
.method public static resultado(I)V
.limit stack 5
.limit locals 100
ldc "Resultado: "
astore 11
iload 0
istore 12
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 11
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc " "
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 12
invokevirtual java/io/PrintStream/print(I)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc " "
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc ""
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
return
.end method
.method public static media(FF)F
.limit stack 5
.limit locals 100
.field public static m F
fload 0
fstore 13
fload 1
fstore 14
fload 13
fload 14
fadd
fstore 15
ldc 2
istore 16
iload 16
i2f
fstore 17
fload 15
fload 17
fdiv
fstore 18
fload 18
putstatic input/m F
getstatic input/m F
fstore 19
fload 19
freturn
.end method
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 100
ldc "Fatorial de N. Digite o n?mero?"
astore 20
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 20
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc " "
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc ""
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 21
iload 21
putstatic input/numero I
getstatic input/numero I
istore 22
iload 22
invokestatic input.fatorial(I)I
istore 23
iload 23
invokestatic input.resultado(I)V
return
.end method
