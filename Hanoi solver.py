def hanoi_solver(n):
    origen = list(range(n, 0, -1))
    auxiliar = []
    destino = []

    historial = []

    def formateo():
        return f'{origen} {auxiliar} {destino}'

    def mover(discos, desde, hacia, ayuda):
        if discos == 0:
            return

        mover(discos - 1, desde, ayuda, hacia)

        disco = desde.pop()
        hacia.append(disco)
        historial.append(formateo())

        mover(discos - 1, ayuda, hacia, desde)

    historial.append(formateo())

    mover(n, origen, destino, auxiliar)

    return '\n'.join(historial)

if __name__ == '__main__':
    print(hanoi_solver(3))