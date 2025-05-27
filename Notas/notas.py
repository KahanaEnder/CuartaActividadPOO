import statistics

class Notas:

    @staticmethod
    def calcular(notas_list):
        
        if len(notas_list) != 5:
            raise ValueError("Debes ingresar exactamente 5 notas.")

        promedio = sum(notas_list) / len(notas_list)
        desviacion = statistics.stdev(notas_list)
        nota_max = max(notas_list)
        nota_min = min(notas_list)

        return {
            'promedio': promedio,
            'desviacion': desviacion,
            'max': nota_max,
            'min': nota_min,
        }