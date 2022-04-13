from django.db import models
import networkx as nx
import matplotlib.pyplot as plt
import random
import os
# Create your models here.


class Guess:
    def __init__(self):
        # self.n = []
        # The number of vertices
        self.nV = 6
        self.INF = 999
        # for _ in range(0, 15):
        #     temp = random.randint(2, 8)
        #     self.n.append(temp)
        # self.G = [[0, self.n[0], self.INF, self.n[9], self.INF, self.INF],
        #           [self.INF, 0, self.n[1], self.n[3], self.INF, self.INF],
        #           [self.n[2], self.INF, 0, self.n[4], self.INF, self.INF],
        #           [self.INF, self.INF, self.INF, 0, self.n[5], self.n[7]],
        #           [self.INF, self.INF, self.n[6], self.INF, 0, self.INF],
        #           [self.n[10], self.INF, self.INF, self.INF, self.n[8], 0]]

        self.n = self.newlist()
        self.G = self.matrix(self.n)
        self.floyd_warshall()
        # end
        # to find path
        self.MAXM = 10
        self.dis = [[-1 for i in range(self.MAXM)] for i in range(self.MAXM)]
        self.Next = [[-1 for i in range(self.MAXM)] for i in range(self.MAXM)]

        self.initialise()
        self.floydWarshall1()

    def savegraph(self):
        G = nx.DiGraph(directed=True)
        E = [(self.n[0][0], self.n[0][1], self.n[0][2]), (self.n[1][0], self.n[1][1], self.n[1][2]), (self.n[2][0], self.n[2][1], self.n[2][2]), (self.n[3][0], self.n[3][1], self.n[3][2]), (self.n[4][0], self.n[4][1], self.n[4][2]), (self.n[5][0], self.n[5][1], self.n[5][2]),
             (self.n[6][0], self.n[6][1], self.n[6][2]), (self.n[7][0], self.n[7][1], self.n[7][2]), (self.n[8][0], self.n[8][1], self.n[8][2]), (self.n[9][0], self.n[9][1], self.n[9][2]), (self.n[10][0], self.n[10][1], self.n[10][2]), (self.n[11][0], self.n[11][1], self.n[11][2])]
        G.add_weighted_edges_from(E)

        pos = nx.spiral_layout(G)

        options = {
            'node_color': 'red',
            'node_size': 700,
            'width': 2,
            'arrowstyle': '-|>',
            'arrowsize': 15,
        }
        # nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx(G, pos, arrows=True, **options)
        edge_weight = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        # plt.show()
        # os.remove("D:\\Django\\first\\static\\images\\graph.png")
        plt.savefig('D:\\Django\\first\\static\\images\\graph.png')
        plt.clf() 

    # Floyd Warshall Algorithm in python

    # Algorithm implementation
    def floyd_warshall(self):
        self.distance = list(map(lambda i: list(map(lambda j: j, i)), self.G))

        # Adding vertices individually
        for k in range(self.nV):
            for i in range(self.nV):
                for j in range(self.nV):
                    self.distance[i][j] = min(
                        self.distance[i][j], self.distance[i][k] + self.distance[k][j])
        self.print_solution()

        # Printing the solution
    def print_solution(self):
        for i in range(self.nV):
            for j in range(self.nV):
                if(self.distance[i][j] == self.INF):
                    print("INF", end=" ")
                else:
                    print(self.distance[i][j], end="  ")
            print(" ")

    def findpath(self, start, end):
        com = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        return self.distance[com[start]][com[end]]

    def initialise(self):
        for i in range(self.nV):
            for j in range(self.nV):
                self.dis[i][j] = self.G[i][j]

                # No edge between node
                # i and j
                if (self.G[i][j] == self.INF):
                    self.Next[i][j] = -1
                else:
                    self.Next[i][j] = j

    def floydWarshall1(self):
        for k in range(self.nV):
            for i in range(self.nV):
                for j in range(self.nV):

                    # We cannot travel through
                    # edge that doesn't exist
                    if (self.dis[i][k] == self.INF or self.dis[k][j] == self.INF):
                        continue
                    if (self.dis[i][j] > self.dis[i][k] + self.dis[k][j]):
                        self.dis[i][j] = self.dis[i][k] + self.dis[k][j]
                        self.Next[i][j] = self.Next[i][k]

    def constructPath(self, u, v):

        # If there's no path between
        # node u and v, simply return
        # an empty array
        if (self.Next[u][v] == -1):
            return []

        # Storing the path in a vector
        path = [u]
        while (u != v):
            u = self.Next[u][v]
            path.append(u)

        return path

    def tracepath(self):
        m = []
        for s in range(self.nV):
            sm = []
            for a in range(self.nV):
                sm.append(self.constructPath(s, a))
            m.append(sm)
        # print(m)
        # print(self.Next)
        return m

    def newlist(self):
        l = []
        for _ in range(50):
            alpha1 = chr(random.randint(ord('A'), ord('F')))
            alpha2 = chr(random.randint(ord('A'), ord('F')))
            if alpha1 != alpha2:
                l.append([alpha1, alpha2])

        nlist = []
        for item in l:
            if item not in nlist:
                nlist.append(item)
        
        b=[]
        for aa in nlist:
            if not any([set(aa) == set(bb) for bb in b if len(aa) == len(bb)]):
                b.append(aa)
        
        for i in range(len(b)):
            b[i].append(random.randint(1, 8))
        return b[:12]

    def matrix(self, n):
        d = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        g = [[self.INF, self.INF, self.INF, self.INF, self.INF, self.INF], [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF], [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF], [
            self.INF, self.INF, self.INF, self.INF, self.INF, self.INF], [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF], [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF]]
        for i in range(6):
            g[i][i] = 0
        for item in n:
            g[d[item[0]]][d[item[1]]] = item[2]
        return g
