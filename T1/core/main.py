"""
ICS1113 - Optimizacion
Tarea 1, Pregunta 3b

Lee los archivos 'oferta.csv' y 'costos_demanda.csv' desde la carpeta
actual, construye el modelo de localizacion / transporte en Gurobi y
reporta la solucion optima (o informa infactibilidad).
"""

import csv
import sys
from typing import Tuple, List, Dict, Any

import gurobipy as gp
from gurobipy import GRB


def leer_oferta(ruta: str) -> Tuple[List[str],
                                    Dict[str, float], Dict[str, float]]:
    """Devuelve (origenes, s, F) donde:
    - origenes es la lista de IDs (como str) en el orden de aparicion,
    - s[i]  es la oferta maxima de la bodega i,
    - F[i]  es el costo fijo de arriendo de la bodega i.
    """
    origenes: List[str] = []
    s: Dict[str, float] = {}
    F: Dict[str, float] = {}
    with open(ruta, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # saltar encabezado
        for fila in reader:
            if not fila or all(c.strip() == "" for c in fila):
                continue
            i: str = fila[0].strip()
            origenes.append(i)
            s[i] = float(fila[1])
            F[i] = float(fila[2])
    return origenes, s, F


def leer_costos_demanda(ruta: str,
                        origenes: List[str]) -> Tuple[List[str],
                                                      Dict[Tuple[str, str], float],
                                                      Dict[str, float]]:
    """Devuelve (destinos, c, d) donde:
    - destinos es la lista de IDs de clientes (como str),
    - c[(i,j)] es el costo unitario de enviar de bodega i a cliente j,
    - d[j]    es la demanda del cliente j.
    """
    with open(ruta, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        filas: List[List[str]] = [fila for fila in reader if fila and any(
            celda.strip() != "" for celda in fila)]

    encabezado: List[str] = filas[0]
    destinos: List[str] = [x.strip() for x in encabezado[1:]]

    c: Dict[Tuple[str, str], float] = {}
    d: Dict[str, float] = {}

    for fila in filas[1:-1]:
        i: str = fila[0].strip()
        for k, j in enumerate(destinos):
            c[(i, j)] = float(fila[k + 1])

    fila_demanda: List[str] = filas[-1]
    for k, j in enumerate(destinos):
        d[j] = float(fila_demanda[k + 1])

    return destinos, c, d


def main() -> None:
    # ---------- Lectura de datos ----------
    ruta_oferta: str = "oferta.csv"
    ruta_costos: str = "costos_demanda.csv"

    try:
        origenes, s, F = leer_oferta(ruta_oferta)
        destinos, c, d = leer_costos_demanda(ruta_costos, origenes)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("La tarea debe ser ejecutada desde la carpeta que contiene oferta.csv y costos_demanda.csv")
        sys.exit(1)

    # ---------- Modelo ----------
    modelo: gp.Model = gp.Model("Localizacion_Transporte")
    modelo.setParam("OutputFlag", 0)  # silenciar el log de Gurobi

    # Variables
    x = modelo.addVars(
        origenes,
        destinos,
        lb=0.0,
        vtype=GRB.CONTINUOUS,
        name="x")
    y = modelo.addVars(origenes, vtype=GRB.BINARY, name="y")

    # Funcion objetivo: costos de transporte + costos fijos de arriendo
    modelo.setObjective(
        gp.quicksum(c[(i, j)] * x[i, j] for i in origenes for j in destinos)
        + gp.quicksum(F[i] * y[i] for i in origenes),
        GRB.MINIMIZE,
    )

    # (4) Capacidad + ligadura con la decision de arriendo
    modelo.addConstrs(
        (gp.quicksum(x[i, j] for j in destinos) <= s[i] * y[i] for i in origenes),
        name="capacidad",
    )

    # (5) Demanda exacta de cada cliente
    modelo.addConstrs(
        (gp.quicksum(x[i, j] for i in origenes) == d[j] for j in destinos),
        name="demanda",
    )

    modelo.optimize()

    # ---------- Reporte ----------
    if modelo.status == GRB.OPTIMAL:
        print("Estado: OPTIMO")
        print(f"Valor optimo: {modelo.objVal:.4f}")

        print("Bodegas arrendadas:")
        for i in origenes:
            if y[i].X > 0.5:
                print(f"Se decidió arrendar la bodega {i}")

        print("Envios realizados:")
        for i in origenes:
            for j in destinos:
                cantidad: float = x[i, j].X
                if cantidad > 1e-6:
                    print(
                        f"Se enviaron {
                            cantidad:g} unidades al cliente {j} desde la bodega {i}")

    elif modelo.status in (GRB.INFEASIBLE, GRB.INF_OR_UNBD):
        print("Estado: INFACTIBLE")
    else:
        print(f"Estado: OTRO (codigo Gurobi {modelo.status})")

if __name__ == "__main__":
    main()
