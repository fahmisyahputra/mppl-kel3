from flask import Flask, render_template, request, jsonify
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

city_map = {
    # West Java
    'CILEGON': {'JAKARTA': 10},
    'JAKARTA': {'CILEGON': 10, 'CIKAMPEK': 8, 'BOGOR': 6},
    'BOGOR': {'JAKARTA': 6, 'BANDUNG': 3},
    'CIKAMPEK': {'JAKARTA': 8, 'BANDUNG': 8, 'CIREBON': 14},
    'BANDUNG': {'CIKAMPEK': 8, 'CIREBON': 14, 'TASIKMALAYA': 11, 'BOGOR': 13},
    'CIREBON': {'CIKAMPEK': 14, 'BANDUNG': 14, 'TEGAL': 8},
    'TASIKMALAYA': {'BANDUNG': 11, 'PURWOKERTO': 14},

    # Mid Java
    'TEGAL': {'CIREBON': 8, 'PURWOKERTO': 10, 'SEMARANG': 17},
    'PURWOKERTO': {'TEGAL': 10, 'YOGYAKARTA': 14, 'TASIKMALAYA': 14},
    'SEMARANG': {'TEGAL': 17, 'SURAKARTA': 10, 'KUDUS': 6},
    'SURAKARTA': {'SEMARANG': 10, 'YOGYAKARTA': 6, 'MADIUN': 11},
    'YOGYAKARTA': {'PURWOKERTO': 14, 'SURAKARTA': 6, 'PACITAN': 11},
    'KUDUS': {'REMBANG': 6, 'SEMARANG': 6},
    'REMBANG': {'KUDUS': 6, 'TUBAN': 10, 'MADIUN': 15},

    # East Java
    'MADIUN': {'SURAKARTA': 11, 'NGANJUK': 6, 'PONOROGO': 3, 'REMBANG': 15},
    'PONOROGO': {'MADIUN': 3, 'PACITAN': 8, 'TULUNGAGUNG': 9},
    'PACITAN': {'YOGYAKARTA': 11, 'PONOROGO': 8},
    'NGANJUK': {'SIDOARJO': 10, 'MADIUN': 6, 'TULUNGAGUNG': 7},
    'SIDOARJO': {'NGANJUK': 10, 'MALANG': 8, 'SURABAYA': 1, 'PROBOLINGGO': 10},
    'MALANG': {'SIDOARJO': 8, 'TULUNGAGUNG': 10, 'LUMAJANG': 9},
    'SURABAYA': {'SIDOARJO': 1, 'GRESIK': 2},
    'GRESIK': {'SURABAYA': 2, 'TUBAN': 9},
    'TULUNGAGUNG': {'PONOROGO': 9, 'MALANG': 10, 'NGANJUK': 7},
    'TUBAN': {'GRESIK': 9, 'REMBANG': 10},
    'PROBOLINGGO': {'SIDOARJO': 10, 'SITUBONDO': 11, 'LUMAJANG': 5},
    'BANYUWANGI': {'SITUBONDO': 10, 'JEMBER': 7},
    'JEMBER': {'BANYUWANGI': 7, 'LUMAJANG': 7, 'SITUBONDO': 7},
    'LUMAJANG': {'JEMBER': 7, 'MALANG': 9, 'PROBOLINGGO': 5},
    'SITUBONDO': {'JEMBER': 7, 'PROBOLINGGO': 11, 'BANYUWANGI': 10}
}

# BFS implementation
def bfs(graph, start, goal):
    queue = [(start, [start], 0)]  # Initial path and distance
    while queue:
        (vertex, path, distance) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next], distance + (graph[vertex][next] * 10)  # Multiply distance by 10
            else:
                queue.append((next, path + [next], distance + (graph[vertex][next] * 10)))  # Multiply distance by 10
    return None, None
