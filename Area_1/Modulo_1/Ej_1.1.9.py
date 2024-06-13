saldoActual = float(input("Ingrese su saldo actual: "));

saldoAño1 = saldoActual + (saldoActual * 3) / 100;

saldoAño2 = saldoAño1 + (saldoAño1 * 3) / 100;

print("Saldo el primer año = $", saldoAño1);
print("Saldo el segundo año = $", saldoAño2);