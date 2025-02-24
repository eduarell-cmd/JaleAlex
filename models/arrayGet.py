class ProcesoVenta:
    def __init__(self, carro, cliente):
        self.carro = carro
        self.cliente = cliente

    def validar_costo(self):
        precio_carro = self.carro.precio
        opciones_financiamiento = {
            12: 0.05,  
            24: 0.10,  
            32: 0.15   
        }

        
        porcentaje_enganche = float(input("Ingrese el porcentaje de enganche (entre 20 y 50): "))
        if porcentaje_enganche < 20 or porcentaje_enganche > 50:
            raise ValueError("El porcentaje de enganche debe estar entre 20 y 50")

        enganche = precio_carro * (porcentaje_enganche / 100)

        tabla_financiamiento = []

        for meses, interes in opciones_financiamiento.items():
            monto_financiado = precio_carro - enganche
            monto_total_con_interes = monto_financiado * (1 + interes)
            mensualidad = monto_total_con_interes / meses
            tabla_financiamiento.append({
            'meses': meses,
            'enganche': enganche,
            'mensualidad': mensualidad,
            'interes': interes,
            'monto_total_con_interes': monto_total_con_interes
            })

        return tabla_financiamiento
